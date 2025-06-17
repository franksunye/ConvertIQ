import streamlit as st
import pandas as pd
from src.data_processor import DataProcessor
from src.visualizer import Visualizer

# 设置页面配置
st.set_page_config(
    page_title="销售转化率分析系统",
    page_icon="📈",
    layout="wide"
)

# 初始化数据处理器和可视化器
@st.cache_resource
def init_processor():
    return DataProcessor()

processor = init_processor()
visualizer = Visualizer()

# 侧边栏 - 数据上传
st.sidebar.title("数据上传")
leads_file = st.sidebar.file_uploader("上传线索数据 (CSV)", type=['csv'])
followup_file = st.sidebar.file_uploader("上传跟进数据 (CSV)", type=['csv'])

# 如果没有上传文件，使用示例数据
if leads_file is None or followup_file is None:
    st.sidebar.info("使用示例数据进行演示")
    processor.load_data("data/sample_leads.csv", "data/sample_lead_followup.csv")
else:
    processor.load_data(leads_file, followup_file)

# 主页面标题
st.title("📈 防水维修平台销售转化率分析系统")

# 创建标签页
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "转化漏斗", "维修部位分析", "销售员表现", "报价分析", 
    "销售员维修部位", "销售员排名", "部位成交分析"
])

# 标签页1：转化漏斗
with tab1:
    st.header("销售转化漏斗分析")
    metrics = processor.calculate_funnel_metrics()
    fig = visualizer.create_funnel_chart(metrics)
    st.plotly_chart(fig, use_container_width=True)

# 标签页2：维修部位分析
with tab2:
    st.header("维修部位转化分析")
    metrics = processor.calculate_repair_part_metrics()
    fig = visualizer.create_repair_part_chart(metrics)
    st.plotly_chart(fig, use_container_width=True)
    
    # 显示详细数据
    st.subheader("详细数据")
    st.dataframe(metrics)

# 标签页3：销售员表现
with tab3:
    st.header("销售员表现分析")
    metrics = processor.calculate_sales_performance()
    fig = visualizer.create_sales_heatmap(metrics)
    st.plotly_chart(fig, use_container_width=True)
    
    # 显示详细数据
    st.subheader("详细数据")
    st.dataframe(metrics)

# 标签页4：报价分析
with tab4:
    st.header("报价与成交关系分析")
    data = processor.calculate_quote_analysis()
    fig = visualizer.create_quote_analysis_chart(data)
    st.plotly_chart(fig, use_container_width=True)
    
    # 显示详细数据
    st.subheader("详细数据")
    st.dataframe(data)

# 标签页5：销售员维修部位
with tab5:
    st.header("销售员在各维修部位的转化率")
    data = processor.calculate_quote_analysis()
    fig = visualizer.create_sales_repair_heatmap(data)
    st.plotly_chart(fig, use_container_width=True)
    
    # 显示详细数据
    st.subheader("详细数据")
    st.dataframe(data.pivot_table(
        index='sales_id',
        columns='repair_part',
        values='final_status',
        aggfunc=lambda x: (x == '成交').mean()
    ).round(3))

# 标签页6：销售员排名
with tab6:
    st.header("销售员转化率排名")
    data = processor.calculate_quote_analysis()
    fig = visualizer.create_sales_ranking(data)
    st.plotly_chart(fig, use_container_width=True)
    
    # 显示详细数据
    st.subheader("详细数据")
    ranking_data = data.groupby('sales_id').agg({
        'final_status': lambda x: (x == '成交').mean(),
        'lead_id': 'count'
    }).rename(columns={
        'final_status': '转化率',
        'lead_id': '线索数'
    }).sort_values('转化率')
    st.dataframe(ranking_data.style.format({'转化率': '{:.1%}'}))

# 标签页7：部位成交分析
with tab7:
    st.header("维修部位成交率与线索占比分析")
    data = processor.calculate_quote_analysis()
    fig = visualizer.create_repair_part_ratio(data)
    st.plotly_chart(fig, use_container_width=True)
    
    # 显示详细数据
    st.subheader("详细数据")
    ratio_data = data.groupby('repair_part').agg({
        'lead_id': 'count',
        'final_status': lambda x: (x == '成交').sum()
    }).rename(columns={
        'lead_id': '线索数',
        'final_status': '成交数'
    })
    ratio_data['线索占比'] = ratio_data['线索数'] / ratio_data['线索数'].sum()
    ratio_data['转化率'] = ratio_data['成交数'] / ratio_data['线索数']
    st.dataframe(ratio_data.style.format({
        '线索占比': '{:.1%}',
        '转化率': '{:.1%}'
    }))

# 页脚
st.markdown("---")
st.markdown("### 使用说明")
st.markdown("""
1. 在左侧上传数据文件，或使用示例数据
2. 通过不同标签页查看各类分析
3. 点击图表可进行交互（放大、下载等）
""") 