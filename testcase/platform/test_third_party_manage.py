import pytest
import allure
import jsonpath

from pylib.platform.thirdPartyManage import thirdPartyManage
from testcase.platform.conftest import getPltLoginToken
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller

td = JsonReader()
testData = td.read_json5('test_third_party_manage.json5')

######################
#  setup & teardown  #
######################



#############
# test_case #
#############

class Test_Thrid_Party_Manage():
    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("獲取三方接口列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('get_third_party_manage'))
    def test_get_third_party_manage(test, getPltLoginToken):
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        # check multi-type
        if "所有資料" in test['scenario']:
            assert set(test['keyword']).issubset(jsonpath.jsonpath(resp.json(), '$..type'))
        else:
            assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("保存三方接口列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('edit_third_party_manage'))
    def test_edit_third_party_manage(test, getPltLoginToken):
        json_replace = td.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                               test['params'], token=getPltLoginToken)
        # check response
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text
        # query and check data after editing
        if resp.status_code == 200:
            id = str(json_replace[0]['id'])
            req = jsonpath.jsonpath(thirdPartyManage().getThirdInterface(plat_token=getPltLoginToken),
                                    f'$.data[?(@.id == {id} )]')
            if req is not False:
               assert set(test['target'].items()).issubset(req[0].items())
