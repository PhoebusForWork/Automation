import logging
import traceback
import pytest
import configparser
from pylib.website.webApiBase import WEB_API

config = configparser.ConfigParser()
config.read('config/config.ini')
cs_account = config['cs_account']['account']
cs_password = config['cs_account']['password']


@pytest.fixture(scope="session")
def getCsLoginToken(username=cs_account, password=cs_password):
    api = WEB_API()
    resp = api.Login(username=username, password=password)
    try:
        token = resp.json()['data']['token']
    except Exception as ex:
        logging.error('登錄失敗！接口返回:{}'.format(resp.text))
        traceback.print_tb(ex)
    logging.info("登錄成功,token為 : {}".format(token))
    return token
