import pytest
import allure
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller

test_data = TestDataReader()
test_data.read_json5('test_risk.json5')


class TestBlackList:
    @staticmethod
    @allure.feature("黑名單")
    @allure.story("新增黑名單")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('add_black_list'))
    def test_add_black_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("黑名單")
    @allure.story("編輯黑名單")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_black_list'))
    def test_edit_black_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("黑名單")
    @allure.story("黑名單列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_black_list'))
    def test_get_black_list(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)
