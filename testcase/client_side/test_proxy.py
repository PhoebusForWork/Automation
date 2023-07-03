import pytest
import allure
from pylib.platform.proxy import ProxyDomain
from utils.data_utils import TestDataReader, ResponseVerification, EnvReader
from utils.api_utils import API_Controller

env = EnvReader()
test_data = TestDataReader()
test_data.read_json5('test_proxy.json5', file_side='cs')


######################
#  setup & teardown  #
######################

@pytest.fixture(scope="class")
def setup_proxy_domain():
    set_domain = ProxyDomain()
    code = set_domain.imgcode()
    set_domain.login(username="superAdmin", imgCode=code)
    set_domain.edit_proxy_domain(proxyId=1, domain_list={"domain1": "test.com", "domain2": "setting.com"})

#############
# test_case #
#############

# 代理
class TestProxy:
    @staticmethod
    @allure.feature("代理")
    @allure.story("判斷代理域名(判斷當前一級域名是否為代理域名並取得代理推廣碼 無需登入)")
    @allure.title("{test[scenario]}")
    @pytest.mark.usefixtures("setup_proxy_domain")
    @pytest.mark.parametrize("test", test_data.get_case('prase_domain'))
    def test_prase_domain(test, get_user_token):
        api = API_Controller(platform='cs')
        api.request_session.headers.update(test['target'])
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['json'], token=get_user_token)

        ResponseVerification.basic_assert(resp, test)
