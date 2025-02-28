import pytest
import allure
import jsonpath
from pylib.platform.user import UserVip, User, UserManage , UserVipPointRatio
from pylib.platform.proxy import ProxyManage, Proxy
from utils.data_utils import TestDataReader, ResponseVerification,GetClassData
from utils.api_utils import API_Controller
from utils.generate_utils import Make
from utils.json_verification import validate_json

test_data = TestDataReader()
test_data.read_json5('test_user.json5')

######################
#  setup & teardown  #
######################


@pytest.fixture(scope="class")  #取得VIP設定檔最後一筆資後，跑完TESTCASE需還原資料
def resetVIPConfig(get_platform_token):

    editVip = UserVip(token=get_platform_token).get_vip_id_exist()
    yield editVip['id']
    editVipInputParams = GetClassData.get_function_args(UserVip().edit_vip)
    resetVip = {}

    for arg in editVipInputParams:
        resetVip[arg] = editVip.get(arg)

    reapi = UserVip(token=get_platform_token)
    reapi.edit_vip(**resetVip)


@pytest.fixture(scope="class")  #還原VIP積分設定檔
def resetVipPointRatio(get_platform_token):
    editCNY = UserVipPointRatio(token=get_platform_token).get_vip_point_ratio_cur(currency='CNY')
    yield
    editVipInputParams = GetClassData.get_function_args(UserVipPointRatio().edit_vip_point_ratio)
    resetVipRatio = {}
    for arg in editVipInputParams:
        resetVipRatio[arg] = editCNY.get(arg)

    reapi = UserVipPointRatio(token=get_platform_token)
    reapi.edit_vip_point_ratio(**resetVipRatio)

@pytest.fixture(scope="function")  # 清除用戶審核列表
def clean(get_platform_token):
    yield
    clean = UserManage()
    clean.clean_approval(plat_token=get_platform_token)


#############
# test_case #
#############

# VIP層級
class TestUserVipConfig:
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
    def test_edit_vip_config(test, get_platform_token , resetVIPConfig):

        test['req_url'] = test['req_url'].replace("存在vip_id", str(resetVIPConfig))

        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

# 客戶VIP層級變更紀錄
class TestUserVipLevelRecord:
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶VIP層級變更紀錄")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_vip_level_record'))
    def test_get_vip_level_record(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

# VIP積分
class TestUserVipRatio:
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("VIP積分")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_vip_point_ratio'))
    def test_get_vip_point_ratio(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("VIP積分")
    @allure.title("{test[scenario]}")
    @pytest.mark.not_regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_vip_point_ratio'))
    def test_edit_vip_ratio_config(test, get_platform_token, resetVipPointRatio):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("VIP積分特定幣別修改記錄")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_vip_point_ratio_records'))
    def test_get_vip_ratio_config_records(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("修改VIP積分幣別排序")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('sort_vip_point_ratio'))
    def test_get_vip_ratio_config_records(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

# 客戶列表
class TestUser:
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_list'))
    def test_get_user_list(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod  # testcase/platform/test_user.py::Test_User::test_get_user_info -s
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_info'))
    def test_get_user_info(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_account'))
    def test_get_user_account(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_risk_analysis_same_ip'))
    def test_get_risk_analysis_same_ip(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_risk_analysis_arbitrage'))
    def test_get_risk_analysis_arbitrage(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_login_info'))
    def test_get_login_info(test, get_platform_token):
        start_time=Make.date("start")
        end_time=Make.date("end")
        test['params'].update({'from':start_time, 'to':end_time})
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_params'))
    def test_get_user_params(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 目前被移除
    # @staticmethod
    # @allure.feature("客戶管理")
    # @allure.story("客戶管理")
    # @allure.title("{test[scenario]}")
    # @pytest.mark.regression
    # @pytest.mark.parametrize("test", test_data.get_case('get_user_login_stat'))
    # def test_get_user_login_stat(test, get_platform_token):
    #     params_replace = test_data.replace_json(test['params'], test['target'])
    #     api = API_Controller()
    #     resp = api.send_request(test['req_method'], test['req_url'], test['json'],
    #                             params_replace, token=get_platform_token)
    #     ResponseVerification.basic_assert(resp, test)
    

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_remark'))
    def test_edit_user_remark(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_reallyName'))
    def test_edit_user_reallyName(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_isWhiteList'))
    def test_edit_user_isWhiteList(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_convertProxy'))
    def test_edit_user_convertProxy(test, get_platform_token):
        if test['json']['userId'] == 'client_id':
            user = User(token=get_platform_token)
            user_id = user.get_client_user()
            test['json']['userId'] = user_id
        elif test['json']['userId'] == 'proxy_id':
            user = Proxy(token=get_platform_token)
            user_id = user.get_proxy(queryType=0, input='proxy001')
            user_id = jsonpath.jsonpath(user_id, "$.data.[0].userId")[0]
            test['json']['userId'] = user_id

        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        if resp.status_code == 200:
            proxy_manage = ProxyManage()
            proxy_manage.clean_proxy_approval(get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('username_validate'))
    def test_username_validate(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶管理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
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
            assert validate_json(resp.json(), test['schema'])





# 審批操作
class TestUserManage:
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_query_params'))
    def test_get_query_params(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
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
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
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
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_manage_list'))
    def test_get_user_manage_list(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_manage_log'))
    def test_get_user_manage_log(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_parent'))
    def test_edit_user_parent(test, get_platform_token, clean):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("審批操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_contact'))
    def test_edit_user_contact(test, get_platform_token, clean):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


# 首頁彈窗消息



# 客戶風控管理API
class TestUserRiskLoginLog:
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶風控管理API")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_risk_login_log'))
    def test_get_user_risk_login_log(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


# 客戶標籤
# 客戶地址
class TestUserAddress:
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶地址")
    @allure.title("{test[scenario]}")
    @pytest.mark.xfail(reason='二期')
    @pytest.mark.parametrize("test", test_data.get_case('get_user_address'))
    def test_get_user_address(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


# 客戶VIP層級
class TestUserVip:
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("客戶VIP層級")
    @allure.title("{test[scenario]}")
    # @pytest.mark.regression
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
    # @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_user_vip'))
    def test_edit_user_vip(test, get_platform_token, clean):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


# 站內信管理
# 用戶操作記錄
class TestUserOperation:
    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("用戶操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_operation_log_list'))
    def test_get_user_operation_log_list(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶管理")
    @allure.story("用戶操作")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_operation_log'))
    def test_get_user_operation_log(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)
