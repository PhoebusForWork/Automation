import pytest
import allure
import time
from pylib.platform.platApiBase import PLAT_API
from pylib.platform.account import AccountAdmin, AccountDept, AccountRole
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller
from utils.generate_utils import Make

td = JsonReader()
testData = td.read_json5('test_universal.json5')

#############
# test_case #
#############


@allure.feature("基本配置")
@allure.story("新增頭像")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('add_config_avatar'))
def add_config_avatar(test, getPltLoginToken):
    now = time.time()
    json_replace = td.replace_json(test['json'], test['target'])
    if test['scenario'] == "新增頭像":
        json_replace['title'] = json_replace['title'] + str(int(now))
        json_replace['url'] = json_replace['url'] + str(int(now))
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("基本配置")
@allure.story("修改頭像")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('edit_config_avatar'))
def edit_config_avatar(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text