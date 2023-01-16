import pytest
import allure
import jsonpath
from pylib.platform.user import UserVip, User, UserManage
from pylib.platform.proxy import ProxyManage
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller

td = JsonReader()
testData = td.read_json5('test_user.json5')

######################
#  setup & teardown  #
######################

# @pytest.fixture(scope="module", autouse=True)  # 清除代理審核列表
# def clean(getPltLoginToken):

#############
# test_case #
#############


class Test_User_Vip():
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("VIP層級")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_vip_config'))
    def test_get_vip_config(test, getPltLoginToken):
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("VIP層級")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_vip_config_mapList'))
    def test_get_vip_config_mapList(test, getPltLoginToken):
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("VIP層級")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('add_vip_config'))
    def test_add_vip_config(test, getPltLoginToken):
        json_replace = td.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("VIP層級")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('edit_vip_config'))
    def test_edit_vip_config(test, getPltLoginToken):
        vip = UserVip()
        test['req_url'] = test['req_url'].replace("存在vip_id", str(
            vip.get_vip_id_exist(plat_token=getPltLoginToken)))

        json_replace = td.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class Test_User():
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_user_list'))  # 目前噴錯待處理
    def test_get_user_list(test, getPltLoginToken):
        params_replace = td.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               params_replace, token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod  # testcase/platform/test_user.py::Test_User::test_get_user_info -s
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_user_info'))  # 目前噴錯待處理
    def test_get_user_info(test, getPltLoginToken):
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_user_account'))
    def test_get_user_account(test, getPltLoginToken):
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_risk_analysis_same_ip'))
    def test_get_risk_analysis_same_ip(test, getPltLoginToken):
        params_replace = td.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               params_replace, token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_risk_analysis_arbitrage'))
    def test_get_risk_analysis_arbitrage(test, getPltLoginToken):
        params_replace = td.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               params_replace, token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_login_info'))
    def test_get_login_info(test, getPltLoginToken):
        params_replace = td.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               params_replace, token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_user_params'))
    def test_get_user_params(test, getPltLoginToken):
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_user_login_stat'))
    def test_get_user_login_stat(test, getPltLoginToken):
        params_replace = td.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               params_replace, token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('edit_user_remark'))
    def test_edit_user_remark(test, getPltLoginToken):
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('edit_user_reallyName'))
    def test_edit_user_reallyName(test, getPltLoginToken):
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('edit_user_isWhiteList'))
    def test_edit_user_isWhiteList(test, getPltLoginToken):
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('edit_user_convertProxy'))
    def test_edit_user_convertProxy(test, getPltLoginToken):
        user_id = None
        if test['json']['userId'] == 'client_id':
            user = User()
            user_id = user.get_client_user(plat_token=getPltLoginToken)
            test['json']['userId'] = user_id
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        if resp.status_code == 200:
            proxy_manage = ProxyManage()
            proxy_manage.clean_proxy_approval(getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('username_validate'))
    def test_username_validate(test, getPltLoginToken):
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('edit_lockStatus'))
    def test_edit_lockStatus(test, getPltLoginToken):
        json_replace = td.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        if resp.status_code == 200:  # 若成功後去確認鎖定類別並且rej掉內容
            target = UserManage()
            jsdata = target.get_user_manage_list(
                plat_token=getPltLoginToken, size=10, status=0)
            ret = jsonpath.jsonpath(jsdata, "$..id")
            optType = jsonpath.jsonpath(jsdata, "$..optType")
            assert test['keyword'] in optType
            target.first_approval(
                plat_token=getPltLoginToken, id=ret[0], status=2, remark='test_approval')
