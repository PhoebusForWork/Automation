import logging
import traceback
import pytest
from pylib.client_side.webApiBase import WEB_API
from utils.data_utils import EnvReader

env = EnvReader()
cs_account = env.CS_ACCOUNT
cs_password = env.CS_PASSWORD
login_user_id = None


@pytest.fixture(scope="module")
def getCsLoginToken(username=cs_account, password=cs_password):
    api = WEB_API()
    resp = api.login(username=username, password=password)
    try:
        token = resp.json()['data']['token']
        global login_user_id
        login_user_id = resp.json()['data']['userId']
    except Exception as ex:
        logging.error('登錄失敗！接口返回:{}'.format(resp.text))
        traceback.print_tb(ex)
    logging.info("登錄成功,token為 : {}".format(token))
    return token


@pytest.fixture(scope="session")
def get_user_id():
    if login_user_id is not None:
        return login_user_id
    else:
        print('---用戶尚未登陸,或取得id失敗---')
        return 0
