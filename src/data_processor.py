import pandas as pd
from datetime import datetime
from typing import Dict, Union, List

class DataProcessor:
    def __init__(self):
        self.leads_df = None
        self.followup_df = None

    def load_data(self, leads_file: Union[str, pd.DataFrame], followup_file: Union[str, pd.DataFrame]):
        """加载线索和跟进数据"""
        # 如果是文件路径，则读取CSV文件
        if isinstance(leads_file, str):
            self.leads_df = pd.read_csv(leads_file)
        else:
            self.leads_df = leads_file
            
        if isinstance(followup_file, str):
            self.followup_df = pd.read_csv(followup_file)
        else:
            self.followup_df = followup_file
        
        # 转换时间列
        time_columns = [
            'created_at', 'first_contact_time', 'scheduled_inspection_time',
            'inspection_done_time', 'quote_time', 'contract_signed_time',
            'payment_done_time'
        ]
        
        for col in time_columns:
            if col in self.leads_df.columns:
                self.leads_df[col] = pd.to_datetime(self.leads_df[col])
            if col in self.followup_df.columns:
                self.followup_df[col] = pd.to_datetime(self.followup_df[col])

    def calculate_funnel_metrics(self) -> Dict[str, float]:
        """计算销售漏斗各阶段指标"""
        metrics = {
            'leads_created': len(self.leads_df),
            'contacted': len(self.followup_df[self.followup_df['first_contact_time'].notna()]),
            'inspected': len(self.followup_df[self.followup_df['inspection_done_time'].notna()]),
            'quoted': len(self.followup_df[self.followup_df['quote_time'].notna()]),
            'signed': len(self.followup_df[self.followup_df['contract_signed_time'].notna()]),
            'paid': len(self.followup_df[self.followup_df['payment_done_time'].notna()])
        }
        
        # 计算转化率
        total_leads = metrics['leads_created']
        for stage in list(metrics.keys()):
            if stage != 'leads_created':
                metrics[f'{stage}_rate'] = metrics[stage] / total_leads
        
        return metrics

    def calculate_repair_part_metrics(self) -> pd.DataFrame:
        """计算各维修部位的转化指标"""
        merged_df = pd.merge(
            self.leads_df,
            self.followup_df,
            on='lead_id',
            how='left'
        )
        
        metrics = merged_df.groupby('repair_part').agg({
            'lead_id': 'count',
            'quote_amount': 'mean',
            'final_status': lambda x: (x == '成交').mean()
        }).rename(columns={
            'lead_id': 'total_leads',
            'quote_amount': 'avg_quote',
            'final_status': 'conversion_rate'
        })
        
        return metrics.reset_index()

    def calculate_sales_performance(self) -> pd.DataFrame:
        """计算销售员表现指标"""
        merged_df = pd.merge(
            self.leads_df,
            self.followup_df,
            on='lead_id',
            how='left'
        )
        
        # 确保时间列是datetime类型
        merged_df['created_at'] = pd.to_datetime(merged_df['created_at'])
        merged_df['first_contact_time'] = pd.to_datetime(merged_df['first_contact_time'])
        
        metrics = merged_df.groupby('sales_id').agg({
            'lead_id': 'count',
            'quote_amount': 'mean',
            'final_status': lambda x: (x == '成交').mean(),
            'first_contact_time': lambda x: (x - merged_df['created_at']).mean().total_seconds() / 3600  # 转换为小时
        }).rename(columns={
            'lead_id': 'total_leads',
            'quote_amount': 'avg_quote',
            'final_status': 'conversion_rate',
            'first_contact_time': 'avg_response_time'
        })
        
        return metrics.reset_index()

    def calculate_quote_analysis(self) -> pd.DataFrame:
        """分析报价与成交关系"""
        merged_df = pd.merge(
            self.leads_df,
            self.followup_df,
            on='lead_id',
            how='left'
        )
        
        analysis_df = merged_df[['lead_id', 'quote_amount', 'final_status', 'repair_part', 'sales_id']].copy()
        analysis_df['converted'] = analysis_df['final_status'] == '成交'
        
        return analysis_df 
        # 只分析有报价的记录
        quoted_df = merged_df[merged_df['quote_amount'].notna()].copy()
        quoted_df['converted'] = quoted_df['contract_signed_time'].notna()
        
        return quoted_df[['lead_id', 'quote_amount', 'converted', 'repair_part', 'sales_id']] 