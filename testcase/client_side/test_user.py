import pytest
import allure
import time
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller
from pylib.client_side.user import Address
from pylib.client_side.validation import Validation
from pylib.client_side.user import Security
from pylib.client_side.test import TransferMock
from utils.generate_utils import Make

test_data = TestDataReader()
test_data.read_json5('test_user.json5', file_side='cs')


######################
#  setup & teardown  #
######################

@pytest.fixture(scope="class")
def clear_address(get_client_side_token):
    clear = Address()
    clear.clear_user_address(
        web_token=get_client_side_token)


@pytest.fixture(scope="class")
def re_password_default():
    validation_api = Validation()
    code = validation_api.valid_sms(mobile=18887827895, requestType=3, countryCode=886)['data']
    uuid = validation_api.valid_account(username='CCuserpwd01', countryCode=886, telephone=18887827895)['data']
    validation_api.reset_pwd(username="CCuserpwd01", uuid=uuid, countryCode=886, telephone=18887827895, newPwd="abc123456", confirmPwd="abc123456", code=code)


@pytest.fixture(scope="class")
def re_mobile_default():

    sms_api = Validation()
    resp_token = sms_api.login(username='changephone01').json()['data']['token']
    get_nm_code = sms_api.valid_sms(device='13847389803', requestType=6)
    get_om_code = sms_api.valid_sms(device='13947389803', requestType=5)
    edit_api = Security(resp_token)
    edit_api.edit_mobile(newMobile=13847389803, nmCode=get_nm_code['data'], omCode=get_om_code['data'])


@pytest.fixture(scope="class")
def re_security_pwd_default():
    validation_api = Validation()
    resp = validation_api.login(username='changepwd01', password="abc12345")
    admin_token = resp.json()['data']['token']
    edit_api = Security(admin_token)
    edit_api.edit_pwd(newPwd="abc123456", oldPwd="abc12345")

@pytest.fixture(scope="class")
def register_check_trigger():
    check_controller = TransferMock()
    check_controller.set_env(False)
    yield
    check_controller.set_env(True)

######################
#      testCase      #
######################

