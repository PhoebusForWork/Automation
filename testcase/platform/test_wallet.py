import pytest
import allure
import random
from pylib.platform.wallet import WalletGameTransferFailed
from testcase.platform.conftest import getPltLoginToken
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller

td = JsonReader()
testData = td.read_json5('test_wallet.json5')


######################
#  setup & teardown  #
######################

# @pytest.fixture(scope="module")
# def 一鍵回收用戶餘額(getPltLoginToken):
# user_deposit("後台轉入指定渠道")結束後需要執行

#############
# test_case #
#############

class Test_UserTransfer():
    @staticmethod
    @allure.feature("客戶列表/資金往來")
    @allure.story("取得所有錢包現狀")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'get_user_wallets'))
    def test_get_user_wallets(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getPltLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("客戶列表/資金往來")  # 查不到資料
    @allure.story("取得使用者交易信息")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, params, req_url, scenario, target, json, code_status, keyword", td.get_test_case(testData, 'get_user_trade_info'))
    def test_get_user_trade_info(test_case, req_method, params, req_url, scenario, target, json, code_status, keyword, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getPltLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("客戶列表/資金往來")
    @allure.story("取得用戶財物信息")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, params, req_url, scenario, target, json, code_status, keyword", td.get_test_case(testData, 'get_user_fund'))
    def test_get_user_fund(test_case, req_method, params, req_url, scenario, target, json, code_status, keyword, getPltLoginToken):

        params = td.replace_json(params, target)

        api = API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getPltLoginToken)

        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("客戶列表/資金往來")
    @allure.story("轉帳紀錄")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, params, req_url, scenario, target, json, code_status, keyword", td.get_test_case(testData, 'get_game_transfer'))
    def test_get_game_transfer(test_case, req_method, params, req_url, scenario, target, json, code_status, keyword, getPltLoginToken):

        params = td.replace_json(params, target)

        api = API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getPltLoginToken)

        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("客戶列表/資金往來")  # [issue]#25492
    @allure.story("刷新所有子錢包餘額")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'update_balance_all'))
    def test_update_balance_all(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getPltLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("客戶列表/資金往來")
    @allure.story("後台一鍵收回")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'user_withdraw_all'))
    def test_user_withdraw_all(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getPltLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("客戶列表/資金往來")
    @allure.story("後台轉入指定渠道")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'user_deposit'))
    def test_user_deposit(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getPltLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text


class Test_GameTransferFail():

    @staticmethod
    @allure.feature("異常轉帳處理")
    @allure.story("顯示所有異常處理人")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyword", td.get_test_case(testData, 'get_fail_approver'))
    def test_get_fail_approver(test_case, req_method, req_url, scenario, json, params, code_status, keyword, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getPltLoginToken)
        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("異常轉帳處理")
    @allure.story("異常轉帳處理列表")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, params, req_url, scenario, target, json, code_status, keyword", td.get_test_case(testData, 'get_game_transfer_fail_list'))
    def test_get_game_transfer_fail_list(test_case, req_method, params, req_url, scenario, target, json, code_status, keyword, getPltLoginToken):

        params = td.replace_json(params, target)

        if "存在ID" == params['tradeId']:
            failed_id = WalletGameTransferFailed()
            params['tradeId'] = params['tradeId'].replace(
                "存在ID", str(failed_id.get_failed_id(platToken=getPltLoginToken)))

        api = API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getPltLoginToken)

        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text

    @staticmethod
    @allure.feature("異常轉帳處理")
    @allure.story("手動處理異常轉帳")
    @allure.title("{scenario}")
    @pytest.mark.parametrize("test_case, req_method, json, req_url, scenario, target, params, code_status, keyword", td.get_test_case(testData, 'trade_manual_result'))
    def test_trade_manual_result(test_case, req_method, json, req_url, scenario, target, params, code_status, keyword, getPltLoginToken):

        json = td.replace_json(json, target)

        if "存在ID" in req_url:
            failed_id = WalletGameTransferFailed()
            req_url = req_url.replace(
                "存在ID", str(failed_id.get_failed_id_unused(platToken=getPltLoginToken)))

        api = API_Controller()
        resp = api.HttpsClient(req_method, req_url, json,
                               params, token=getPltLoginToken)

        assert resp.status_code == code_status, resp.text
        assert keyword in resp.text
