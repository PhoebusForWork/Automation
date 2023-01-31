import pytest
import allure
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller
import random

td = JsonReader()
testData = td.read_json5('test_validation.json5', file_side='cs')

######################
#  setup & teardown  #
######################

#############
# test_case #
#############


@allure.feature("發送驗證")
@allure.story("發送語音驗證訊息")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('validation_voice'))
def test_validation_voice(test, getCsLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    if test['scenario'] == "[requestType重複]1:註冊" and json_replace['requestType'] == '1':
        json_replace['device'] = json_replace['device']
    elif test['scenario'] == "[requestType]null":
        json_replace['device'] = json_replace['device']
    elif test['scenario'] == "[device]email":
        json_replace['device'] = json_replace['device']
    else:
        json_replace['device'] = str(random.randrange(99999999999))
    print(json_replace)
    api = API_Controller(platfrom='cs')
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getCsLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("發送驗證")
@allure.story("發送短信驗證訊息")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('validation_sms'))
def test_validation_sms(test, getCsLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    if test['scenario'] == "[requestType重複]1:註冊" and json_replace['requestType'] == '1':
        json_replace['device'] = json_replace['device']
    elif test['scenario'] == "[requestType]null":
        json_replace['device'] = json_replace['device']
    elif test['scenario'] == "[device]email":
        json_replace['device'] = json_replace['device']
    else:
        json_replace['device'] = str(random.randrange(99999999999))
    print(json_replace)
    api = API_Controller(platfrom='cs')
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getCsLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("發送驗證")
@allure.story("發送郵箱驗證訊息")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('validation_email'))
def test_validation_email(test, getCsLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    if test['scenario'] == "[requestType重複]1:註冊" and json_replace['requestType'] == '1':
        json_replace['device'] = json_replace['device']
    elif test['scenario'] == "[requestType]null":
        json_replace['device'] = json_replace['device']
    elif test['scenario'] == "[device]number":
        json_replace['device'] = json_replace['device']
    else:
        json_replace['device'] = str(random.randrange(99999))+json_replace['device']
    print(json_replace)
    api = API_Controller(platfrom='cs')
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getCsLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


# @allure.feature("發送驗證") ##尚未串接第三方廠商，case未完成目前只有複製貼上
# @allure.story("取得圖形驗證廠商")
# @allure.title("{test[scenario]}")
# @pytest.mark.parametrize("test", td.get_case('validation_captcha'))
# def test_validation_captcha(test, getCsLoginToken):
#
#     json_replace = td.replace_json(test['json'], test['target'])
#     api = API_Controller(platfrom='cs')
#     resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
#                            test['params'], token=getCsLoginToken)
#     assert resp.status_code == test['code_status'], resp.text
#     assert test['keyword'] in resp.text


