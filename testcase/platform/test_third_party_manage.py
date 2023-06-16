import pytest
import allure
import jsonpath

from pylib.platform.thirdPartyManage import ThirdPartyManage
from pylib.platform.config import CountryCodeRelation
from pylib.platform.fund import UserGroup
from pylib.client_side.validation import Validation
from utils.data_utils import TestDataReader, ResponseVerification, EnvReader
from utils.api_utils import API_Controller
from utils.json_verification import validate_json

env = EnvReader()

test_data = TestDataReader()
test_data.read_json5('test_third_party_manage.json5')

######################
#  setup & teardown  #
######################
@pytest.fixture(scope="class")
def check_customer_group(get_platform_token):
    customer = ThirdPartyManage(get_platform_token)
    target = customer.get_customer_group(groupName='客服群組名稱測試')
    ret = jsonpath.jsonpath(target, "$..groupName")
    if ret is False:
        add_user_group = UserGroup(get_platform_token)
        add_user_group.save_group(groupName='客服測試-群組類型測試-客服群組名稱測試')

@pytest.fixture(scope="class")
def make_vaild_code(get_platform_token):
    # 關閉風控開關
    # 開啟後台66(泰國)國碼三方簡訊商
    update_sms = CountryCodeRelation(get_platform_token)
    update_sms.edit_manage(thirdPartyId=8, countryCodeId=6)
    # 前台發送各類型驗證
    valid_build = Validation()
    valid_build.login(username=env.CS_TEST_ACCOUNT)
    valid_build.build_all_valid()
    yield
    # 開啟風控開關

#############
# test_case #
#############
# 用戶驗證碼找回
class TestUserValidCode:
    # 查找用戶驗證碼
    @staticmethod
    @allure.feature("用戶驗證碼找回")
    @allure.story("查找用戶驗證碼")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.usefixtures('make_vaild_code')
    @pytest.mark.parametrize("test", test_data.get_case('get_valid_code'))
    def test_get_valid_code(test, get_platform_token):
        api = API_Controller()
        params_replace = test_data.replace_json(test["params"], test["target"])
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 查找用戶驗證碼類型列表
    @staticmethod
    @allure.feature("用戶驗證碼找回")
    @allure.story("查找用戶驗證碼類型列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_code_type'))
    def test_get_code_type(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


# 三方接口管理
class TestThirdPartyManage:
    # 三方接口:權重更新
    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("三方接口:權重更新")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('update_weighting'))
    def test_update_weighting(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 三方接口:開關更新
    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("三方接口:開關更新")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('update_switched'))
    def test_update_switched(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 客服接口-群組管理-查詢
    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("客服接口-群組管理-查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.usefixtures("check_customer_group")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_customer_group'))
    def test_get_customer_group(test, get_platform_token):
        parmas_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                parmas_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 客服接口-群組管理-保存
    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("客服接口-群組管理-保存")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('save_customer_group'))
    def test_save_customer_group(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 三方接口:查詢
    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("三方接口:查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_third_party_manage'))
    def test_get_third_party_manage(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        # check multi-type
        if "所有資料" in test['scenario']:
            assert set(test['keyword']).issubset(jsonpath.jsonpath(resp.json(), '$..type'))
        else:
            assert test['keyword'] in resp.text
        if resp.status_code == 200:
            assert validate_json(resp.json(), test['schema'])

    # 三方接口:圖形驗證接口-查詢
    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("三方接口:圖形驗證接口-查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_captcha'))
    def test_get_captcha(test, get_platform_token):
        api = API_Controller()
        parmas_replace = test_data.replace_json(test["params"], test["target"])
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                parmas_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 三方接口:銀行卡接口-查詢
    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("三方接口:銀行卡接口-查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_bank_card'))
    def test_get_bank_card(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 客服接口-群組管理-最後更新時間
    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("客服接口-群組管理-最後更新時間")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_customer_group_last_update_time'))
    def test_get_customer_group_last_update_time(test, get_platform_token):
        api = API_Controller()
        parmas_replace = test_data.replace_json(test["params"], test["target"])
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                parmas_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 客服接口-群組管理-群組類型下拉選單
    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("客服接口-群組管理-群組類型下拉選單")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_customer_group_type'))
    def test_get_customer_group_type(test, get_platform_token):
        api = API_Controller()
        params_replace = test_data.replace_json(test["params"], test["target"])
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 客服接口-群組管理-客服下拉選單
    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("客服接口-群組管理-客服下拉選單")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_customer_service'))
    def test_get_customer_service(test, get_platform_token):
        api = API_Controller()
        params_replace = test_data.replace_json(test["params"], test["target"])
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)
