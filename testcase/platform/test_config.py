import pytest
import allure
import copy
from datetime import datetime
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller
from pylib.platform.config import Avatar

test_data = TestDataReader()
test_data.read_json5('test_config.json5')


######################
#  setup & teardown  #
######################


#############
# test_case #
#############


@allure.feature("基本配置")
@allure.story("新增頭像")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('add_config_avatar'))
def test_add_config_avatar(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("基本配置")
@allure.story("編輯頭像")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('edit_config_avatar'))
def test_edit_config_avatar(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("基本配置")
@allure.story("刪除頭像")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('delete_config_avatar'))
def test_delete_config_avatar(test, get_platform_token):
    if "存在id" in test['req_url']:
        id = Avatar()
        test['req_url'] = test['req_url'].replace("存在id", str(
            id.get_delete_avatar(plat_token=get_platform_token)))
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("基本配置")
@allure.story("依照條件進行查詢")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_config_avatars'))
def test_get_config_avatars(test, get_platform_token):
    json_replace = test_data.replace_json(test['params'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            json_replace, token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("基本配置")
@allure.story("依頭像id進行查詢")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_config_avatar_one'))
def test_get_config_avatar_one(test, get_platform_token):
    if "存在id" in test['req_url']:
        id = Avatar()
        test['req_url'] = test['req_url'].replace("存在id", str(
            id.get_delete_avatar(plat_token=get_platform_token)))
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("檔案上傳")
@allure.story("上傳圖片")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('file_image_upload'))
def test_file_image_upload(test, get_platform_token):
    if test['files'] == 'null':
        files = None
    else:
        files = [('file', ('upload_image_charliebrown.jpeg',
                           open('resources/upload_file/upload_image_charliebrown.jpeg', 'rb'), 'image/jpeg'))]
    api = API_Controller()
    api.request_session.headers.update({"Content-Type": None})
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token, files=files)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("檔案上傳")
@allure.story("上傳影片")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('file_video_upload'))
def test_file_video_upload(test, get_platform_token):
    if test['files'] == 'null':
        files = None
    else:
        files = [('file', ('upload_video_realshort.mp4',
                           open('resources/upload_file/upload_video_realshort.mp4', 'rb'), 'application/octet-stream'))]
    api = API_Controller()
    api.request_session.headers.update({"Content-Type": None})
    resp = api.send_request(test['req_method'], test['req_url'], test['json'], test['params'],
                            token=get_platform_token, files=files)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("幣別管理")
@allure.story("站點幣別查詢")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_platform_currency'))
def test_get_platform_currency(test, get_platform_token):
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("語系管理")
@allure.story("站點語系查詢")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_platform_language'))
def test_get_platform_language(test, get_platform_token):
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("操作日誌")
@allure.story("查詢後台用戶操作登入日誌")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_admin_action_log'))
def test_get_admin_action_log(test, get_platform_token):
    today = datetime.today().strftime('%Y-%m-%d')
    date_from = today + 'T00:00:00Z'
    date_to = today + 'T23:59:59Z'
    temp = copy.deepcopy(test)
    if test["params"]["to"] == "today_date_to":
        temp["params"].update({"from": date_from, "to": date_to})
    params_replace = test_data.replace_json(temp['params'], temp['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            params_replace, token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("電話區碼管理")
@allure.story("電話區碼查詢")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_country_code_manage'))
def test_get_country_code_manage(test, get_platform_token):
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("電話區碼管理")
@allure.story("修改電話區碼")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('put_country_code_manage'))
def test_put_country_code_manage(test, get_platform_token):
    json_replace = test_data.replace_json_list(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)

