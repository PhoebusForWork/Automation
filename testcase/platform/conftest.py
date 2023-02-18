import logging
import traceback
import pytest
from pylib.platform.platApiBase import PLAT_API
from utils.data_utils import EnvReader

"""
如果用例执行前需要先登录获取token值，就要用到conftest.py文件了
作用：conftest.py 配置里可以实现数据共享，不需要import导入 conftest.py，pytest用例会自动查找
scope参数为session，那么所有的测试文件执行前执行一次
scope参数为module，那么每一个测试文件执行前都会执行一次conftest文件中的fixture
scope参数为class，那么每一个测试文件中的测试类执行前都会执行一次conftest文件中的fixture
scope参数为function，那么所有文件的测试用例执行前都会执行一次conftest文件中的fixture
"""

env = EnvReader()


@pytest.fixture(scope="module")
def get_platform_token(username='superAdmin', password='abc123456'):
    api = PLAT_API()
    code = api.imgcode()
    resp = api.login(username=username, password=password, imgCode=code)
    try:
        token = resp.json()['data']['token']
    except Exception as ex:
        logging.error('登錄失敗！接口返回:{}'.format(resp.text))
        traceback.print_tb(ex)
    logging.info("登錄成功,token為 : {}".format(token))
    return token
