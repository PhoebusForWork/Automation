import pytest
import allure
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller
from utils.postgres_utils import User_wallet
from pylib.website.wallet import Wallet

td = JsonReader()
testData = td.read_json5('test_wallet.json5', file_side='cs')


######################
#  setup & teardown  #
######################

@pytest.fixture(scope="class")  #
def reset_user_wallet_for_deposit(getCsLoginToken):
    do_withdraw = Wallet()
    do_withdraw.wallet_game_transfer_withdraw_all(
        webToken=getCsLoginToken)
    reset = User_wallet()
    reset.user_wallet_reset(balance=100)
    yield
    do_withdraw.wallet_game_transfer_withdraw_all(
        webToken=getCsLoginToken)


@pytest.fixture(scope="class")  #
def reset_user_wallet_for_withdraw(getCsLoginToken, get_user_id):
    do_withdraw = Wallet()
    do_withdraw.wallet_game_transfer_withdraw_all(
        webToken=getCsLoginToken)
    reset = User_wallet()
    reset.user_wallet_reset(balance=100, user_id=get_user_id)
    do_withdraw.wallet_game_transfer_deposit(
        webToken=getCsLoginToken, channelCode='AWC', amount=100)


@pytest.fixture(scope="class")  #
def reset_user_wallet_for_withdraw_all(getCsLoginToken, get_user_id):
    do_withdraw = Wallet()
    do_withdraw.wallet_game_transfer_withdraw_all(
        webToken=getCsLoginToken)
    reset = User_wallet()
    reset.user_wallet_reset(balance=150, user_id=get_user_id)
    do_withdraw.wallet_game_transfer_deposit(
        webToken=getCsLoginToken, channelCode='AWC', amount=50)


######################
#      testCase      #
######################


@allure.feature("錢包管理")
@allure.story("顯示中心錢包及各遊戲錢包金額和渠道狀態")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'get_wallet_user_info'))
def test_get_wallet_user_info(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getCsLoginToken):

    api = API_Controller(platfrom='cs')
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getCsLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyword in resp.text


class Test_withdraw_all():
    @staticmethod
    @allure.feature("錢包管理")
    @allure.story("一鍵回收")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'wallet_game_transfer_withdraw_all'))
    def test_wallet_game_transfer_withdraw_all(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getCsLoginToken, reset_user_wallet_for_withdraw_all):

        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getCsLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text


class Test_deposit():
    @staticmethod
    @allure.feature("錢包管理")
    @allure.story("將錢轉出至遊戲渠道")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'wallet_game_transfer_deposit'))
    def test_wallet_game_transfer_deposit(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getCsLoginToken, get_user_id, reset_user_wallet_for_deposit):

        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getCsLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text
        if resp.status_code == 200:  # 轉帳成功額外確認資料庫是否正確
            assert User_wallet.user_wallet_deposit_check(user_id=get_user_id,
                                                         check_amount=json['amount'], channel=json['channelCode']) is True


class Test_withdraw():
    @staticmethod
    @allure.feature("錢包管理")
    @allure.story("從指定遊戲渠道轉回中心錢包")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'wallet_game_transfer_withdraw'))
    def test_wallet_game_transfer_withdraw(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getCsLoginToken, get_user_id, reset_user_wallet_for_withdraw):

        api = API_Controller(platfrom='cs')
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getCsLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text
        if resp.status_code == 200:  # 轉帳成功額外確認資料庫是否正確
            assert User_wallet.user_wallet_withdraw_check(user_id=get_user_id,
                                                          check_amount=json['amount'], channel=json['channelCode']) is True


@allure.feature("錢包管理")  # 不能使用噴錯
@allure.story("取得使用者資金明細")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, params, scenario, target, json, code_status, keyword", td.get_test_case(testData, 'get_wallet_front_user_fund'))
def test_get_wallet_front_user_fund(test_case, req_method, req_url, params, scenario, target, json, code_status, keyword, getCsLoginToken):

    json_replace = td.replace_json(params, target)

    api = API_Controller(platfrom='cs')
    resp = api.HttpsClient(req_method, req_url, json,
                           json_replace, token=getCsLoginToken)

    assert resp.status_code == code_status, resp.text
    assert keyword in resp.text
