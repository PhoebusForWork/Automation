import pytest
import allure
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
