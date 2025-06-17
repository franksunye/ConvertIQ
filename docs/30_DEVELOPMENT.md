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

### Branching Strategy
- main：稳定主分支
- feature/xxx：新功能开发

### Code Style
- 遵循PEP8
- 保持函数和模块简洁

### Commit Guidelines
- 以功能/修复为单位提交

## Build Process
- Streamlit 自动热更新，无需复杂构建

## Deployment
- 支持 Streamlit Cloud 或公司内部服务器

## Notes
- 数据和代码分离，便于维护
- 以业务价值为导向，优先交付最有用的分析功能
- This document will be updated as development processes evolve
- New developers should review this document before starting work
- We maintain simple, clear processes to avoid complexity
- Regular retrospectives help us improve our development practices 