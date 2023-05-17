import pytest
import allure
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller
from utils.postgres_utils import UserWallet
from pylib.client_side.wallet import GameTransfer

test_data = TestDataReader()
test_data.read_json5('test_wallet.json5', file_side='cs')


######################
#  setup & teardown  #
######################

@pytest.fixture(scope="class")
def reset_user_wallet_for_deposit(get_user_token):
    do_withdraw = GameTransfer(token=get_user_token)
    do_withdraw.wallet_game_transfer_withdraw_all()
    reset = UserWallet()
    reset.reset(balance=100)
    yield
    do_withdraw.wallet_game_transfer_withdraw_all()


@pytest.fixture(scope="class")
def reset_user_wallet_for_withdraw(get_user_token, get_user_id):
    do_withdraw = GameTransfer(token=get_user_token)
    do_withdraw.wallet_game_transfer_withdraw_all()
    reset = UserWallet()
    reset.reset(balance=100, user_id=get_user_id)
    do_withdraw.wallet_game_transfer_deposit(
        channelCode='AI', amount=100)


@pytest.fixture(scope="class")
def reset_user_wallet_for_withdraw_all(get_user_token, get_user_id):
    do_withdraw = GameTransfer(token=get_user_token)
    do_withdraw.wallet_game_transfer_withdraw_all()
    reset = UserWallet()
    reset.reset(balance=150, user_id=get_user_id)
    do_withdraw.wallet_game_transfer_deposit(
        channelCode='AI', amount=50)


######################
#      testCase      #
######################

# 轉帳操作
class TestGameTransfer:
    # 從指定遊戲渠道轉錢回中心錢包
    @staticmethod
    @allure.feature("轉帳操作")
    @allure.story("從指定遊戲渠道轉錢回中心錢包")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.usefixtures("reset_user_wallet_for_withdraw")
    @pytest.mark.parametrize("test", test_data.get_case('wallet_game_transfer_withdraw'))
    def test_wallet_game_transfer_withdraw(test, get_user_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    # 一鍵收回
    @staticmethod
    @allure.feature("轉帳操作")
    @allure.story("一鍵收回")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.usefixtures("reset_user_wallet_for_withdraw_all")
    @pytest.mark.parametrize("test", test_data.get_case('wallet_game_transfer_withdraw_all'))
    def test_wallet_game_transfer_withdraw_all(test, get_user_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    # 將錢轉出至遊戲渠道
    @staticmethod
    @allure.feature("轉帳操作")
    @allure.story("將錢轉出至遊戲渠道")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.usefixtures("reset_user_wallet_for_deposit")
    @pytest.mark.parametrize("test", test_data.get_case('wallet_game_transfer_deposit'))
    def test_wallet_game_transfer_deposit(test, get_user_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    # 顯示中心錢包及各遊戲錢包金額和渠道狀態
    @staticmethod
    @allure.feature("轉帳操作")
    @allure.story("顯示中心錢包及各遊戲錢包金額和渠道狀態")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('get_wallet_user_info'))
    def test_get_wallet_user_info(test, get_user_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_user_token)
        ResponseVerification.basic_assert(resp, test)


# 錢包操作
class TestFrontUser:
    # 取得使用者訂單資訊
    @staticmethod
    @allure.feature("錢包操作")
    @allure.story("取得使用者訂單資訊")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('get_trade_info'))
    def test_get_trade_info(test, get_user_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    # 遊戲可回收餘額
    @staticmethod
    @allure.feature("錢包操作")
    @allure.story("遊戲可回收餘額")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('get_refundable_balance'))
    def test_get_refundable_balance(test, get_user_token):
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    # 取得使用者資金明細
    @staticmethod
    @allure.feature("錢包操作")
    @allure.story("取得使用者資金明細")
    @allure.title("{test[scenario]}")
    # @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('get_wallet_front_user_fund'))
    def test_get_wallet_front_user_fund(test, get_user_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_user_token)
        ResponseVerification.basic_assert(resp, test)

    # 查詢用戶各幣別餘額
    @staticmethod
    @allure.feature("錢包操作")
    @allure.story("查詢用戶各幣別餘額")
    @allure.title("{test[scenario]}")
    @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('get_balance'))
    def test_get_balance(test, get_user_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        api = API_Controller(platform='cs')
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_user_token)
        ResponseVerification.basic_assert(resp, test)
