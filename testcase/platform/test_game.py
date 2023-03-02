import pytest
import allure
import random
from datetime import datetime
from utils.data_utils import TestDataReader, ResponseVerification
from pylib.platform.game import Game, RebateTemplate
from utils.data_utils import TestDataReader
from utils.api_utils import API_Controller
from pylib.platform.game import GameRecover

test_data = TestDataReader()
test_data.read_json5('test_game.json5')


######################
#  setup & teardown  #
######################


@pytest.fixture(scope="module")  # 保持指定遊戲開啟
def open_game(get_platform_token):
    game = Game()
    game.edit_game_status(plat_token=get_platform_token,
                          game_code="AI_SPORT_AI", status=True, currency="CNY")


@pytest.fixture()
def clear_game_recover_first_change(get_platform_token, request):
    def clear_first():
        clear_game_recover = GameRecover()
        manage_id = clear_game_recover.find_recover_manage_id(plat_token=get_platform_token)
        if manage_id is not False:
            clear_game_recover.post_game_recover_first(
                plat_token=get_platform_token,
                recoverManageId=manage_id,
                isApprove=False)
    request.addfinalizer(clear_first)


@pytest.fixture(scope="module")
def clear_game_recover_first(get_platform_token):
    clear_game_recover = GameRecover()
    manage_id = clear_game_recover.find_recover_manage_id(plat_token=get_platform_token)
    if manage_id is not False:
        clear_game_recover.post_game_recover_first(
            plat_token=get_platform_token,
            recoverManageId=manage_id,
            isApprove=False)


@pytest.fixture()
def clear_game_recover_second(get_platform_token, request):
    def clear_second():
        clear_game_recover = GameRecover()
        manage_id = clear_game_recover.find_recover_manage_id(plat_token=get_platform_token, status=1)
        if manage_id is not False:
            clear_game_recover.post_game_recover_second(
                plat_token=get_platform_token,
                recoverManageId=manage_id,
                isApprove=False)
    request.addfinalizer(clear_second)


#############
# test_case #
#############


