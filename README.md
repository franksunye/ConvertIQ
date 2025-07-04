# ConvertIQ 销售转化率分析系统

## 项目简介
本项目为防水维修平台销售转化率分析系统，帮助企业通过数据分析和可视化，定位销售流程中的瓶颈和改进点。我们坚持敏捷开发和KISS原则，快速交付、持续优化。

## 项目目标
- 分析销售转化率各环节效率，定位问题
- 多维度（销售员、区域、渠道、维修部位）分析
- 可视化展示关键指标，辅助经营决策

## 核心功能
系统提供7个维度的分析模块：

1. **销售转化漏斗**
   - 全层级转化环节显示
   - 漏斗图直观展示各阶段转化情况

2. **维修部位分析**
   - 各部位成交差异分析
   - 转化率和平均报价对比

3. **销售员表现**
   - 销售员整体表现分析
   - 转化率、平均报价、响应时间

4. **报价分析**
   - 报价金额与成交关系
   - 散点图展示相关性

5. **销售员维修部位**
   - 销售员在各维修部位的转化率
   - 热力图直观展示表现差异

6. **销售员排名**
   - 转化率较低者排名
   - 识别需要改进的销售员

7. **部位成交分析**
   - 维修部位成交率 vs 线索占比
   - 发现薄弱环节

## 技术栈
- Python + Pandas：数据处理与分析
- Streamlit + Plotly：可视化前端
- Streamlit Cloud/公司服务器：部署

## 快速开始

### 环境要求
- Python 3.8+
- pip

### 安装步骤
1. 克隆仓库
```bash
git clone https://github.com/franksunye/ConvertIQ.git
cd ConvertIQ
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行应用
```bash
streamlit run app.py
```

### 数据要求
- leads.csv：包含线索基本信息
- lead_followup.csv：包含跟进和成交信息

## 使用说明
1. 在左侧上传数据文件，或使用示例数据
2. 通过不同标签页查看各类分析
3. 点击图表可进行交互（放大、下载等）

## 部署说明

### Streamlit Cloud 部署
1. 访问 [Streamlit Cloud](https://streamlit.io/cloud)
2. 使用 GitHub 账号登录
3. 点击 "New app"
4. 选择本仓库
5. 选择 main 分支
6. 设置主文件路径为 `app.py`
7. 点击 "Deploy"

### 本地部署
1. 确保已安装所有依赖
2. 运行 `streamlit run app.py`
3. 访问 `http://localhost:8501`

## 文档
- [架构设计](docs/10_ARCHITECTURE.md)
- [开发指南](docs/30_DEVELOPMENT.md)
- [测试指南](docs/31_TESTING.md)
- [用户指南](docs/40_USER_GUIDE.md)
- [变更日志](docs/01_CHANGELOG.md)

## 贡献
欢迎通过issue或PR提出建议和改进。

## 许可证
[待定]

## 联系方式
[待定] 