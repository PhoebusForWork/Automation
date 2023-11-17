import pytest
import allure
from pylib.platform.activity import ActivityManagement
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller

test_data = TestDataReader()
test_data.read_json5("test_activity.json5")


######################
#  setup & teardown  #
######################
@pytest.fixture(scope="class")
def get_activity_id(get_platform_token):
    activity_id = ActivityManagement(token=get_platform_token).\
        test_get_activity_id(code="autotest661", name="autotestactivity")
    yield activity_id


@pytest.fixture(scope="class")
def get_activity_del_id(get_platform_token):
    activity_del_id = ActivityManagement(token=get_platform_token).\
        test_get_activity_id(code="autotestdel661", name="autotestactivity")
    yield activity_del_id


@pytest.fixture(scope="class")
def get_recommend_activity_id(get_platform_token):
    recommend_activity_id = ActivityManagement(token=get_platform_token).\
        test_get_recommend_id(code="autotest661", activityName="autotestactivity")
    yield recommend_activity_id


#############
# test_case #
#############
class TestActivityManagement:
    # SIT環境，ADD、delete 可以不用跑(CODE:autotest661,autotestdel661)
    @staticmethod
    @allure.feature("活動管理")
    @allure.story("新增活動")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("add_activity"))
    def test_add_activity(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動管理")
    @allure.story("刪除活動")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("delete_activity"))
    def test_delete_activity(test, get_platform_token, get_activity_del_id):
        activity_del_id = get_activity_del_id
        test['req_url'] = test['req_url'].replace("存在activity_id", str(activity_del_id))
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動管理")
    @allure.story("修改活動")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("update_activity"))
    def test_update_activity(test, get_platform_token, get_activity_id):
        activity_id = get_activity_id
        test['json']['id'] = activity_id
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動管理")
    @allure.story("取得活動列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_activity_list"))
    def test_get_activity_list(test, get_platform_token):

        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)

        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動管理")
    @allure.story("取得單一活動資訊")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_activity"))
    def test_get_activity(test, get_platform_token, get_activity_id):
        activity_id = get_activity_id
        test['req_url'] = test['req_url'].replace("存在activity_id", str(activity_id))
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動管理")
    @allure.story("修改活動狀態")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("update_activity_status"))
    def test_update_activity_status(test, get_platform_token, get_activity_id):
        activity_id = get_activity_id
        test['json']['id'] = activity_id
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動管理")
    @allure.story("活動類型列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_activity_category"))
    def test_get_activity_category(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            params_replace,
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動管理")
    @allure.story("顯示所有操作者")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_activity_list_operator"))
    def test_get_activity_list_operator(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動推薦管理")
    @allure.story("活動推薦下拉選單")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_select_activity_list"))
    def test_get_select_activity_list(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動推薦管理")
    @allure.story("新增推薦活動")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("add_recommend_activity"))
    def test_add_recommend_activity(test, get_platform_token, get_activity_id):
        activity_id = get_activity_id
        test['json']['activityId'] = activity_id
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動推薦管理")
    @allure.story("調整推薦活動")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("update_recommend_activity"))
    def test_update_recommend_activity(test, get_platform_token, get_recommend_activity_id):
        recommend_activity_id = get_recommend_activity_id
        test['json']['activityRecommendId'] = recommend_activity_id
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動推薦管理")
    @allure.story("推薦活動列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_recommend_list"))
    def test_get_recommend_list(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動推薦管理")
    @allure.story("刪除推薦活動")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("delete_recommend_activity"))
    def test_delete_recommend_activity(test, get_platform_token, get_recommend_activity_id):
        recommend_activity_id = get_recommend_activity_id
        test['req_url'] = test['req_url'].replace("存在recommend_id", str(recommend_activity_id))
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動管理")
    @allure.story("活動獎勵查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_reward_list"))
    def test_get_reward_list(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            params_replace,
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("活動管理")
    @allure.story("活動參賽名單")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_activity_participation_list"))
    def test_get_activity_participation_list(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)
    #
    # @staticmethod
    # @allure.feature("活動管理")
    # @allure.story("資金配置管理 - 添加活動紅利")
    # @allure.title("{test[scenario]}")
    # @pytest.mark.regression
    # @pytest.mark.parametrize("test", test_data.get_case("get_active_activities"))
    # def test_get_active_activities(test, get_platform_token):
    #     api = API_Controller()
    #     resp = api.send_request(
    #         test["req_method"],
    #         test["req_url"],
    #         test["json"],
    #         test["params"],
    #         token=get_platform_token,
    #     )
    #     ResponseVerification.basic_assert(resp, test)
    #
