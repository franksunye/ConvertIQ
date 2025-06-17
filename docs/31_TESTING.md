# Testing Guide

## Testing Philosophy
我们坚持敏捷和KISS原则，测试以保证数据准确性和可视化正确性为核心。

## Overview
- 重点测试数据处理逻辑、指标计算和可视化展示
- 每个分析模块需有对应的单元测试和集成测试

## Test Types

### Unit Tests
- 数据加载和清洗测试
  - CSV文件导入
  - DataFrame直接传入
  - 时间字段转换
- 指标计算测试
  - 销售漏斗转化率计算
  - 维修部位转化率计算
  - 销售员表现指标计算
  - 报价分析计算
- 可视化测试
  - 漏斗图生成
  - 柱状图和折线图生成
  - 热力图生成
  - 散点图生成

### Integration Tests
- 数据流全流程测试
  - 数据加载到指标计算
  - 指标计算到可视化
  - 界面交互测试

## Test Environment
- 使用pytest框架
- 使用模拟数据进行测试
- 测试数据包含各种场景和边界情况

## Running Tests
```bash
# 运行所有测试
python -m pytest tests/ -v

# 运行特定测试文件
python -m pytest tests/test_data_processor.py -v
python -m pytest tests/test_visualizer.py -v
```

## Test Coverage
- 数据处理函数覆盖率
- 指标计算函数覆盖率
- 可视化函数覆盖率
- 错误处理覆盖率

## Test Data
- 使用模拟数据覆盖各种场景
- 包含正常数据和异常数据
- 数据格式符合实际使用场景

## Continuous Integration
- 可集成GitHub Actions等自动化测试
- 每次提交自动运行测试
- 测试失败阻止合并

## Notes
- 保持测试用例简单明了，覆盖核心业务流程
- 每次迭代需补充新功能的测试
- 定期更新测试数据以覆盖新场景 