@allure.feature("遊戲管理")
@allure.story("獲取遊戲列表")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_game_list'))
def test_get_game_list(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲管理")
@allure.story("遊戲設置")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('edit_game_list'))
def test_edit_game_list(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲管理")
@allure.story("遊戲開啟關閉狀態")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('edit_game_status'))
def test_edit_game_status(test, get_platform_token):
    params_replace = test_data.replace_json(test['params'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            params_replace, token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲管理")
@allure.story("遊戲測試開啟/關閉")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('edit_game_is_testing'))
def test_edit_game_is_testing(test, get_platform_token, open_game):
    params_replace = test_data.replace_json(test['params'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            params_replace, token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲管理")
@allure.story("同步遊戲數據")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('game_sync'))
def test_game_sync(test, get_platform_token, open_game):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲管理")
@allure.story("查詢注單")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('get_game_orders'))
def test_get_game_orders(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲管理")
@allure.story("遊戲平台下拉選單")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_game_code'))
def test_get_game_code(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲管理")
@allure.story("遊戲語言下拉選單")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_game_languages'))
def test_get_game_languages(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲管理")
@allure.story("遊戲幣別下拉選單")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_game_currencies'))
def test_get_game_currencies(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲管理")
@allure.story("取得遊戲平台查詢條件下的下拉選單")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_game_channel_map_list'))
def test_get_game_channel_map_list(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("返水模板配置")
@allure.story("獲取返水模板配置")  # API可能會調整，待釐清
@allure.title("{test[scenario]}")
# @pytest.mark.regression API可能會調整，待釐清
@pytest.mark.xfail()
@pytest.mark.parametrize("test", test_data.get_case('get_rebate_template_config'))
def test_get_rebate_template_config(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("返水模板配置")
@allure.story("依遊戲類型分類獲取所有返水模板")  # API可能會調整，待釐清
@allure.title("{test[scenario]}")
# @pytest.mark.regression API可能會調整，待釐清
@pytest.mark.xfail()
@pytest.mark.parametrize("test", test_data.get_case('get_rebate_template_all_by_game_type'))
def test_get_rebate_template_all_by_game_type(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("返水模板配置")
@allure.story("新增返水模板")  # API可能會調整，待釐清
@allure.title("{test[scenario]}")
# @pytest.mark.regression API可能會調整，待釐清
@pytest.mark.parametrize("test", test_data.get_case('add_rebate_template_config'))
def test_add_rebate_template_config(test, get_platform_token):
    json_replace = test_data.replace_json(test['json'], test['target'])

    if json_replace['templateName'] == "不重複名稱":
        json_replace['templateName'] = json_replace['templateName'] + \
            str(random.randrange(99999))
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("返水模板配置")
@allure.story("更新返水模板")  # API可能會調整，待釐清
@allure.title("{test[scenario]}")
# @pytest.mark.regression API可能會調整，待釐清
@pytest.mark.parametrize("test", test_data.get_case('edit_rebate_template_config'))
def test_edit_rebate_template_config(test, get_platform_token):
    if "存在模板id" in test['req_url']:
        template = RebateTemplate()
        test['req_url'] = test['req_url'].replace("存在模板id", str(
            template.get_exist_template_auto(plat_token=get_platform_token)))

    json_replace = test_data.replace_json(test['json'], test['target'])

    if json_replace['templateName'] == "不重複名稱":
        json_replace['templateName'] = json_replace['templateName'] + \
            str(random.randrange(99999))
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("返水模板配置")
@allure.story("刪除返水模板")  # API可能會調整，待釐清
@allure.title("{test[scenario]}")
# @pytest.mark.regression API可能會調整，待釐清
@pytest.mark.parametrize("test", test_data.get_case('delete_rebate_template_config'))
def test_delete_rebate_template_config(test, get_platform_token):
    if "存在模板id" in test['req_url']:
        template = RebateTemplate()
        test['req_url'] = test['req_url'].replace("存在模板id", str(
            template.get_exist_template_auto(plat_token=get_platform_token)))
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲返水配置")
@allure.story("新增/修改遊戲反水配置")  # API可能會調整，待釐清
@allure.title("{test[scenario]}")
# @pytest.mark.regression API可能會調整，待釐清
@pytest.mark.parametrize("test", test_data.get_case('edit_game_rebate_config'))
def test_edit_game_rebate_config(test, get_platform_token):
    json_replace = test_data.replace_json(test['json'], test['target'])
    if json_replace[0]['gameCode'] == "不重複名稱":
        json_replace[0]['gameCode'] = json_replace[0]['gameCode'] + \
            str(random.randrange(99999))
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲返水配置")
@allure.story("獲取指定遊戲類型反水模板配置")  # API可能會調整，待釐清
@allure.title("{test[scenario]}")
# @pytest.mark.regression API可能會調整，待釐清
@pytest.mark.parametrize("test", test_data.get_case('get_game_rebate_config'))
def test_get_game_rebate_config(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲返水配置")
@allure.story("手動結算反水")  # API可能會調整，待釐清
@allure.title("{test[scenario]}")
# @pytest.mark.regression API可能會調整，待釐清
@pytest.mark.parametrize("test", test_data.get_case('game_rebate_manual_rebate'))
def test_game_rebate_manual_rebate(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("遊戲返水配置")
@allure.story("更新遊戲返水開關")  # API可能會調整，待釐清
@allure.title("{test[scenario]}")
# @pytest.mark.regression API可能會調整，待釐清
@pytest.mark.parametrize("test", test_data.get_case('game_rebate_config_open'))
def test_game_rebate_config_open(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("返水紀錄")
@allure.story("獲取返水紀錄")  # API可能會調整，待釐清
@allure.title("{test[scenario]}")
# @pytest.mark.regression 需要反水的資料，目前尚未製造反水資料
@pytest.mark.xfail()
@pytest.mark.parametrize("test", test_data.get_case('rebate_record'))
def test_rebate_record(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("平台派彩")
@allure.story("平台派彩")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_game_payout'))
def test_get_game_payout(test, get_platform_token):
    params_replace = test_data.replace_json(test['params'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            params_replace, token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("資金歸集審核管理")
@allure.story("資金歸集審核列表")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('get_game_recover'))
def test_get_game_recover(test, get_platform_token, clear_game_recover_first_change, clear_game_recover_second):
    params_replace = test_data.replace_json(test['params'], test['target'])
    today = datetime.today().strftime('%Y-%m-%d')
    date_from = today + 'T00:00:00Z'
    date_to = today + 'T23:59:59Z'
    if params_replace['status'] == "status_case0":
        params_replace = {'from': date_from, 'to': date_to, 'status': 0}
        get_recover_manage = GameRecover()
        get_recover_manage.post_game_recover(plat_token=get_platform_token)
    elif params_replace['status'] == "status_case1":
        params_replace = {'from': date_from, 'to': date_to, 'status': 1}
        get_recover_manage = GameRecover()
        get_recover_manage.post_game_recover(plat_token=get_platform_token)
        manage_id = get_recover_manage.find_recover_manage_id(plat_token=get_platform_token, status=0)
        get_recover_manage.post_game_recover_first(
            plat_token=get_platform_token,
            recoverManageId=manage_id,
            isApprove=True)
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'], params_replace, token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("資金歸集審核管理")
@allure.story("一鍵歸集")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('post_game_recover'))
def test_post_game_recover(test, get_platform_token, clear_game_recover_first):
    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("資金歸集審核管理")
@allure.story("資金歸集一審")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('post_game_recover_first'))
def test_post_game_recover_first(test, get_platform_token, clear_game_recover_second):
    json_replace = test_data.replace_json(test['json'], test['target'])
    if json_replace['recoverManageId'] == "true_false_case":
        get_recover_manage = GameRecover()
        get_recover_manage.post_game_recover(plat_token=get_platform_token)
        manage_id = get_recover_manage.find_recover_manage_id(plat_token=get_platform_token, status=0)
        json_replace['recoverManageId'] = manage_id
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("資金歸集審核管理")
@allure.story("資金歸集二審")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('post_game_recover_second'))
def test_post_game_recover_second(test, get_platform_token,):
    json_replace = test_data.replace_json(test['json'], test['target'])
    if json_replace['recoverManageId'] == "true_false_case":
        get_recover_manage = GameRecover()
        get_recover_manage.post_game_recover(plat_token=get_platform_token)
        manage_id = get_recover_manage.find_recover_manage_id(plat_token=get_platform_token, status=0)
        get_recover_manage.post_game_recover_first(
            plat_token=get_platform_token,
            recoverManageId=manage_id,
            isApprove=True)
        json_replace['recoverManageId'] = manage_id
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)
