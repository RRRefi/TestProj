import pytest
from base.log import Logger

logger = Logger(logger_name='conftest').get_logger()

@pytest.fixture(scope="session", autouse=True)
def init_env():
    logger.info("==== 测试环境初始化完成 ====")
    yield
    logger.info("==== 测试环境清理完成 ====")