import pytest
import allure
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller

td = JsonReader()
testData = td.read_json5('test_config.json5', file_side='cs')


######################
#  setup & teardown  #
######################

#############
# test_case #
#############


@allure.feature("基本配置")
@allure.story("頭像連結列表")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, json, scenario, target, params, code_status, keyword", td.get_test_case(testData, 'get_config_avatar_urls'))
def test_get_config_avatar_urls(test_case, req_method, req_url, json, scenario, target, params, code_status, keyword, getCsLoginToken):

    # json_replace = td.replace_json(json, target)

    api = API_Controller(platfrom='cs')
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getCsLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyword in resp.text
