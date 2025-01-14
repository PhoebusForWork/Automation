import pytest
import allure
from pylib.client_side.webApiBase import WebAPI
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller
from pylib.client_side.user import Address, Vip
from pylib.client_side.validation import Validation
from pylib.client_side.user import Security
from pylib.platform.config import CountryCodeRelation
from utils.generate_utils import Make
from ..platform.conftest import get_platform_token

test_data = TestDataReader()
test_data.read_json5('test_user.json5', file_side='cs')


######################
#  setup & teardown  #
######################

@pytest.fixture(scope="class")
def clear_address(get_user_token):
    clear = Address()
    clear.clear_user_address(
        web_token=get_user_token)


@pytest.fixture()
def re_password_default(request, test):
    if request.param_index == 0:
        validation_api = Validation()
        target = request.getfixturevalue("test")
        mobile = target['json']['telephone']
        username = target['json']['username']
        countryCode = target['json']['countryCode']
        password = "abc123456"
        code = validation_api.valid_sms(mobile=mobile, requestType=3, countryCode=countryCode)['data']
        uuid = validation_api.valid_account(username=username, countryCode=countryCode, telephone=mobile)['data']
        validation_api.reset_pwd(username=username, uuid=uuid, countryCode=countryCode, telephone=mobile, newPwd=password, confirmPwd=password, code=code)


@pytest.fixture(scope="class")
def re_mobile_default():
    yield
    sms_api = Validation()
    resp_token = sms_api.login(username='generic003').json()['data']['token']
    edit_api = Security(resp_token)
    edit_api.edit_mobile(newMobileCountryCode=86, newMobile=18198933333, nmCode="000000",
                         omCode="000000")


@pytest.fixture(scope="class")
def re_security_pwd_default():
    yield
    validation_api = Validation()
    resp = validation_api.login(username='generic004', password="abc12345")
    admin_token = resp.json()['data']['token']
    edit_api = Security(admin_token)
    edit_api.edit_pwd(newPwd="abc123456", oldPwd="abc12345")


@pytest.fixture(scope="class")
def make_register_new_user():
    register_new_user = WebAPI()
    name_len = 10
    new_name = Make.name(name_len)
    print(new_name)
    deviceId = Make.mobile()
    pwd = 'abc123456'
    resp = register_new_user.user_register(
        deviceId=deviceId,
        username=new_name,
        password=pwd,
        confirmPassword=pwd,
        captchaValidation={"channelName": "string", "imgToken": "000000"})
    token = resp['data']['token']
    return token

@pytest.fixture(scope='class')
def set_country_code_relation(get_platform_token):
    api = CountryCodeRelation(token=get_platform_token)
    api.edit_manage(item=[{"thirdPartyId":8,"countryCodeId":6},{"thirdPartyId":8,"countryCodeId":5}])


@pytest.fixture(scope="class")
def vip_register_new_user():

    user_list = [f"VI{Make.format_date(format='%y%m%d%H%M')}{str(i).zfill(2)}" for i in range(12)]
    for user in user_list:
        pwd = 'abc123456'
        api = Validation()
        api.user_register(deviceId=Make.mobile(), username=user,
                          password=pwd, confirmPassword=pwd)

    return user_list

######################
#      testCase      #
######################


