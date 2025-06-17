# Development Guide

## Development Philosophy
我们坚持敏捷开发和KISS原则，优先实现核心分析和可视化功能，快速迭代，持续优化。

## Getting Started

### Prerequisites
- Python 3.8+
- 推荐使用虚拟环境（venv/conda）
- 依赖：pandas, streamlit, plotly 等

### Installation
```bash
pip install -r requirements.txt
```

### Development Environment Setup
- 推荐使用 VSCode/PyCharm
- 本地运行：`streamlit run app.py`

## Development Workflow
- 以数据表和指标为核心，先实现数据处理和指标计算
- 每个分析模块独立开发，优先可视化展示
- 每次迭代交付可用的分析页面，收集反馈再优化
- 代码和文档保持同步更新

### 数据处理模块
- `DataProcessor` 类负责数据加载和指标计算
- 支持CSV文件或DataFrame直接传入
- 自动处理时间字段转换
- 提供漏斗、维修部位、销售员、报价等分析功能

### 可视化模块
- `Visualizer` 类负责图表生成
- 使用Plotly创建交互式图表
- 支持漏斗图、柱状图、折线图、热力图、散点图等
- 统一的样式和布局设置

### 主程序
- 使用Streamlit构建Web界面
- 支持文件上传和示例数据
- 分标签页展示各类分析
- 提供详细数据表格展示

### Branching Strategy
- main：稳定主分支
- feature/xxx：新功能开发

### Code Style
- 遵循PEP8
- 保持函数和模块简洁
- 添加类型注解
- 编写单元测试

### Commit Guidelines
- 以功能/修复为单位提交
- 提交信息清晰描述变更

## Testing
- 使用pytest进行单元测试
- 测试覆盖数据处理和可视化功能
- 使用模拟数据进行测试
- 运行测试：`python -m pytest tests/ -v`

## Deployment
- 支持 Streamlit Cloud 或公司内部服务器
- 确保依赖版本一致
- 配置文件权限和访问控制

## Notes
- 数据和代码分离，便于维护
- 以业务价值为导向，优先交付最有用的分析功能
- 保持代码简洁，避免过度设计
- 定期进行代码审查和重构
- This document will be updated as development processes evolve
- New developers should review this document before starting work
- We maintain simple, clear processes to avoid complexity
- Regular retrospectives help us improve our development practices 