# Testing Guide

## Testing Philosophy
我们坚持敏捷和KISS原则，测试以保证数据准确性和可视化正确性为核心。

## Overview
- 重点测试数据处理逻辑、指标计算和可视化展示
- 每个分析模块需有对应的单元测试和集成测试

## Test Types

### Unit Tests
- 数据清洗、指标计算函数的单元测试

### Integration Tests
- 数据流全流程测试（从导入到可视化）

### End-to-End Tests
- 主要流程的端到端测试，确保用户操作无误

## Test Environment
- 推荐使用pytest
- 可用mock数据进行测试

## Running Tests
```bash
pytest
```

## Test Coverage
- 重点覆盖数据处理、指标计算、可视化输出

## Continuous Integration
- 可集成GitHub Actions等自动化测试

## Notes
- 保持测试用例简单明了，覆盖核心业务流程
- 每次迭代需补充新功能的测试 