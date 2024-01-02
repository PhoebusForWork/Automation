import pytest
import allure
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller
from utils.generate_utils import Make
from pylib.platform.platApiBase import PlatformAPI
from pylib.platform.game import Game
from pylib.client_side.webApiBase import WebAPI

test_data = TestDataReader()
test_data.read_json5('test_game.json5', file_side='cs')


######################
#  setup & teardown  #
######################
@pytest.fixture(scope="class")
def set_game_type_list():
    api = PlatformAPI()
    code = api.imgcode()
    resp = api.login(username='superAdmin', password='abc123456', imgCode=code)
    token = resp.json()['data']['token']
    instantiate = Game(token)
    instantiate.put_game_type()

######################
#      testCase      #
######################


class TestGameRelated:
    @staticmethod
    @allure.feature("遊戲相關")
    @allure.story("遊戲列表下拉選單(注單查詢用)")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('game_select_list'))
    def test_game_select_list(test, get_user_token, set_game_type_list):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("遊戲相關")
    @allure.story("遊戲類型列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('game_type'))
    def test_game_type(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("遊戲相關")
    @allure.story("遊戲跳轉")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('game_redirect'))
    def test_game_redirect(test, get_user_token):
        api = API_Controller(platform='cs')
        if test["scenario"] == "遊戲跳轉過於頻繁":
            for _ in range(4):
                resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                        test['params'], token=get_user_token)
        else:
            resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                    test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("遊戲相關")
    @allure.story("常用遊戲列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('game_usual'))
    def test_game_usual(test, get_user_token):
        if test["scenario"] == "未有遊戲紀錄":
            instantiate = WebAPI()
            get_user_token = instantiate.login(username='generic001').json()['data']['token']
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("遊戲相關")
    @allure.story("遊戲列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('game_list'))
    def test_game_list(test):
        api = API_Controller(platform='cs')
        login_token = WebAPI().login(username="generic003").json()['data']['token']
        if test['scenario'] == "os_type_APP":
            api.request_session.headers['os-type'] = 'ANDROID'
        elif test['scenario'] == "os_type_H5":
            api.request_session.headers['os-type'] = 'H5'
        else:
            api.request_session.headers['os-type'] = None
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=login_token)
        ResponseVerification.basic_assert(resp, test)


class TestGameOrder:
    @staticmethod
    @allure.feature("遊戲注單")
    @allure.story("注單查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_game_order'))
    def test_get_game_order(test):
        startime = Make.generate_custom_date(months=-3)
        endtime = Make.generate_custom_date(days=1)
        test['param'].update({'from':startime, 'to':endtime})
        web_api = WebAPI()
        resp = web_api.login(username='generic001')
        token = resp.json()['data']['token']
        if test['scenario'] == '不帶條件查詢':
            param_replace = {}
        else:
            param_replace = test_data.replace_json(test['param'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                param_replace, token=token)

        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("遊戲注單")
    @allure.story("注單總和查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_game_order_summary'))
    def test_get_game_order_summary(test):
        web_api = WebAPI()
        resp = web_api.login(username='generic001')
        token = resp.json()['data']['token']
        if test['scenario'] == '不帶條件查詢':
            param_replace = {}
        else:
            param_replace = test_data.replace_json(test['param'], test['target'])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                param_replace, token=token)

        ResponseVerification.basic_assert(resp, test)
