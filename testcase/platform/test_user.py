import pytest
import allure
from testcase.platform.conftest import getPltLoginToken
from pylib.platform.user import UserVip
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
