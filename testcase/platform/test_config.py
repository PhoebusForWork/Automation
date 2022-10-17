import pytest
import allure
from testcase.platform.conftest import getPltLoginToken
from utils.data_utils import Utils
from utils.api_utils import API_Controller
from pylib.platform.config import Avatar

td = Utils()
testData = td.read_json5('test_config.json5')


######################
#  setup & teardown  #
######################


#############
# test_case #
#############


@allure.feature("基本配置")
@allure.story("新增頭像")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, json, scenario, target, params, code_status, keyWord", td.get_test_case(testData, 'add_config_avatar'))
def test_add_config_avatar(test_case, req_method, req_url, json, scenario, target, params, code_status, keyWord, getPltLoginToken):

    json_replace = td.replace_json(json, target)

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json_replace,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("基本配置")
@allure.story("編輯頭像")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, json, req_url, scenario, target, params, code_status, keyWord", td.get_test_case(testData, 'edit_config_avatar'))
def test_edit_config_avatar(test_case, req_method, json, req_url, scenario, target, params, code_status, keyWord, getPltLoginToken):

    json_replace = td.replace_json(json, target)

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json_replace,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("基本配置")
@allure.story("刪除頭像")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, json, req_url, scenario, target, params, code_status, keyWord", td.get_test_case(testData, 'delete_config_avatar'))
def test_delete_config_avatar(test_case, req_method, json, req_url, scenario, target, params, code_status, keyWord, getPltLoginToken):
    if "存在id" in req_url:
        id = Avatar()
        req_url = req_url.replace("存在id", str(
            id.get_delete_avatar(platToken=getPltLoginToken)))
    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("基本配置")
@allure.story("依照條件進行查詢")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, params, req_url, scenario, target, json, code_status, keyWord", td.get_test_case(testData, 'get_config_avatars'))
def test_get_config_avatars(test_case, req_method, params, req_url, scenario, target, json, code_status, keyWord, getPltLoginToken):
    json_replace = td.replace_json(params, target)
    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           json_replace, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("基本配置")
@allure.story("依頭像id進行查詢")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, json, req_url, scenario, target, params, code_status, keyWord", td.get_test_case(testData, 'get_config_avatar_one'))
def test_get_config_avatar_one(test_case, req_method, json, req_url, scenario, target, params, code_status, keyWord, getPltLoginToken):
    if "存在id" in req_url:
        id = Avatar()
        req_url = req_url.replace("存在id", str(
            id.get_delete_avatar(platToken=getPltLoginToken)))
    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text
