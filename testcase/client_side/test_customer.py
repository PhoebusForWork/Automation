import pytest
import allure
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller

test_data = TestDataReader()
test_data.read_json5('test_customer.json5', file_side='cs')


######################
#  setup & teardown  #
######################

#############
# test_case #
#############


@allure.feature("客服管理")
@allure.story("取得客服連結")
@allure.title("{test[scenario]}")
@pytest.mark.regression
@pytest.mark.parametrize("test", test_data.get_case('get_customer_link'))
def test_get_config_avatar_urls(test):

    api = API_Controller(platform='cs')
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'])
    ResponseVerification.basic_assert(resp, test)