class TestVIP:
    @staticmethod
    @allure.feature("VIP")
    @allure.story("各VIP階層與幣別積分比例")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_vip_config'))
    def test_get_user_vip_config(test, get_user_token):

        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("VIP")
    @allure.story("用戶VIP查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_vip'))
    def test_get_user_vip(test, get_user_token):

        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("VIP")
    @allure.story("用戶VIP未領點卷")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_vip_coupons'))
    def test_get_user_vip_coupons(test, get_user_token):

        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("VIP")
    @allure.story("用戶VIP點卷詳情")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_vip_coupon_records'))
    def test_get_user_vip_coupon_records(test, get_user_token):

        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("VIP")
    @allure.story("用戶VIP點卷可兌換詳情")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_vip_coupon_exchange'))
    def test_get_user_vip_coupon_exchange(test, get_user_token):

        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("VIP")
    @allure.story("VIP升降邏輯")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_vip_level'))
    def test_get_user_vip_level(test, register_check_trigger, vip_register_new_user):

        account = vip_register_new_user
        user_name = account[test['params']['username']]
        user_vip = Vip()
        token = user_vip.login(username=user_name).json()['data']['token']
        org_user_vip = user_vip.get_vip()

        # 設定USER資料->調整JSON->將JSON資料帶入MONGO調整->run xxl-job
        user_vip.run_vip_process(token=token, test=test, user_name=user_name)

        # 取得USER VIP資訊,確認1.VIP等級2.升級点券數量3.升级点券金額
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], {},
                                test['params'], token=token)

        # 1.VIP等級(一次升多等)
        assert resp.status_code == test['code_status'], resp.text
        assert (test['params']['vipName'] if test['keyword'] == "vipName" else test['keyword']) in resp.text

        # 2.升級点券數量
        user_vip_id, user_vip_name = resp.json()['data']['vipId'], resp.json()['data']['vipName']
        user_coupons, available_coupons = user_vip.get_coupon_data(
            test=test,
            type_id=test['params']['type'],
            org_user_vip=org_user_vip["data"]["vipId"],
            user_vip_id=user_vip_id,
            user_vip_name=user_vip_name
        )
        assert len(user_coupons) == len(available_coupons)

        # 3.升级点券金額(升多等，需補派各等級之點券)
        user_coupon_points = set(int(coupon['point']) for coupon in user_coupons)
        available_coupon_points = set(int(coupon['point']) for coupon in available_coupons)
        assert available_coupon_points.issubset(user_coupon_points)

        # 4.兌換點卷(含幣別轉換)
        actual_balance, estimate_balance = user_vip.get_coupon_exchange_bonus(token, test, available_coupons)
        assert actual_balance == estimate_balance

        # 動態產生測試資訊於報表
        allure.dynamic.description(
            f"User: {user_name}\n"
            f"JSON: {str(test['json'])}\n"
            f"Result: 1.VIP等級: {user_vip_name} \n"
            f"2.升級点券數量 user_coupons: {len(user_coupons)} , available_coupons: {len(available_coupons)},\n"
            f"3.升级点券金額 \n"
            f"User coupon points: {user_coupon_points}\n"
            f"Available coupon points: {available_coupon_points},\n"
            f"4.兑换彩金確認 estimate-user_balances :{estimate_balance} ,actual-user_balances {actual_balance} \n"
        )


