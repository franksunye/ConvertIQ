import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict

class Visualizer:
    @staticmethod
    def create_funnel_chart(metrics: Dict[str, float]) -> go.Figure:
        """创建销售转化漏斗图"""
        stages = ['leads_created', 'contacted', 'inspected', 'quoted', 'signed', 'paid']
        values = [metrics[stage] for stage in stages]
        
        fig = go.Figure(go.Funnel(
            y=stages,
            x=values,
            textinfo="value+percent initial"
        ))
        
        fig.update_layout(
            title="销售转化漏斗",
            showlegend=False,
            height=500
        )
        
        return fig
    
    @staticmethod
    def create_repair_part_chart(metrics: pd.DataFrame) -> go.Figure:
        """创建维修部位转化率分析图"""
        fig = go.Figure()
        
        # 添加转化率柱状图
        fig.add_trace(go.Bar(
            x=metrics['repair_part'],
            y=metrics['conversion_rate'],
            name='转化率',
            marker_color='rgb(55, 83, 109)'
        ))
        
        # 添加平均报价折线图
        fig.add_trace(go.Scatter(
            x=metrics['repair_part'],
            y=metrics['avg_quote'],
            name='平均报价',
            yaxis='y2',
            line=dict(color='rgb(26, 118, 255)')
        ))
        
        fig.update_layout(
            title="维修部位转化率分析",
            xaxis_title="维修部位",
            yaxis_title="转化率",
            yaxis2=dict(
                title="平均报价",
                overlaying='y',
                side='right'
            ),
            showlegend=True,
            height=500
        )
        
        return fig
    
    @staticmethod
    def create_sales_heatmap(metrics: pd.DataFrame) -> go.Figure:
        """创建销售员表现热力图"""
        # 创建热力图
        fig = go.Figure(data=go.Heatmap(
            z=metrics[['conversion_rate', 'avg_quote', 'avg_response_time']].values,
            x=['转化率', '平均报价', '平均响应时间'],
            y=metrics['sales_id'],
            colorscale='Viridis'
        ))
        
        fig.update_layout(
            title="销售员表现热力图",
            xaxis_title="指标",
            yaxis_title="销售员",
            height=500
        )
        
        return fig
    
    @staticmethod
    def create_quote_analysis_chart(data: pd.DataFrame) -> go.Figure:
        """创建报价与成交关系分析图"""
        # 将final_status映射为'成交'/'未成交'
        data = data.copy()
        data['成交情况'] = data['final_status'].apply(lambda x: '成交' if x == '成交' else '未成交')
        fig = px.scatter(
            data,
            x='quote_amount',
            y='成交情况',
            color='repair_part',
            hover_data=['sales_id'],
            category_orders={'成交情况': ['未成交', '成交']},
            title="报价与成交关系分析"
        )
        
        fig.update_layout(
            xaxis_title="报价金额",
            yaxis_title="是否成交",
            height=500
        )
        
        return fig

    @staticmethod
    def create_sales_repair_heatmap(metrics: pd.DataFrame) -> go.Figure:
        """创建销售员在各维修部位的转化率热力图"""
        # 计算每个销售员在每个维修部位的转化率
        pivot_data = metrics.groupby(['sales_id', 'repair_part']).agg({
            'final_status': lambda x: (x == '成交').mean()
        }).reset_index()
        
        # 创建透视表
        pivot_table = pivot_data.pivot(
            index='sales_id',
            columns='repair_part',
            values='final_status'
        )
        
        fig = go.Figure(data=go.Heatmap(
            z=pivot_table.values,
            x=pivot_table.columns,
            y=pivot_table.index,
            colorscale='Greens',  # 使用绿色色阶
            zmin=0,
            zmax=1,
            text=[[f'{val:.1%}' if not pd.isna(val) else '' for val in row] for row in pivot_table.values],
            texttemplate='%{text}',
            textfont={"size": 10},
            hoverongaps=False
        ))
        
        fig.update_layout(
            title="销售员在各维修部位的转化率",
            xaxis_title="维修部位",
            yaxis_title="销售员",
            height=500
        )
        
        return fig

    @staticmethod
    def create_sales_ranking(metrics: pd.DataFrame) -> go.Figure:
        """创建销售员转化率排名表"""
        # 计算每个销售员的总体转化率
        sales_metrics = metrics.groupby('sales_id').agg({
            'final_status': lambda x: (x == '成交').mean(),
            'lead_id': 'count'
        }).rename(columns={
            'final_status': 'conversion_rate',
            'lead_id': 'total_leads'
        })
        
        # 按转化率排序
        sales_metrics = sales_metrics.sort_values('conversion_rate')
        
        # 创建条形图
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=sales_metrics.index,
            y=sales_metrics['conversion_rate'],
            text=[f'{rate:.1%}' for rate in sales_metrics['conversion_rate']],
            textposition='auto',
            marker_color='rgb(55, 83, 109)'
        ))
        
        fig.update_layout(
            title="销售员转化率排名",
            xaxis_title="销售员",
            yaxis_title="转化率",
            height=500,
            yaxis=dict(
                tickformat='.1%',
                range=[0, max(sales_metrics['conversion_rate']) * 1.1]
            )
        )
        
        return fig

    @staticmethod
    def create_repair_part_ratio(metrics: pd.DataFrame) -> go.Figure:
        """创建维修部位成交率与线索占比分析图"""
        # 计算每个维修部位的总线索数和成交数
        repair_metrics = metrics.groupby('repair_part').agg({
            'lead_id': 'count',
            'final_status': lambda x: (x == '成交').sum()
        }).rename(columns={
            'lead_id': 'total_leads',
            'final_status': 'converted_leads'
        })
        
        # 计算总体线索数和成交数
        total_leads = repair_metrics['total_leads'].sum()
        total_converted = repair_metrics['converted_leads'].sum()
        
        # 计算占比
        repair_metrics['lead_ratio'] = repair_metrics['total_leads'] / total_leads
        repair_metrics['conversion_rate'] = repair_metrics['converted_leads'] / repair_metrics['total_leads']
        
        # 创建双轴图
        fig = go.Figure()
        
        # 添加线索占比柱状图
        fig.add_trace(go.Bar(
            x=repair_metrics.index,
            y=repair_metrics['lead_ratio'],
            name='线索占比',
            marker_color='rgb(55, 83, 109)'
        ))
        
        # 添加转化率折线图
        fig.add_trace(go.Scatter(
            x=repair_metrics.index,
            y=repair_metrics['conversion_rate'],
            name='转化率',
            yaxis='y2',
            line=dict(color='rgb(26, 118, 255)')
        ))
        
        fig.update_layout(
            title="维修部位成交率与线索占比分析",
            xaxis_title="维修部位",
            yaxis_title="线索占比",
            yaxis2=dict(
                title="转化率",
                overlaying='y',
                side='right',
                tickformat='.1%'
            ),
            yaxis=dict(
                tickformat='.1%'
            ),
            showlegend=True,
            height=500
        )
        
        return fig 