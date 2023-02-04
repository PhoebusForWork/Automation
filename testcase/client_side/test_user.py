import pytest
import allure
import time
import random
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller
from pylib.client_side.user import Address
from pylib.client_side.webApiBase import WEB_API
from pylib.client_side.validation import validation

td = JsonReader()
testData = td.read_json5('test_address.json5', file_side='cs')


######################
#  setup & teardown  #
######################

@pytest.fixture(scope="class")
def clear_address(getCsLoginToken):
    clear = Address()
    clear.clear_user_address(
        web_token=getCsLoginToken)

@pytest.fixture(scope="class")
def re_password_default(getCsLoginToken):

    api = validation()
    code = api.valid_sms(device=13191857262, requestType=3)
    code = code['data']
    reapi = WEB_API()
    reapi.reset_pwd(username="charlie01", telephone=13191857262, newPwd="abc123456", code=code)

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
                delete_id.get_user_address_not_default(web_token=getCsLoginToken)))

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


class Test_user_detail():
    @staticmethod
    @allure.feature("客戶明細資料")
    @allure.story("獲取用戶明細資料")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_user_detail'))
    def test_get_user_detail(test, getCsLoginToken):
        api = WEB_API()
        resp = api.login(username="charlie01")
        admin_token = resp.json()['data']['token']
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'], test['params'], token=admin_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶明細資料")
    @allure.story("修改用戶明細資料")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('put_user_detail'))
    def test_put_user_detail(test, getCsLoginToken):
        api = WEB_API()
        resp = api.login(username="charlie01")
        admin_token = resp.json()['data']['token']
        json_replace = td.replace_json(test['json'], test['target'])
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=admin_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class Test_user_operation():
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("用戶註冊")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('user_register'))
    def test_user_register(test, getCsLoginToken):
        list_value = [130, 131, 132, 133, 134, 135, 136, 137, 138, 139]
        randomname = str(random.choice(list_value))+str(random.randrange(99999999))
        now = time.time()
        api = validation()
        resp = api.valid_sms(device=randomname, requestType=1)
        json_replace = td.replace_json(test['json'], test['target'])

        if test['scenario'] == "一般註冊":
            json_replace['mobile'] = randomname
            json_replace['username'] = json_replace['username'] + str(int(now))
            json_replace['code'] = resp['data']
        if test['scenario'] == "手機號碼格式錯誤":
            code = api.valid_sms(device=12345, requestType=1)
            json_replace['code'] = code['data']
            json_replace['username'] = json_replace['username'] + str(int(now))
        if test['scenario'] == "使用者名稱已經註冊":
            json_replace['mobile'] = randomname
            json_replace['code'] = resp['data']
        print(json_replace)
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=getCsLoginToken)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("用戶登出")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('user_logout'))
    def test_user_logout(test, getCsLoginToken):
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'], test['params'], token=getCsLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("帳戶名登入")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('user_login'))
    def test_user_login(test, getCsLoginToken):
        json_replace = td.replace_json(test['json'], test['target'])
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=getCsLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("手機快捷登入")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('user_loginByMobile'))
    def test_user_loginByMobile(test, getCsLoginToken):
        api = validation()
        list_mobile = [13176543627, 13198560380, 13464647087, 13757723333, 13780721194, 13125561886]
        mobile = str(random.choice(list_mobile))
        code = api.valid_sms(device=mobile, requestType=2)
        json_replace = td.replace_json(test['json'], test['target'])
        if test["scenario"] == "手機快捷登入":
            json_replace["code"] = code['data']
            json_replace["telephone"] = mobile
        print(json_replace)
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=getCsLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("用戶重設密碼")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('user_pwd'))
    def test_user_pwd(test, getCsLoginToken, re_password_default):
        api = validation()
        code = api.valid_sms(device=13191857262, requestType=3)
        json_replace = td.replace_json(test['json'], test['target'])
        if test['scenario'] == '驗證碼錯誤':
            json_replace['code'] = str(123456)
        else:
            json_replace['code'] = code['data']
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=getCsLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("傳送手機驗證碼(通過帳號與手機號重設密碼)")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('user_sendCode'))
    def test_user_sendCode(test, getCsLoginToken):
        json_replace = td.replace_json(test['json'], test['target'])
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=getCsLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    # @staticmethod
    # @allure.feature("用戶操作")
    # @allure.story("用戶心跳")  ###目前不work
    # @allure.title("{test[scenario]}")
    # @pytest.mark.parametrize("test", td.get_case('user_heartbeat'))
    # def test_user_heartbeat(test, getCsLoginToken):
    #     json_replace = td.replace_json(test['json'], test['target'])
    #     api = API_Controller(platfrom='cs')
    #     resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=getCsLoginToken)
    #     assert resp.status_code == test['code_status'], resp.text
    #     assert test['keyword'] in resp.text
