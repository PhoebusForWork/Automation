import pytest
import allure
import jsonpath
from pylib.platform.user import UserVip, User, UserManage
from pylib.platform.proxy import ProxyManage
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller

test_data = TestDataReader()
test_data.read_json5('test_user.json5')

######################
#  setup & teardown  #
######################


@pytest.fixture(scope="function")  # 清除用戶審核列表
def clean(get_platform_token):
    yield
    clean = UserManage()
    clean.clean_approval(plat_token=get_platform_token)
#############
# test_case #
#############


class TestUserVipConfig:
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("VIP層級")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('add_vip_config'))
    def test_add_vip_config(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("VIP層級")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_vip_config'))
    def test_get_vip_config(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("VIP層級")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_vip_config_mapList'))
    def test_get_vip_config_mapList(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("VIP層級")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_vip_config'))
    def test_edit_vip_config(test, get_platform_token):
        vip = UserVip()
        test['req_url'] = test['req_url'].replace("存在vip_id", str(vip.get_vip_id_exist(plat_token=get_platform_token)))

        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


class TestUser:
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_list'))
    def test_get_user_list(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod  # testcase/platform/test_user.py::Test_User::test_get_user_info -s
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_info'))
    def test_get_user_info(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_account'))
    def test_get_user_account(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_risk_analysis_same_ip'))
    def test_get_risk_analysis_same_ip(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_risk_analysis_arbitrage'))
    def test_get_risk_analysis_arbitrage(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_login_info'))
    def test_get_login_info(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_params'))
    def test_get_user_params(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_login_stat'))
    def test_get_user_login_stat(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_remark'))
    def test_edit_user_remark(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_reallyName'))
    def test_edit_user_reallyName(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_isWhiteList'))
    def test_edit_user_isWhiteList(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_convertProxy'))
    def test_edit_user_convertProxy(test, get_platform_token):
        if test['json']['userId'] == 'client_id':
            user = User()
            user_id = user.get_client_user(plat_token=get_platform_token)
            test['json']['userId'] = user_id
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        if resp.status_code == 200:
            proxy_manage = ProxyManage()
            proxy_manage.clean_proxy_approval(get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('username_validate'))
    def test_username_validate(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('edit_lockStatus'))
    def test_edit_lockStatus(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        if resp.status_code == 200:  # 若成功後去確認鎖定類別並且rej掉內容
            target = UserManage()
            jsdata = target.get_user_manage_list(
                plat_token=get_platform_token, size=10, status=0)
            ret = jsonpath.jsonpath(jsdata, "$..id")
            optType = jsonpath.jsonpath(jsdata, "$..optType")
            assert test['keyword'] in optType
            target.first_approval(
                plat_token=get_platform_token, id=ret[0], status=2, remark='test_approval')


class TestUserManage:
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_manage_list'))
    def test_get_user_manage_list(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_query_params'))
    def test_get_query_params(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('get_user_manage_log'))
    def test_get_user_manage_log(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_manage_first_approval'))
    def test_user_manage_first_approval(test, get_platform_token, clean):
        if "{id}" in test['req_url']:
            manage = UserManage()
            manage_id = manage.get_manage_id(
                plat_token=get_platform_token, phase=1)
            test['req_url'] = test['req_url'].replace("{id}", str(manage_id))
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('user_manage_second_approval'))
    def test_user_manage_second_approval(test, get_platform_token, clean):
        if "{id}" in test['req_url']:
            manage = UserManage()
            manage_id = manage.get_manage_id(
                plat_token=get_platform_token, phase=2)
            test['req_url'] = test['req_url'].replace("{id}", str(manage_id))
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_parent'))
    def test_edit_user_parent(test, get_platform_token, clean):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_contact'))
    def test_edit_user_contact(test, get_platform_token, clean):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class TestUserVip:
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶VIP層級")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_vip'))
    def test_get_user_vip(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶VIP層級")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_vip'))
    def test_edit_user_vip(test, get_platform_token, clean):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)
