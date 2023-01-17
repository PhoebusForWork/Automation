import pytest
import allure
from testcase.platform.conftest import getPltLoginToken
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller
from pylib.platform.config import Avatar

td = JsonReader()
testData = td.read_json5('test_config.json5')


######################
#  setup & teardown  #
######################


#############
# test_case #
#############


@allure.feature("基本配置")
@allure.story("新增頭像")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('add_config_avatar'))
def test_add_config_avatar(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)

    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("基本配置")
@allure.story("編輯頭像")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('edit_config_avatar'))
def test_edit_config_avatar(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)

    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("基本配置")
@allure.story("刪除頭像")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('delete_config_avatar'))
def test_delete_config_avatar(test, getPltLoginToken):
    if "存在id" in test['req_url']:
        id = Avatar()
        test['req_url'] = test['req_url'].replace("存在id", str(
            id.get_delete_avatar(plat_token=getPltLoginToken)))
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)

    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("基本配置")
@allure.story("依照條件進行查詢")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('get_config_avatars'))
def test_get_config_avatars(test, getPltLoginToken):
    json_replace = td.replace_json(test['params'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           json_replace, token=getPltLoginToken)

    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("基本配置")
@allure.story("依頭像id進行查詢")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('get_config_avatar_one'))
def test_get_config_avatar_one(test, getPltLoginToken):
    if "存在id" in test['req_url']:
        id = Avatar()
        test['req_url'] = test['req_url'].replace("存在id", str(
            id.get_delete_avatar(plat_token=getPltLoginToken)))
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)

    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("檔案上傳")
@allure.story("上傳圖片")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('file_image_upload'))
def test_file_image_upload(test, getPltLoginToken):
    if test['files'] == 'null':
        files = None
    else:
        files = [('file', ('upload_image_charliebrown.jpeg',
                           open('resources/upload_file/upload_image_charliebrown.jpeg', 'rb'), 'image/jpeg'))]
    api = API_Controller()
    api.s.headers.update({"Content-Type": None})
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken, files=files)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("檔案上傳")
@allure.story("上傳影片")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('file_video_upload'))
def test_file_video_upload(test, getPltLoginToken):
    if test['files'] == 'null':
        files = None
    else:
        files = [('file', ('upload_video_realshort.mp4',
                           open('resources/upload_file/upload_video_realshort.mp4', 'rb'), 'application/octet-stream'))]
    api = API_Controller()
    api.s.headers.update({"Content-Type": None})
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'], test['params'], token=getPltLoginToken, files=files)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text
