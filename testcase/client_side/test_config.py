import pytest
import allure
from utils.data_utils import TestDataReader
from utils.api_utils import API_Controller

test_data = TestDataReader()
test_data.read_json5('test_config.json5', file_side='cs')


######################
#  setup & teardown  #
######################

#############
# test_case #
#############


@allure.feature("基本配置")
@allure.story("頭像連結列表")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('get_config_avatar_urls'))
def test_get_config_avatar_urls(test, get_client_side_token):

    api = API_Controller(platform='cs')
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['json'], token=get_client_side_token)

    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text
