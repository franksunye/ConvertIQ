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
tab1, tab2, tab3, tab4 = st.tabs([
    "转化漏斗", "维修部位分析", "销售员表现", "报价分析"
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

# 页脚
st.markdown("---")
st.markdown("### 使用说明")
st.markdown("""
1. 在左侧上传数据文件，或使用示例数据
2. 通过不同标签页查看各类分析
3. 点击图表可进行交互（放大、下载等）
""") 