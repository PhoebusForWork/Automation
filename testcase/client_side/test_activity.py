import pytest
import allure
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller
from pylib.platform.activity import ActivityManagement
from pylib.platform.platApiBase import PlatformAPI

test_data = TestDataReader()
test_data.read_json5('test_activity.json5', file_side='cs')


######################
#  setup & teardown  #
######################
@pytest.fixture(scope="class")
def get_activity_id():
    api = PlatformAPI()
    code = api.imgcode()
    resp = api.login(username='superAdmin', password='abc123456', imgCode=code)
    token = resp.json()['data']['token']
    activity_id = ActivityManagement(token).\
        add_auto_activity(code="autotest661forClient", name="autotestactivityforClient")



#############
# test_case #
#############
class TestActivity:
    @staticmethod
    @allure.feature("活動")
    @allure.story("活動類型列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_activity_category"))
    def test_get_activity_category(test, get_user_token, get_activity_id):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動")
    @allure.story("取得單一活動資訊")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_activity_info"))
    def test_get_activity_info(test, get_user_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動")
    @allure.story("參加活動")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("join_activity"))
    def test_join_activity(test, get_user_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test["params"], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動")
    @allure.story("參加活動狀態")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_join_activity_status"))
    def test_get_join_activity_status(test, get_user_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動")
    @allure.story("活動列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_activity_list"))
    def test_get_activity_list(test, get_user_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test["params"], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動")
    @allure.story("推薦活動列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_recommend_list"))
    def test_get_recommend_list(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test["json"],
                                test["params"], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動獎勵")
    @allure.story("彈窗未領取的彩金")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_unclaimed_reward_list"))
    def test_get_unclaimed_reward_list(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test["json"],
                                test["params"], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)
