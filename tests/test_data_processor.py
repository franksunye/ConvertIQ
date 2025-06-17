import pytest
import pandas as pd
from datetime import datetime
from src.data_processor import DataProcessor

@pytest.fixture
def sample_data():
    # 创建示例数据
    leads_data = {
        'lead_id': ['L001', 'L002', 'L003'],
        'created_at': ['2024-01-01', '2024-01-02', '2024-01-03'],
        'region': ['北京', '上海', '广州'],
        'source_channel': ['线上', '线下', '线上'],
        'repair_part': ['卫生间', '厨房', '阳台'],
        'customer_id': ['C001', 'C002', 'C003'],
        'sales_id': ['S001', 'S002', 'S001']
    }
    
    followup_data = {
        'lead_id': ['L001', 'L002', 'L003'],
        'first_contact_time': ['2024-01-01 10:00', '2024-01-02 11:00', '2024-01-03 09:00'],
        'scheduled_inspection_time': ['2024-01-02 14:00', '2024-01-03 15:00', None],
        'inspection_done_time': ['2024-01-02 15:00', '2024-01-03 16:00', None],
        'quote_amount': [5000.0, 3000.0, None],
        'quote_time': ['2024-01-02 16:00', '2024-01-03 17:00', None],
        'contract_signed_time': ['2024-01-03 10:00', None, None],
        'payment_done_time': ['2024-01-03 11:00', None, None],
        'final_status': ['成交', '报价未成', '未联系']
    }
    
    return pd.DataFrame(leads_data), pd.DataFrame(followup_data)

def test_load_data(sample_data):
    processor = DataProcessor()
    leads_df, followup_df = sample_data
    
    # 测试数据加载
    processor.leads_df = leads_df
    processor.followup_df = followup_df
    
    assert len(processor.leads_df) == 3
    assert len(processor.followup_df) == 3
    assert 'lead_id' in processor.leads_df.columns
    assert 'lead_id' in processor.followup_df.columns

def test_calculate_funnel_metrics(sample_data):
    processor = DataProcessor()
    leads_df, followup_df = sample_data
    processor.leads_df = leads_df
    processor.followup_df = followup_df
    
    metrics = processor.calculate_funnel_metrics()
    
    assert isinstance(metrics, dict)
    assert 'leads_created' in metrics
    assert 'contacted' in metrics
    assert 'inspected' in metrics
    assert 'quoted' in metrics
    assert 'signed' in metrics
    assert 'paid' in metrics

def test_calculate_repair_part_metrics(sample_data):
    processor = DataProcessor()
    leads_df, followup_df = sample_data
    processor.leads_df = leads_df
    processor.followup_df = followup_df
    
    metrics = processor.calculate_repair_part_metrics()
    
    assert isinstance(metrics, pd.DataFrame)
    assert 'repair_part' in metrics.columns
    assert 'conversion_rate' in metrics.columns
    assert 'avg_quote' in metrics.columns

def test_calculate_sales_performance(sample_data):
    processor = DataProcessor()
    leads_df, followup_df = sample_data
    processor.leads_df = leads_df
    processor.followup_df = followup_df
    
    metrics = processor.calculate_sales_performance()
    
    assert isinstance(metrics, pd.DataFrame)
    assert 'sales_id' in metrics.columns
    assert 'conversion_rate' in metrics.columns
    assert 'avg_quote' in metrics.columns

def test_calculate_quote_analysis(sample_data):
    processor = DataProcessor()
    leads_df, followup_df = sample_data
    processor.leads_df = leads_df
    processor.followup_df = followup_df
    
    data = processor.calculate_quote_analysis()
    
    assert isinstance(data, pd.DataFrame)
    assert 'quote_amount' in data.columns
    assert 'final_status' in data.columns 
 