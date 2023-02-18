import pytest
import allure
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller
from utils.postgres_utils import User_wallet
from pylib.client_side.wallet import Wallet

td = JsonReader()
td.read_json5('test_wallet.json5', file_side='cs')


######################
#  setup & teardown  #
######################

@pytest.fixture(scope="class")  #
def reset_user_wallet_for_deposit(get_client_side_token):
    do_withdraw = Wallet()
    do_withdraw.wallet_game_transfer_withdraw_all(
        web_token=get_client_side_token)
    reset = User_wallet()
    reset.user_wallet_reset(balance=100)
    yield
    do_withdraw.wallet_game_transfer_withdraw_all(
        web_token=get_client_side_token)


@pytest.fixture(scope="class")  #
def reset_user_wallet_for_withdraw(get_client_side_token, get_user_id):
    do_withdraw = Wallet()
    do_withdraw.wallet_game_transfer_withdraw_all(
        web_token=get_client_side_token)
    reset = User_wallet()
    reset.user_wallet_reset(balance=100, user_id=get_user_id)
    do_withdraw.wallet_game_transfer_deposit(
        web_token=get_client_side_token, channelCode='AWC', amount=100)


@pytest.fixture(scope="class")  #
def reset_user_wallet_for_withdraw_all(get_client_side_token, get_user_id):
    do_withdraw = Wallet()
    do_withdraw.wallet_game_transfer_withdraw_all(
        web_token=get_client_side_token)
    reset = User_wallet()
    reset.user_wallet_reset(balance=150, user_id=get_user_id)
    do_withdraw.wallet_game_transfer_deposit(
        web_token=get_client_side_token, channelCode='AWC', amount=50)


######################
#      testCase      #
######################


@allure.feature("錢包管理")
@allure.story("顯示中心錢包及各遊戲錢包金額和渠道狀態")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('get_wallet_user_info'))
def test_get_wallet_user_info(test, get_client_side_token):

    api = API_Controller(platfrom='cs')
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=get_client_side_token)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


class Test_withdraw_all():
    @staticmethod
    @allure.feature("錢包管理")
    @allure.story("一鍵回收")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('wallet_game_transfer_withdraw_all'))
    def test_wallet_game_transfer_withdraw_all(test, get_client_side_token, reset_user_wallet_for_withdraw_all):

        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class Test_deposit():
    @staticmethod
    @allure.feature("錢包管理")
    @allure.story("將錢轉出至遊戲渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('wallet_game_transfer_deposit'))
    def test_wallet_game_transfer_deposit(test, get_client_side_token, get_user_id, reset_user_wallet_for_deposit):

        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text
        if resp.status_code == 200:  # 轉帳成功額外確認資料庫是否正確
            assert User_wallet.user_wallet_deposit_check(user_id=get_user_id,
                                                         check_amount=test['json']['amount'], channel=test['json']['channelCode']) is True


class Test_withdraw():
    @staticmethod
    @allure.feature("錢包管理")
    @allure.story("從指定遊戲渠道轉回中心錢包")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('wallet_game_transfer_withdraw'))
    def test_wallet_game_transfer_withdraw(test, get_client_side_token, get_user_id, reset_user_wallet_for_withdraw):

        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=get_client_side_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text
        if resp.status_code == 200:  # 轉帳成功額外確認資料庫是否正確
            assert User_wallet.user_wallet_withdraw_check(user_id=get_user_id,
                                                          check_amount=test['json']['amount'], channel=test['json']['channelCode']) is True


@allure.feature("錢包管理")  # 不能使用噴錯
@allure.story("取得使用者資金明細")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('get_wallet_front_user_fund'))
def test_get_wallet_front_user_fund(test, get_client_side_token):

    json_replace = td.replace_json(test['params'], test['target'])

    api = API_Controller(platfrom='cs')
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           json_replace, token=get_client_side_token)

    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text
