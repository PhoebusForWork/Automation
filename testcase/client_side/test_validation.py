import pytest
import allure
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller
from utils.generate_utils import Make
import random

test_data = TestDataReader()
test_data.read_json5('test_validation.json5', file_side='cs')

######################
#  setup & teardown  #
######################

#############
# test_case #
#############


@allure.feature("發送驗證")
@allure.story("發送語音驗證訊息")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('validation_voice'))
def test_validation_voice(test, get_user_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    if json_replace['mobile'] == "隨機手機":
        json_replace['mobile'] = Make.mobile()
    api = API_Controller(platform='cs')
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_user_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("發送驗證")
@allure.story("發送短信驗證訊息")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('validation_sms'))
def test_validation_sms(test, get_user_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    if json_replace['mobile'] == "隨機手機":
        json_replace['mobile'] = Make.mobile()
    api = API_Controller(platform='cs')
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_user_token)
    ResponseVerification.basic_assert(resp, test)


# @allure.feature("發送驗證")
# @allure.story("發送郵箱驗證訊息")
# @allure.title("{test[scenario]}")
# @pytest.mark.parametrize("test", test_data.get_case('validation_email'))
# def test_validation_email(test, get_user_token):

#     json_replace = test_data.replace_json(test['json'], test['target'])
#     if json_replace['device'] == '@gmail.com':
#         json_replace['device'] = str(random.randrange(99999)) + json_replace['device']
#     api = API_Controller(platform='cs')
#     resp = api.send_request(test['req_method'], test['req_url'], json_replace,
#                             test['params'], token=get_user_token)
#     assert resp.status_code == test['code_status'], resp.text
#     assert test['keyword'] in resp.text


@allure.feature("發送驗證")
@allure.story("檢查發送語音訊息規則")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('voice_check'))
def test_voice_check(test, get_user_token):
    params_replace = test_data.replace_json(test['params'], test['target'])
    api = API_Controller(platform='cs')
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            params_replace, token=get_user_token)
    ResponseVerification.basic_assert(resp, test)

@allure.feature("發送驗證")
@allure.story("取得圖形驗證廠商")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('validation_captcha'))
def test_validation_captcha(test, get_user_token):

    api = API_Controller(platform='cs')
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_user_token)
    ResponseVerification.basic_assert(resp, test)