class TestAddress:
    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("新增地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.xfail(reason="確定一期不處理，二期到時再看著辦")
    @pytest.mark.parametrize("test", test_data.get_case('add_user_address'))
    def test_add_user_address(test, get_user_token, clear_address):

        json_replace = test_data.replace_json(test['json'], test['target'])

        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_user_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class TestAddressOther:
    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("更新地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.xfail(reason="確定一期不處理，二期到時再看著辦")
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_address'))
    def test_edit_user_address(test, get_user_token, clear_address):

        json_replace = test_data.replace_json(test['json'], test['target'])

        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_user_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("刪除地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.xfail(reason="確定一期不處理，二期到時再看著辦")
    @pytest.mark.parametrize("test", test_data.get_case('delete_user_address'))
    def test_delete_user_address(test, get_user_token):
        if "可刪除id" in test['req_url']:
            delete_id = Address()
            test['req_url'] = test['req_url'].replace("可刪除id", str(
                delete_id.get_user_address_not_default(web_token=get_user_token)))

        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("依使用者查詢地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.xfail(reason="確定一期不處理，二期到時再看著辦")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_address'))
    def test_get_user_address(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("查詢單筆地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.xfail(reason="確定一期不處理，二期到時再看著辦")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_address_one'))
    def test_get_user_address_one(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("省列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.xfail(reason="確定一期不處理，二期到時再看著辦")
    @pytest.mark.parametrize("test", test_data.get_case('get_provinces'))
    def test_get_provinces(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("用戶送貨地址")
    @allure.story("省下城市列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.xfail(reason="確定一期不處理，二期到時再看著辦")
    @pytest.mark.parametrize("test", test_data.get_case('get_provinces_city'))
    def test_get_provinces_city(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class TestUserDetail:
    @staticmethod
    @allure.feature("客戶明細資料")
    @allure.story("獲取用戶明細資料")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_detail'))
    def test_get_user_detail(test, register_check_trigger):
        validation_api = Validation()
        resp = validation_api.login(username="generic003")
        admin_token = resp.json()['data']['token']
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'], test['params'], token=admin_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶明細資料")
    @allure.story("修改用戶明細資料")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('put_user_detail'))
    @pytest.mark.regression
    def test_put_user_detail(test):
        validation_api = Validation()
        resp = validation_api.login(username="generic001")
        token = resp.json()['data']['token']
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'], test['params'], token=token)
        ResponseVerification.basic_assert(resp, test)


# 用戶操作
class TestUserOperation:
    # 用戶註冊
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("用戶註冊")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
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
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('user_logout'))
    def test_user_logout(test):
        validation_api = Validation()
        resp = validation_api.login(username=test["login_user"])
        admin_token = resp.json()['data']['token']
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'], test['params'], token=admin_token)
        ResponseVerification.basic_assert(resp, test)

    # 帳戶名登入
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("帳戶名登入")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.usefixtures('register_check_trigger')
    @pytest.mark.parametrize("test", test_data.get_case('user_login'))
    def test_user_login(test, register_check_trigger):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'])
        ResponseVerification.basic_assert(resp, test)

    # 手機快捷登入
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("手機快捷登入")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test # 還缺設置手機號
    @pytest.mark.usefixtures('register_check_trigger')
    @pytest.mark.parametrize("test", test_data.get_case('user_login_by_mobile'))
    def test_user_login_by_mobile(test, register_check_trigger):
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
    # @pytest.mark.test 還缺設置手機號
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
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('user_pwd'))
    def test_user_pwd(test, set_country_code_relation, re_password_default):
        json_replace = test_data.replace_json(test['json'], test['target'])
        if test['scenario'] == '驗證碼錯誤':
            json_replace['code'] = '123456'
        else:
            validation_api = Validation()
            json_replace['code'] = '000000'
            json_replace['uuid'] = validation_api.valid_account(
                username=json_replace['username'], countryCode=json_replace['countryCode'],
                telephone=json_replace['telephone'])['data']
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'])
        ResponseVerification.basic_assert(resp, test)

    # 用戶心跳
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("用戶心跳")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('user_heartbeat'))
    def test_user_heartbeat(test, get_user_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    # 取得用戶資訊
    @staticmethod
    @allure.feature("用戶操作")
    @allure.story("取得用戶資訊")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_info'))
    def test_get_user_info(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'], test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)


class TestUserSecurityCenter:
    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("提款短信驗證開關")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_withdrawProtect'))
    @pytest.mark.regression
    def test_user_security_withdraw_protect(test, get_user_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'],
                                json_replace, test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    # 已廢棄
    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("获取用户安全中心信息")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_info'))
    def test_user_security_info(test, get_user_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'],
                                token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("綁定郵箱地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.xfail(reason="目前拔掉此需求")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_email_binding'))
    @pytest.mark.regression
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
    @pytest.mark.xfail(reason="目前拔掉此需求")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_email_unbind'))
    @pytest.mark.regression
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
    @allure.story("是否綁定手機號碼")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_security_mobile'))
    @pytest.mark.regression
    def test_get_user_security_mobile(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("綁定手機號碼")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('put_user_security_mobile_binding'))
    @pytest.mark.regression
    def test_put_user_security_mobile_binding(test, register_check_trigger, make_register_new_user):
        json_replace = test_data.replace_json(test['json'], test['target'])
        register_new_user_token = make_register_new_user
        if json_replace['mobile'] == "綁定號碼":
            new_mobile = Make.mobile()
            json_replace['mobile'] = new_mobile
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=register_new_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("更换手机号码")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('put_user_security_mobile'))
    @pytest.mark.regression
    def test_put_user_security_mobile(test, re_mobile_default):
        validation_api = Validation()
        resp_token = validation_api.login(username='generic003').json()['data']['token']
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'], token=resp_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("用戶安全中心")
    @allure.story("修改密碼")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_security_pwd'))
    @pytest.mark.regression
    def test_user_security_pwd(test, re_security_pwd_default):
        validation_api = Validation()
        resp = validation_api.login(username='generic004')
        admin_token = resp.json()['data']['token']
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'], token=admin_token)
        ResponseVerification.basic_assert(resp, test)


class TestUserLanguageAndCurrency:
    @staticmethod
    @allure.feature("用戶語系與幣種")
    @allure.story("選擇語系")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_language'))
    @pytest.mark.regression
    def test_user_language(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'],
                                test['json'], test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("用戶語系與幣種")
    @allure.story("選擇幣別")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_currency'))
    @pytest.mark.regression
    def test_user_currency(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'],
                                test['json'], test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)
