import pytest
import allure
import time
from utils.data_utils import TestDataReader
from utils.api_utils import API_Controller
from pylib.client_side.user import Address
from pylib.client_side.validation import validation
from pylib.client_side.user import Security
from utils.generate_utils import Make

test_data = TestDataReader()
test_data.read_json5('test_address.json5', file_side='cs')


######################
#  setup & teardown  #
######################

@pytest.fixture(scope="class")
def clear_address(get_client_side_token):
    clear = Address()
    clear.clear_user_address(
        web_token=get_client_side_token)


@pytest.fixture(scope="function")
def re_password_default():
    validation_api = validation()
    code = validation_api.valid_sms(device=18887827895, requestType=3)['data']
    validation_api.reset_pwd(username="CCuserpwd01", telephone=18887827895, newPwd="abc123456", code=code)


@pytest.fixture(scope="class")
def re_mobile_default():

    sms_api = validation()
    resp_token = sms_api.login(username='changephone01').json()['data']['token']
    get_nm_code = sms_api.valid_sms(device='13847389803', requestType=6)
    get_om_code = sms_api.valid_sms(device='13947389803', requestType=5)
    edit_api = Security(resp_token)
    edit_api.editMobile(newMobile=13847389803, nmCode=get_nm_code['data'], omCode=get_om_code['data'])

@pytest.fixture(scope="class")
def re_security_pwd_default():
    validation_api = validation()
    resp = validation_api.login(username='changepwd01', password="abc12345")
    admin_token = resp.json()['data']['token']
    edit_api = Security(admin_token)
    edit_api.editPwd(newPwd="abc123456", oldPwd="abc12345")

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

        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
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

        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
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

        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("依使用者查詢地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_address'))
    def test_get_user_address(test, get_client_side_token):
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("查詢單筆地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_address_one'))
    def test_get_user_address_one(test, get_client_side_token):
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("省列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_provinces'))
    def test_get_provinces(test, get_client_side_token):
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("省下城市列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_provinces_city'))
    def test_get_provinces_city(test, get_client_side_token):
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class Test_user_detail():
    @staticmethod
    @allure.feature("客戶明細資料")
    @allure.story("獲取用戶明細資料")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_detail'))
    def test_get_user_detail(test, getCsLoginToken):
        validation_api = validation()
        resp = validation_api.login(username="charlie01")
        admin_token = resp.json()['data']['token']
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'], test['params'], token=admin_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶明細資料")
    @allure.story("修改用戶明細資料")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('put_user_detail'))
    def test_put_user_detail(test, getCsLoginToken):
        validation_api = validation()
        resp = validation_api.login(username="charlie01")
        admin_token = resp.json()['data']['token']
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=admin_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class Test_user_operation():
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("用戶註冊")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_register'))
    def test_user_register(test):
        # list_value = [130, 131, 132, 133, 134, 135, 136, 137, 138, 139]
        # random_mobile = str(random.choice(list_value))+str(random.randrange(11111111, 99999999))
        make_mobile = Make()
        register_mobile = make_mobile.mobile()
        now = time.time()
        api = validation()
        resp = api.valid_sms(device=register_mobile, requestType=1)
        json_replace = test_data.replace_json(test['json'], test['target'])

        if test['scenario'] == "一般註冊":
            json_replace['mobile'] = register_mobile
            json_replace['username'] = json_replace['username'] + str(int(now))
            json_replace['code'] = resp['data']
        if test['scenario'] == "手機號碼格式錯誤":
            code = api.valid_sms(device=12345, requestType=1)
            json_replace['code'] = code['data']
            json_replace['username'] = json_replace['username'] + str(int(now))
        if test['scenario'] == "使用者名稱已經註冊":
            json_replace['mobile'] = register_mobile
            json_replace['code'] = resp['data']
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'])

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("用戶登出")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_logout'))
    def test_user_logout(test, getCsLoginToken):
        validation_api = validation()
        resp = validation_api.login(username='CCheartbeat01')
        admin_token = resp.json()['data']['token']
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'], test['params'], token=admin_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("帳戶名登入")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_login'))
    def test_user_login(test):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'])
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("手機快捷登入")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_login_by_mobile'))
    def test_user_login_by_mobile(test):
        json_replace = test_data.replace_json(test['json'], test['target'])
        if test["scenario"] == "手機快捷登入":
            api = validation()
            code = api.valid_sms(device=json_replace['telephone'], requestType=2)
            json_replace["code"] = code['data']
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'])
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("用戶重設密碼")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_pwd'))
    def test_user_pwd(test, re_password_default):
        json_replace = test_data.replace_json(test['json'], test['target'])
        if test['scenario'] == '驗證碼錯誤':
            json_replace['code'] = '123456'
        else:
            validation_api = validation()
            code = validation_api.valid_sms(device=json_replace['telephone'], requestType=3)
            json_replace['code'] = code['data']
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'])
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("傳送手機驗證碼(通過帳號與手機號重設密碼)")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_send_code'))
    def test_user_send_code(test):
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'], test['params'])
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("用戶心跳")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_heartbeat'))
    def test_user_heartbeat(test, getCsLoginToken):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=getCsLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class Test_user_security_center():
    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("获取用户安全中心信息")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_info'))
    def test_user_security_info(test, getCsLoginToken):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=getCsLoginToken)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("綁定郵箱地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_email_binding'))
    def test_user_security_email_binding(test):
        validation_api = validation()
        token_resp = validation_api.login(username='CCemail01')
        admin_token = token_resp.json()['data']['token']
        json_replace = test_data.replace_json(test['json'], test['target'])
        if json_replace['code'] == "值":
            get_email_code = validation_api.valid_email(device='CCemail01@gmail.com', requestType=8)
            json_replace['code'] = get_email_code["data"]
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=admin_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("解綁郵箱地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_email_unbind'))
    def test_user_security_email_unbind(test):
        validation_api = validation()
        token_resp = validation_api.login(username='CCemail01')
        admin_token = token_resp.json()['data']['token']
        json_replace = test_data.replace_json(test['json'], test['target'])
        if json_replace['code'] == "值":
            get_email_code = validation_api.valid_email(device='CCemail01@gmail.com', requestType=7)
            json_replace['code'] = get_email_code["data"]
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=admin_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("更换手机号码")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_mobile'))
    def test_user_security_mobile(test, re_mobile_default):
        validation_api = validation()
        json_replace = test_data.replace_json(test['json'], test['target'])
        resp_token = validation_api.login(username='changephone01').json()['data']['token']
        if test['scenario'] == '正常更換手機號碼':
            get_nm_code = validation_api.valid_sms(device=json_replace['newMobile'], requestType=6)
            get_om_code = validation_api.valid_sms(device='13847389803', requestType=5)
            json_replace['nmCode'] = get_nm_code["data"]
            json_replace['omCode'] = get_om_code["data"]
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=resp_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("修改密碼")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_pwd'))
    def test_user_security_pwd(test, re_security_pwd_default):
        validation_api = validation()
        resp = validation_api.login(username='changepwd01')
        admin_token = resp.json()['data']['token']
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace, test['params'], token=admin_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


