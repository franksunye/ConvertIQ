# Architecture Overview

## Development Philosophy
我们坚持敏捷开发和KISS原则，架构设计以简单、可扩展、易维护为目标，优先满足业务分析需求，后续根据反馈持续优化。

## System Design
- 数据驱动的分析与可视化系统
- 前端采用 Streamlit，后端以 Python + Pandas/SQL 处理数据
- 支持本地和云端部署

## Data Model
### leads
| 字段 | 类型 | 含义 |
|---|---|---|
| lead_id | string | 唯一线索ID |
| created_at | datetime | 创建时间 |
| region | string | 区域 |
| source_channel | string | 渠道 |
| repair_part | string | 维修部位 |
| customer_id | string | 客户ID |
| sales_id | string | 销售ID |

### lead_followup
| 字段 | 类型 | 含义 |
|---|---|---|
| lead_id | string | FK |
| first_contact_time | datetime | 首次联系时间 |
| scheduled_inspection_time | datetime | 约诊时间 |
| inspection_done_time | datetime | 约诊完成时间 |
| quote_amount | float | 报价金额 |
| quote_time | datetime | 报价时间 |
| contract_signed_time | datetime | 签约时间 |
| payment_done_time | datetime | 付款时间 |
| final_status | string | 状态（成交/报价未成/未联系）|

## Analysis Workflow
1. 数据导入与清洗
   - 支持CSV文件导入或DataFrame直接传入
   - 自动转换时间字段为datetime类型
2. 指标计算
   - 销售漏斗转化率
   - 维修部位转化率与平均报价
   - 销售员表现（转化率、平均报价、响应时间）
   - 报价与成交关系分析
   - 销售员在各维修部位的转化率
   - 销售员转化率排名
   - 维修部位成交率与线索占比
3. 多维度分析
   - 销售员维度
   - 区域维度
   - 渠道维度
   - 维修部位维度
4. 可视化展示与交互
   - 漏斗图展示转化流程
   - 柱状图+折线图展示维修部位分析
   - 热力图展示销售员表现
   - 散点图展示报价与成交关系
   - 热力图展示销售员在各维修部位的转化率
   - 条形图展示销售员转化率排名
   - 双轴图展示维修部位成交率与线索占比

## Visualization Modules
- 销售转化漏斗（漏斗图）
- 各部位成交差异（柱状图+折线图）
- 报价金额 vs 成交（散点图）
- 销售员表现分布（热力图）
- 销售员在各维修部位的转化率（热力图）
- 销售员转化率排名（条形图）
- 维修部位成交率与线索占比（双轴图）

## Technology Stack
- Python + Pandas：数据处理与分析
- Streamlit + Plotly：前端可视化
- Streamlit Cloud/公司服务器：部署

## Security & Performance
- 仅处理业务所需数据，避免冗余
- 保持架构简洁，便于维护和扩展

## Notes
- 架构会根据实际需求持续优化
- 所有设计优先考虑简单和可扩展 