class TestAddress:
    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("新增地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('add_user_address'))
    def test_add_user_address(test, get_client_side_token, clear_address):

        json_replace = test_data.replace_json(test['json'], test['target'])

        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_client_side_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class TestAddressOther:
    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("更新地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_address'))
    def test_edit_user_address(test, get_client_side_token, clear_address):

        json_replace = test_data.replace_json(test['json'], test['target'])

        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_client_side_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("刪除地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('delete_user_address'))
    def test_delete_user_address(test, get_client_side_token):
        if "可刪除id" in test['req_url']:
            delete_id = Address()
            test['req_url'] = test['req_url'].replace("可刪除id", str(
                delete_id.get_user_address_not_default(web_token=get_client_side_token)))

        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("依使用者查詢地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_address'))
    def test_get_user_address(test, get_client_side_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("查詢單筆地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_address_one'))
    def test_get_user_address_one(test, get_client_side_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("省列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_provinces'))
    def test_get_provinces(test, get_client_side_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("省下城市列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_provinces_city'))
    def test_get_provinces_city(test, get_client_side_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class TestUserDetail:
    @staticmethod
    @allure.feature("客戶明細資料")
    @allure.story("獲取用戶明細資料")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_detail'))
    def test_get_user_detail(test, get_client_side_token):
        validation_api = Validation()
        resp = validation_api.login(username="charlie01")
        admin_token = resp.json()['data']['token']
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'], test['params'], token=admin_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶明細資料")
    @allure.story("修改用戶明細資料")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('put_user_detail'))
    def test_put_user_detail(test, get_client_side_token):
        validation_api = Validation()
        resp = validation_api.login(username="charlie01")
        admin_token = resp.json()['data']['token']
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'], token=admin_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


# 用戶操作
class TestUserOperation:
    # 用戶註冊
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("用戶註冊")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('user_register'))
    def test_user_register(test, register_check_trigger):
        json_replace = test_data.replace_json(test['json'], test['target'])
        if json_replace['username'] == "不重複用戶名":
            name_len = 10
            json_replace['username'] = Make.name(name_len)
            print(json_replace['username'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'])
        ResponseVerification.basic_assert(resp, test)

    # 用戶登出
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("用戶登出")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('user_logout'))
    def test_user_logout(test, get_client_side_token):
        validation_api = Validation()
        resp = validation_api.login(username='CCheartbeat01')
        admin_token = resp.json()['data']['token']
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'], test['params'], token=admin_token)
        ResponseVerification.basic_assert(resp, test)

    # 帳戶名登入
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("帳戶名登入")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('user_login'))
    def test_user_login(test):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'])
        ResponseVerification.basic_assert(resp, test)

    # 手機快捷登入
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("手機快捷登入")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('user_login_by_mobile'))
    def test_user_login_by_mobile(test):
        json_replace = test_data.replace_json(test['json'], test['target'])
        if json_replace['code'] == "正確驗證碼":
            api = Validation()
            code = api.valid_sms(mobile=json_replace['telephone'],
                                 countryCode=json_replace['countryCode'],
                                 requestType=2)['data']
            json_replace["code"] = code
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'])
        ResponseVerification.basic_assert(resp, test)

    # 忘記密碼重設(帳號驗證)
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("忘記密碼重設(帳號驗證)")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('user_valid_account'))
    def test_user_valid_account(test):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'])
        ResponseVerification.basic_assert(resp, test)

    # 忘記密碼重設
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("忘記密碼重設")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('user_pwd'))
    def test_user_pwd(test, re_password_default):
        json_replace = test_data.replace_json(test['json'], test['target'])
        if test['scenario'] == '驗證碼錯誤':
            json_replace['code'] = '123456'
        else:
            validation_api = Validation()
            json_replace['code'] = '000000'
            json_replace['uuid'] = validation_api.valid_account(username=json_replace['username'], countryCode=json_replace['countryCode'], telephone=json_replace['telephone'])['data']
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'])
        ResponseVerification.basic_assert(resp, test)

    # 用戶心跳
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("用戶心跳")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('user_heartbeat'))
    def test_user_heartbeat(test, get_client_side_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'], token=get_client_side_token)
        ResponseVerification.basic_assert(resp, test)


class TestUserSecurityCenter:
    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("获取用户安全中心信息")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_info'))
    def test_user_security_info(test, get_client_side_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'], token=get_client_side_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("綁定郵箱地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_email_binding'))
    def test_user_security_email_binding(test):
        validation_api = Validation()
        token_resp = validation_api.login(username='CCemail01')
        admin_token = token_resp.json()['data']['token']
        json_replace = test_data.replace_json(test['json'], test['target'])
        if json_replace['code'] == "值":
            get_email_code = validation_api.valid_email(device='CCemail01@gmail.com', requestType=8)
            json_replace['code'] = get_email_code["data"]
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'], token=admin_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("解綁郵箱地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_email_unbind'))
    def test_user_security_email_unbind(test):
        validation_api = Validation()
        token_resp = validation_api.login(username='CCemail01')
        admin_token = token_resp.json()['data']['token']
        json_replace = test_data.replace_json(test['json'], test['target'])
        if json_replace['code'] == "值":
            get_email_code = validation_api.valid_email(device='CCemail01@gmail.com', requestType=7)
            json_replace['code'] = get_email_code["data"]
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'], token=admin_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("更换手机号码")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_mobile'))
    def test_user_security_mobile(test, re_mobile_default):
        validation_api = Validation()
        json_replace = test_data.replace_json(test['json'], test['target'])
        resp_token = validation_api.login(username='changephone01').json()['data']['token']
        if test['scenario'] == '正常更換手機號碼':
            get_nm_code = validation_api.valid_sms(device=json_replace['newMobile'], requestType=6)
            get_om_code = validation_api.valid_sms(device='13847389803', requestType=5)
            json_replace['nmCode'] = get_nm_code["data"]
            json_replace['omCode'] = get_om_code["data"]
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'], token=resp_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("修改密碼")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_pwd'))
    def test_user_security_pwd(test, re_security_pwd_default):
        validation_api = Validation()
        resp = validation_api.login(username='changepwd01')
        admin_token = resp.json()['data']['token']
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'], token=admin_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text
