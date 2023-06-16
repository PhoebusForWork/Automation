import pytest
import allure
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller

test_data = TestDataReader()
test_data.read_json5('test_config.json5', file_side='cs')


######################
#  setup & teardown  #
######################

#############
# test_case #
#############
# 基本配置
class TestConfig():
    # 取得預設可用語系列表(無須登入)
    @staticmethod
    @allure.feature("基本配置")
    @allure.story("取得預設可用語系列表(無須登入)")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_language_list'))
    def test_get_language_list(test):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=None)
        ResponseVerification.basic_assert(resp, test)

    # 取得動態資料 (無須登入)
    @staticmethod
    @allure.feature("基本配置")
    @allure.story("取得動態資料 (無須登入)")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_dynamic_data'))
    def test_get_dynamic_data(test, get_user_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_user_token)

        ResponseVerification.basic_assert(resp, test)

    # 取得預設可用幣別列表(無須登入)
    @staticmethod
    @allure.feature("基本配置")
    @allure.story("取得預設可用幣別列表(無須登入)")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_currency_list'))
    def test_get_currency_list(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)

        ResponseVerification.basic_assert(resp, test)

    # 頭像連結列表
    @staticmethod
    @allure.feature("基本配置")
    @allure.story("頭像連結列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_config_avatar_urls'))
    def test_get_config_avatar_urls(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['json'], token=get_user_token)

        ResponseVerification.basic_assert(resp, test)
