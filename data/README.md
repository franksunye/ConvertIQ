# 数据说明

## 数据来源
本项目使用防水维修平台的销售数据，包括：
- 线索数据（leads.csv）
- 跟进数据（lead_followup.csv）

## 数据格式
### leads.csv
```csv
lead_id,created_at,region,source_channel,repair_part,customer_id,sales_id
L001,2024-01-01 10:00:00,华东,线上,屋顶,C001,S001
L002,2024-01-01 11:00:00,华南,线下,卫生间,C002,S002
```

### lead_followup.csv
```csv
lead_id,first_contact_time,scheduled_inspection_time,inspection_done_time,quote_amount,quote_time,contract_signed_time,payment_done_time,final_status
L001,2024-01-01 10:30:00,2024-01-02 14:00:00,2024-01-02 15:00:00,5000.00,2024-01-02 16:00:00,2024-01-03 10:00:00,2024-01-03 11:00:00,成交
L002,2024-01-01 11:30:00,2024-01-02 15:00:00,2024-01-02 16:00:00,3000.00,2024-01-02 17:00:00,,,报价未成
```

## 示例数据
- `sample_leads.csv`: 包含100条示例线索数据
- `sample_lead_followup.csv`: 对应的跟进数据

## 数据说明
1. 所有时间字段使用ISO 8601格式
2. 金额字段使用两位小数
3. 状态字段可选值：成交、报价未成、未联系

## 数据更新
- 示例数据每月更新一次
- 实际数据通过API或数据库同步

## 注意事项
- 示例数据已脱敏处理
- 实际使用时需要替换为真实数据
- 数据导入前需要进行格式验证 