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
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('get_config_avatar_urls'))
def test_get_config_avatar_urls(test, getCsLoginToken):

    api = API_Controller(platfrom='cs')
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['json'], token=getCsLoginToken)

    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text
