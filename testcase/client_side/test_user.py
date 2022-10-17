import pytest
import allure
from utils.data_utils import JsonReader
from utils.api_utils import Cs_API_Controller
from pylib.website.user import Address

td = JsonReader()
testData = td.read_json5('test_address.json5', file_side='cs')


######################
#  setup & teardown  #
######################

@pytest.fixture(scope="class")
def clear_address(getCsLoginToken):
    clear = Address()
    clear.clear_user_address(
        webToken=getCsLoginToken)


######################
#      testCase      #
######################

class Test_address():
    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("新增地址")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, json, scenario, target, params, code_status, keyword", td.get_test_case(testData, 'add_user_address'))
    def test_add_user_address(test_case, req_method, req_url, json, scenario, target, params, code_status, keyword, getCsLoginToken, clear_address):

        json_replace = td.replace_json(json, target)

        api = Cs_API_Controller()
        resp = api.HttpsClient(req_method, req_url, json_replace,
                               params, token=getCsLoginToken)

        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text


class Test_address_other():
    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("更新地址")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, json, scenario, target, params, code_status, keyword", td.get_test_case(testData, 'edit_user_address'))
    def test_edit_user_address(test_case, req_method, req_url, json, scenario, target, params, code_status, keyword, getCsLoginToken, clear_address):

        json_replace = td.replace_json(json, target)

        api = Cs_API_Controller()
        resp = api.HttpsClient(req_method, req_url, json_replace,
                               params, token=getCsLoginToken)

        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("刪除地址")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'delete_user_address'))
    def test_delete_user_address(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getCsLoginToken):
        if "可刪除id" in req_url:
            delete_id = Address()
            req_url = req_url.replace("可刪除id", str(
                delete_id.get_user_address_not_default(webToken=getCsLoginToken)))

        api = Cs_API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getCsLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("依使用者查詢地址")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'get_user_address'))
    def test_get_user_address(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getCsLoginToken):
        api = Cs_API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getCsLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("查詢單筆地址")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'get_user_address_one'))
    def test_get_user_address_one(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getCsLoginToken):
        api = Cs_API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getCsLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("省列表")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'get_provinces'))
    def test_get_provinces(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getCsLoginToken):
        api = Cs_API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getCsLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("省下城市列表")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'get_provinces_city'))
    def test_get_provinces_city(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getCsLoginToken):
        api = Cs_API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getCsLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text
