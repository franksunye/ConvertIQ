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
        # 创建透视表
        pivot_table = metrics.pivot(
            index='sales_id',
            columns='repair_part',
            values='conversion_rate'
        )
        
        fig = go.Figure(data=go.Heatmap(
            z=pivot_table.values,
            x=pivot_table.columns,
            y=pivot_table.index,
            colorscale='Viridis'
        ))
        
        fig.update_layout(
            title="销售员表现热力图",
            xaxis_title="维修部位",
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