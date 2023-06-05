import logging
import traceback
import pytest
from pylib.client_side.webApiBase import WebAPI
from utils.data_utils import EnvReader

env = EnvReader()
cs_account = env.CS_TEST_ACCOUNT
cs_password = env.CS_TEST_PASSWORD

@pytest.fixture(scope="module")
def get_client_side_token(username=cs_account, password=cs_password):
    api = WebAPI()
    resp = api.login(username=username, password=password)
    try:
        token = resp.json()['data']['token']
        global login_user_id
        login_user_id = resp.json()['data']['userId']
        print(login_user_id)
    except Exception as ex:
        logging.error('登錄失敗！接口返回:{}'.format(resp.text))
        traceback.print_tb(ex)
    logging.info("登錄成功,token為 : {}".format(token))
    return token, login_user_id

@pytest.fixture(scope="module")
def get_user_token(get_client_side_token):
    token, _ = get_client_side_token
    if token is not None:
        return token
    else:
        print('---用戶尚未登陸，或取得id失敗---')
        return 0

@pytest.fixture(scope="module")
def get_user_id(get_client_side_token):
    _, user_id = get_client_side_token
    if user_id is not None:
        return user_id
    else:
        print('---用戶尚未登陸，或取得id失敗---')
        return 0
