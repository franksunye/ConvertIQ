import os
import sys
import pytest

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 创建必要的目录
@pytest.fixture(autouse=True)
def setup_test_environment():
    # 确保src目录存在
    os.makedirs('src', exist_ok=True)
    
    # 确保data目录存在
    os.makedirs('data', exist_ok=True)
    
    # 确保tests目录存在
    os.makedirs('tests', exist_ok=True)
    
    yield
    
    # 测试后的清理工作（如果需要）
    pass 