import pytest
import allure
import time
from pylib.platform.wallet import WalletGameTransferFailed
from utils.data_utils import TestDataReader, ResponseVerification
from utils.generate_utils import Make
from utils.api_utils import API_Controller

test_data = TestDataReader()
test_data.read_json5('test_wallet.json5')


######################
#  setup & teardown  #
######################

# @pytest.fixture(scope="module")
# def turn_on_test_game(getPltLoginToken):
# user_deposit("後台轉入指定渠道")結束後需要執行

#############
# test_case #
#############

class TestUserTransfer:
    @staticmethod
    @allure.feature("客戶列表/資金往來")
    @allure.story("取得所有錢包現狀")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_wallets'))
    def test_get_user_wallets(test, get_platform_token):

        api = API_Controller()
        resp = api.send_request(test['req_method'],
                                test['req_url'],
                                test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶列表/資金往來")  # 查不到資料
    @allure.story("取得使用者交易信息")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_trade_info'))
    def test_get_user_trade_info(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'],
                                test['req_url'],
                                test['json'],
                                params_replace,
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶列表/資金往來")
    @allure.story("取得用戶財物信息")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_user_summary'))
    def test_get_user_summary(test, get_platform_token):
        test['params'] = {"from": Make.generate_custom_date(days=-30), "to": Make.generate_custom_date()}
        print(test['params'])
        params_replace = test_data.replace_json(test['params'], test['target'])

        api = API_Controller()
        resp = api.send_request(test['req_method'],
                                test['req_url'],
                                test['json'],
                                params_replace,
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶列表/資金往來")  # [issue]#25492
    @allure.story("刷新所有子錢包餘額")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('update_balance_all'))
    def test_update_balance_all(test, get_platform_token):

        api = API_Controller()
        resp = api.send_request(test['req_method'],
                                test['req_url'],
                                test['json'],
                                test['params'],
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶列表/資金往來")
    @allure.story("後台轉入指定渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('user_deposit'))
    def test_user_deposit(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'],
                                test['req_url'],
                                json_replace,
                                test['params'],
                                token=get_platform_token)
        if "第一次新增錢包" in test['scenario']:
            time.sleep(5)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶列表/資金往來")
    @allure.story("後台一鍵收回")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('user_withdraw_all'))
    def test_user_withdraw_all(test, get_platform_token):

        api = API_Controller()
        resp = api.send_request(test['req_method'],
                                test['req_url'],
                                test['json'],
                                test['params'],
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("客戶列表/資金往來")
    @allure.story("轉帳紀錄")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_game_transfer'))
    def test_get_game_transfer(test, get_platform_token):

        params_replace = test_data.replace_json(test['params'], test['target'])

        api = API_Controller()
        resp = api.send_request(test['req_method'],
                                test['req_url'],
                                test['json'],
                                params_replace,
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


class TestGameTransferFail:

    @staticmethod
    @allure.feature("異常轉帳處理")
    @allure.story("顯示所有異常處理人")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_fail_approver'))
    def test_get_fail_approver(test, get_platform_token):

        api = API_Controller()
        resp = api.send_request(test['req_method'],
                                test['req_url'],
                                test['json'],
                                test['params'],
                                token=get_platform_token)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("異常轉帳處理")
    @allure.story("手動處理異常轉帳")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('trade_manual_result'))
    def test_trade_manual_result(test, get_platform_token):

        test['json'] = test_data.replace_json(test['json'], test['target'])

        if "存在ID" in test['req_url']:
            failed_id = WalletGameTransferFailed()
            test['req_url'] = test['req_url'].replace(
                "存在ID",
                str(failed_id.get_failed_id_unused(
                    plat_token=get_platform_token))
            )

        api = API_Controller()
        resp = api.send_request(test['req_method'],
                                test['req_url'],
                                test['json'],
                                test['params'],
                                token=get_platform_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("異常轉帳處理")
    @allure.story("異常轉帳處理列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test",
                             test_data.get_case('get_game_transfer_fail_list')
                             )
    def test_get_game_transfer_fail_list(test, get_platform_token):

        test['params'] = test_data.replace_json(test['params'], test['target'])

        if "存在ID" == test['params']['tradeId']:
            failed_id = WalletGameTransferFailed()
            test['params']['tradeId'] = test['params']['tradeId'].replace(
                "存在ID",
                str(failed_id.get_failed_id(plat_token=get_platform_token))
            )

        api = API_Controller()
        resp = api.send_request(test['req_method'],
                                test['req_url'],
                                test['json'],
                                test['params'],
                                token=get_platform_token)

        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class TestWater:
    @staticmethod
    @allure.feature("流水相關操作")
    @allure.story("一鍵流水清零")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('waterAndValidWaterClear'))
    def test_water_and_valid_water_clear(test, get_platform_token):
        if "currency" in test['scenario']:
            params_replace = test_data.replace_json(test['params'], test['target'])
            api = API_Controller()
            resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                    params_replace, token=get_platform_token)
            ResponseVerification.basic_assert(resp, test)

        else:
            json_replace = test_data.replace_json(test['json'], test['target'])
            params_replace = test_data.replace_json(test['params'], test['target'])
            api = API_Controller()
            resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                    params_replace, token=get_platform_token)
            ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("流水相關操作")
    @allure.story("提現流水清零")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('waterClear'))
    def test_water_clear(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("流水相關操作")
    @allure.story("限制流水清零")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('limitWaterClear'))
    def test_limit_water_clear(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("流水相關操作")
    @allure.story("獲取提現流水匯總")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('waterTotal'))
    def test_water_total(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("流水相關操作")
    @allure.story("獲取提現流水清零列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('clearPendingList'))
    def test_clear_pending_list(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("流水相關操作")
    @allure.story("獲取提現限制流水匯總(無資料)")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('limitWaterTotalNoData'))
    def test_limit_water_total_no_data(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("流水相關操作")
    @allure.story("獲取提現限制流水匯總(有資料)")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('limitWaterTotalWithData'))
    # @pytest.mark.xfail(reason='待修復')
    def test_limit_water_total_with_data(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("流水相關操作")
    @allure.story("獲取提現限制流水清零列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('limitWaterClearPendingList'))
    def test_limit_water_clear_pending_list(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)
