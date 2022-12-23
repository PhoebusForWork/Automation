import pytest
import allure
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller
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
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('add_user_address'))
    def test_add_user_address(test, getCsLoginToken, clear_address):

        json_replace = td.replace_json(test['json'], test['target'])

        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                               test['params'], token=getCsLoginToken)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class Test_address_other():
    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("更新地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('edit_user_address'))
    def test_edit_user_address(test, getCsLoginToken, clear_address):

        json_replace = td.replace_json(test['json'], test['target'])

        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                               test['params'], token=getCsLoginToken)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("刪除地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('delete_user_address'))
    def test_delete_user_address(test, getCsLoginToken):
        if "可刪除id" in test['req_url']:
            delete_id = Address()
            test['req_url'] = test['req_url'].replace("可刪除id", str(
                delete_id.get_user_address_not_default(webToken=getCsLoginToken)))

        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getCsLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("依使用者查詢地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_user_address'))
    def test_get_user_address(test, getCsLoginToken):
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getCsLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("查詢單筆地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_user_address_one'))
    def test_get_user_address_one(test, getCsLoginToken):
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getCsLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("省列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_provinces'))
    def test_get_provinces(test, getCsLoginToken):
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getCsLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("省下城市列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_provinces_city'))
    def test_get_provinces_city(test, getCsLoginToken):
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getCsLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text
