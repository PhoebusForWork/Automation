import pytest
import allure
import time
from pylib.platform.platApiBase import PLAT_API
from pylib.platform.account import AccountAdmin, AccountDept, AccountRole
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller
from utils.generate_utils import Make

td = JsonReader()
testData = td.read_json5('test_file_upload.json5')

#############
# test_case #
#############


@allure.feature("檔案上傳")
@allure.story("上傳圖片")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('file_image_upload'))
def test_file_image_upload(test, getPltLoginToken):
    files = [('file', ('charliebrown.jpeg',
                open('/Users/charliechan/Downloads/charliebrown.jpeg', 'rb'), 'image/jpeg'))]
    json_replace = td.replace_json(test['json'], test['target'])
    if test['scenario'] == "上傳圖片":
        json_replace['filers'] = files
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


# @allure.feature("檔案上傳")
# @allure.story("上傳影片")
# @allure.title("{test[scenario]}")
# @pytest.mark.parametrize("test", td.get_case('file_video_upload'))
# def test_file_video_upload(test, getPltLoginToken):
#     now = time.time()
#     json_replace = td.replace_json(test['json'], test['target'])
#     if test["scenario"] == "[id]不存在":
#         json_replace['id'] = str(int(now))
#     api = API_Controller()
#     resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
#                            test['params'], token=getPltLoginToken)
#     assert resp.status_code == test['code_status'], resp.text
#     assert test['keyword'] in resp.text

