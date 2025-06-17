import pytest
import pandas as pd
import plotly.graph_objects as go
from src.visualizer import Visualizer

@pytest.fixture
def sample_metrics():
    # 创建示例漏斗指标
    funnel_metrics = {
        'leads_created': 100,
        'contacted': 80,
        'inspected': 60,
        'quoted': 40,
        'signed': 20,
        'paid': 10
    }
    
    # 创建示例维修部位指标
    repair_part_metrics = pd.DataFrame({
        'repair_part': ['卫生间', '厨房', '阳台'],
        'conversion_rate': [0.3, 0.4, 0.2],
        'avg_quote': [5000, 3000, 4000]
    })
    
    # 创建示例销售员表现指标
    sales_metrics = pd.DataFrame({
        'sales_id': ['S001', 'S002', 'S003'],
        'repair_part': ['卫生间', '厨房', '阳台'],
        'conversion_rate': [0.3, 0.4, 0.2],
        'avg_quote': [5000, 3000, 4000]
    })
    
    # 创建示例报价分析数据，增加sales_id列
    quote_data = pd.DataFrame({
        'quote_amount': [5000, 3000, 4000],
        'final_status': ['成交', '报价未成', '成交'],
        'repair_part': ['卫生间', '厨房', '阳台'],
        'sales_id': ['S001', 'S002', 'S003']
    })
    
    return funnel_metrics, repair_part_metrics, sales_metrics, quote_data

def test_create_funnel_chart(sample_metrics):
    funnel_metrics, _, _, _ = sample_metrics
    fig = Visualizer.create_funnel_chart(funnel_metrics)
    
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 1
    assert fig.layout.title.text == "销售转化漏斗"

def test_create_repair_part_chart(sample_metrics):
    _, repair_part_metrics, _, _ = sample_metrics
    fig = Visualizer.create_repair_part_chart(repair_part_metrics)
    
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 2  # 柱状图和折线图
    assert fig.layout.title.text == "维修部位转化率分析"

def test_create_sales_heatmap(sample_metrics):
    _, _, sales_metrics, _ = sample_metrics
    fig = Visualizer.create_sales_heatmap(sales_metrics)
    
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 1
    assert fig.layout.title.text == "销售员表现热力图"

def test_create_quote_analysis_chart(sample_metrics):
    _, _, _, quote_data = sample_metrics
    fig = Visualizer.create_quote_analysis_chart(quote_data)
    
    assert isinstance(fig, go.Figure)
    # 应有与repair_part种类数相同的trace
    assert len(fig.data) == quote_data['repair_part'].nunique()
    assert fig.layout.title.text == "报价与成交关系分析" 