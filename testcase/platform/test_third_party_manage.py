import pytest
import allure
import jsonpath

from pylib.platform.thirdPartyManage import thirdPartyManage
from utils.data_utils import TestDataReader
from utils.api_utils import API_Controller

test_data = TestDataReader()
test_data.read_json5('test_third_party_manage.json5')

######################
#  setup & teardown  #
######################


#############
# test_case #
#############


class TestThirdPartyManage:
    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("獲取三方接口列表")
    @allure.title("{test[scenario]}")
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

    @staticmethod
    @allure.feature("三方接口管理")
    @allure.story("保存三方接口列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", test_data.get_case('edit_third_party_manage'))
    def test_edit_third_party_manage(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        # check response
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text
        # query and check data after editing
        if resp.status_code == 200:
            id = str(json_replace[0]['id'])
            req = jsonpath.jsonpath(thirdPartyManage().getThirdInterface(plat_token=get_platform_token),
                                    f'$.data[?(@.id == {id} )]')
            if req is not False:
                assert set(test['target'].items()).issubset(req[0].items())