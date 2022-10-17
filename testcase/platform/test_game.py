import pytest
import allure
import random
from pylib.platform.game import Game, Rebate_template
from testcase.platform.conftest import getPltLoginToken
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller

td = JsonReader()
testData = td.read_json5('test_game.json5')


######################
#  setup & teardown  #
######################


@pytest.fixture(scope="module")  # 保持指定遊戲開啟
def open_game(getPltLoginToken):
    game = Game()
    game.edit_game_status(platToken=getPltLoginToken,
                          gameCode="AWC_LIVE_SEXY", status=True)

#############
# test_case #
#############


@allure.feature("遊戲管理")
@allure.story("獲取遊戲列表")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'get_game_list'))
def test_get_game_list(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("遊戲管理")
@allure.story("遊戲設置")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, json, scenario, target, params, code_status, keyWord", td.get_test_case(testData, 'edit_game_list'))
def test_edit_game_list(test_case, req_method, req_url, json, scenario, target, params, code_status, keyWord, getPltLoginToken):

    json_replace = td.replace_json(json, target)

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json_replace,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("遊戲管理")
@allure.story("遊戲開啟關閉狀態")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'edit_game_status'))
def test_edit_game_status(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("遊戲管理")
@allure.story("遊戲測試開啟/關閉")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'edit_game_isTesting'))
def test_edit_game_isTesting(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken, open_game):

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("遊戲管理")
@allure.story("同步遊戲數據")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'game_sync'))
def test_game_sync(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken, open_game):

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("遊戲管理")
@allure.story("查詢注單")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, json, scenario, target, params, code_status, keyWord", td.get_test_case(testData, 'get_game_orders'))
def test_get_game_orders(test_case, req_method, req_url, json, scenario, target, params, code_status, keyWord, getPltLoginToken):

    json_replace = td.replace_json(json, target)

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json_replace,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("遊戲管理")
@allure.story("遊戲平台下拉選單")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'get_game_code'))
def test_get_game_code(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("遊戲管理")
@allure.story("取得遊戲平台查詢條件下的下拉選單")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'get_game_channel_mapList'))
def test_get_game_channel_mapList(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("返水模板配置")
@allure.story("獲取返水模板配置")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'get_rebate_template_config'))
def test_get_rebate_template_config(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("返水模板配置")
@allure.story("依遊戲類型分類獲取所有返水模板")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'get_rebate_template_allByGameType'))
def test_get_rebate_template_allByGameType(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("返水模板配置")
@allure.story("新增返水模板")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, json, scenario, target, params, code_status, keyWord", td.get_test_case(testData, 'add_rebate_template_config'))
def test_add_rebate_template_config(test_case, req_method, req_url, json, scenario, target, params, code_status, keyWord, getPltLoginToken):
    json_replace = td.replace_json(json, target)

    if json_replace['templateName'] == "不重複名稱":
        json_replace['templateName'] = json_replace['templateName'] + \
            str(random.randrange(99999))
    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json_replace,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("返水模板配置")
@allure.story("更新返水模板")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, json, req_url, scenario, target, params, code_status, keyWord", td.get_test_case(testData, 'edit_rebate_template_config'))
def test_edit_rebate_template_config(test_case, req_method, json, req_url, scenario, target, params, code_status, keyWord, getPltLoginToken):
    if "存在模板id" in req_url:
        template = Rebate_template()
        req_url = req_url.replace("存在模板id", str(
            template.get_exist_template_auto(platToken=getPltLoginToken)))

    json_replace = td.replace_json(json, target)

    if json_replace['templateName'] == "不重複名稱":
        json_replace['templateName'] = json_replace['templateName'] + \
            str(random.randrange(99999))
    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json_replace,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("返水模板配置")
@allure.story("刪除返水模板")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'delete_rebate_template_config'))
def test_delete_rebate_template_config(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):
    if "存在模板id" in req_url:
        template = Rebate_template()
        req_url = req_url.replace("存在模板id", str(
            template.get_exist_template_auto(platToken=getPltLoginToken)))
    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("遊戲返水配置")
@allure.story("獲取指定遊戲類型反水模板配置")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'get_game_rebate_config'))
def test_get_game_rebate_config(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("遊戲返水配置")
@allure.story("新增/修改遊戲反水配置")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, json, scenario, target, params, code_status, keyWord", td.get_test_case(testData, 'edit_game_rebate_config'))
def test_edit_game_rebate_config(test_case, req_method, req_url, json, scenario, target, params, code_status, keyWord, getPltLoginToken):
    json_replace = td.replace_json(json, target)

    if json_replace[0]['gameCode'] == "不重複名稱":
        json_replace[0]['gameCode'] = json_replace[0]['gameCode'] + \
            str(random.randrange(99999))
    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json_replace,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("遊戲返水配置")
@allure.story("手動結算反水")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'game_rebate_manual_rebate'))
def test_game_rebate_manual_rebate(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("遊戲返水配置")
@allure.story("更新遊戲返水開關")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'game_rebate_config_open'))
def test_game_rebate_config_open(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text
