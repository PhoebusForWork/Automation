from ..platform.platApiBase import PlatformAPI  # 執行RF時使用
from ..client_side.wallet import GameTransfer, TestGameTransferMock as CsMock
from utils.api_utils import KeywordArgument
from utils.redis_utils import RedisSentinel
from utils.xxl_job_utils import XxlJobs
from utils.data_utils import EnvReader
from utils.generate_utils import Make
import time
import jsonpath
import os

xxl = XxlJobs()
env = EnvReader()
platform_host = env.PLATFORM_HOST


class WalletManage(PlatformAPI):
    # 一鍵流水清零
    def water_clear_all(self, userId=None, remark=None, currency=None):
        request_body = {
            "method": "post",
            "url": "/v1/water/manage/withdrawWater/waterAndValidWater/clear",
            "json": KeywordArgument.body_data(),
            "params": currency
        }

        response = self.send_request(**request_body)
        return response.json()

    # 提現流水清零
    def withdraw_water_clear(self, plat_token=None, userId=None, remark=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/water/manage/withdrawWater/water/clear",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 限制流水清零
    def withdraw_limit_water_clear(self,
                                   plat_token=None,
                                   userId=None,
                                   remark=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/water/manage/withdrawLimitWater/water/clear",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取提現流水匯總
    def get_withdraw_water_total(self,
                                 plat_token=None,
                                 userId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/water/manage/withdrawLimitWater/water/clear",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取提現流水清零列表
    def get_withdraw_water_clear_pending_list(
            self, plat_token=None, userId=None, orderId=None, orderType=None,
            adminName=None, waterStatus=None, page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/water/manage/withdrawWater/clearPendingList",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取提現限制流水匯總
    def get_withdraw_limit_water_total(self, plat_token=None, userId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/water/manage/withdrawLimitWater/total",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取提現限制流水清零列表
    def get_withdraw_limit_water_clear_pending_list(
            self, plat_token=None, userId=None,
            orderId=None, orderType=None, adminName=None,
            waterStatus=None, limitGameType=None,
            limitGameCode=None, page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/water/manage/withdrawLimitWater/clearPendingList",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()


class WalletUser(PlatformAPI):
    # 取得所有錢包現狀
    def get_wallets(self, plat_token=None, userId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/wallet/user/{userId}/wallets"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 取得使用者交易信息
    def get_trade_info(
            self, plat_token=None, userId=None, From=None, to=None,
            types=None,  # 交易类型:0轉帳|6返水|7存款|8紅利|9提款|10上分|12充值補分|13充值減分|14加幣|15減幣
            status=None,  # 交易状态:0轉帳中|1成功|2失敗
            page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/wallet/user/{userId}/trade/info",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 取得用戶財務信息
    def get_fund(self, plat_token=None, userId=None, From=None, to=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/wallet/user/{userId}/fund",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()


class WalletGameTransfer(PlatformAPI):
    # 刷新所有子錢包餘額
    def update_balance_all(self, plat_token=None, userId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/wallet/game/transfer/user/{userId}/update/balance/all"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 後台一鍵回收
    def withdraw_all(self, plat_token=None, userId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": f"/v1/wallet/game/transfer/user/{userId}/withdraw/all",
        }

        response = self.send_request(**request_body)
        return response.json()

    # 後台轉入指定渠道
    def deposit(self, plat_token=None,
                userId=None, channelCode=None, amount=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": f"/v1/wallet/game/transfer/user/{userId}/deposit",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 轉賬記錄
    def get_game_transfer(
            self, plat_token=None,
            timeType=None,  # 時間類型 1:轉帳時間|2:更新時間
            startTime='2022-01-01T00:00:00Z', endTime='2023-01-01T00:00:00Z',
            username=None, minAmount=None, maxAmount=None,
            transactionStatus=None,  # 轉帳狀態 0:轉帳中|1:成功|2:失敗|3:錯誤
            fromChannelCode=None, toChannelCode=None,
            tradeId=None,
            page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/wallet/game/transfer",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()


class TestGameTransferMock(PlatformAPI):
    #  後台從中心錢包轉錢至指定渠道
    def mock_deposit(self, plat_token, userId,
                     channelCode=None,
                     gameCode=None,
                     amount=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        request_body = {
            "method": "post",
            "url": f"/v1/test/game/transfer/user/{userId}/deposit",
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    #  塞轉帳用的MOCK資料
    def add_mock(self,
                 channelCode=None,
                 gameBalance=None,
                 result=None,
                 recheckResult=None):
        request_body = {
            "method": "post",
            "url": f"/v1/test/game/transfer/mock/{channelCode}",
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    #  刪除轉帳用的MOCK資料
    def delete_mock(self,
                    channelCode=None
                    ):
        request_body = {
            "method": "delete",
            "url": f"/v1/test/game/transfer/mock/{channelCode}",
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    #  塞是否測試異常轉帳資料
    def irregular_testing(self,
                          is_testing: bool = None):
        request_body = {
            "method": "post",
            "url": "/v1/test/game/transfer/irregular/transaction/isTesting",
            "json": is_testing
        }
        response = self.send_request(**request_body)
        return response.json()


class WalletGameTransferFailed(PlatformAPI):
    @staticmethod
    def _create_failed_transfer_record():
        cs_wallet = GameTransfer()
        cs_wallet.login(deviceId="345",
                        username='AutoTester',
                        password="abc123456")
        cs_wallet.wallet_game_transfer_withdraw_all()
        time.sleep(2)
        # 回收後進行redis MOCK配置
        set_plt_result = RedisSentinel(platform='plt', select=3)
        set_plt_result.master.hset(name='MOCK::AWC',
                                   key='recheckResult',
                                   value='"UNKNOWN"')
        set_cs_result = RedisSentinel(platform='cs', select=12)
        set_cs_result.master.hset(name='MOCK::AWC',
                                  key='transferResult',
                                  value='"UNKNOWN"')
        set_plt_irregular_transfer = RedisSentinel(platform='plt', select=4)
        set_plt_irregular_transfer.master.set(
            name='IrregularTransfer::isTesting',
            value='true')

        retry_times = 6  # 目前case是消耗3以倍數定值
        for _ in range(retry_times):
            cs_wallet.wallet_game_transfer_deposit(channelCode="AWC",
                                                   amount=10)

        xxl.game_transfer_executor()
        time.sleep(2)

        set_plt_result.master.hdel('MOCK::AWC', 'recheckResult')
        set_cs_result.master.hdel('MOCK::AWC', 'transferResult')
        set_plt_irregular_transfer.master.delete('IrregularTransfer::isTesting')

    @staticmethod
    def _create_failed_transfer_record_v2(cs_user='ptest01'):
        if os.getenv('MODE'):
            cs_user = 'wallet001'
        cs_wallet = GameTransfer()
        cs_wallet.login(deviceId="345",
                        username=cs_user,
                        password="abc123456")
        cs_wallet.wallet_game_transfer_withdraw_all()
        time.sleep(2)
        #  回收後進行redis MOCK配置
        #  目前只有AI後續如果欲新增的話要想一下相關邏輯改寫
        set_plt_mock = TestGameTransferMock()
        set_plt_mock.add_mock(gameBalance=10,
                              channelCode='AI',
                              result='UNKNOWN',
                              recheckResult='UNKNOWN')
        set_cs_mock = CsMock()
        set_cs_mock.add_mock(channel_code='AI',
                             gameBalance=10,
                             result='UNKNOWN')
        # 以廢棄改xxl_job
        # set_plt_mock.irregular_testing(is_testing=True)
        xxl.game_transfer_fail(isTesting=True)
        retry_times = 6  # 目前case是消耗3以倍數定值
        for _ in range(retry_times):
            cs_wallet.wallet_game_transfer_deposit(channelCode="AI",
                                                   amount=10)
        xxl.game_transfer_executor()
        time.sleep(2)

        set_plt_mock.delete_mock(channelCode='AI')
        set_cs_mock.delete_mock(channelCode='AI')
        # 以廢棄改xxl_job
        # set_plt_mock.irregular_testing(is_testing=False)
        xxl.game_transfer_fail(isTesting=False)

    # 顯示所有異常處理人
    def get_approver(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/wallet/game/transfer/failed/approver"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 轉帳異常處理列表
    def get_failed_list(
            self, timeType=None, currency=None, dateType=1,
            startTime=Make.date('start'), endTime=Make.date('end'), failedTransferStatus=None,
            operator=None, fromChannelCode=None, toChannelCode=None,
            tradeId=None, page=None, size=None
    ):
        request_body = {
            "method": "get",
            "url": "/v1/wallet/game/transfer/failed",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 手動處理異常轉帳
    def trade_manual_result(self, tradeId=None, result=None, remark=None):
        request_body = {
            "method": "post",
            "url": f"/v1/wallet/game/transfer/failed/tradeId/{tradeId}/manual/result",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢第三方結果
    def get_fail_tradeid_status(self, tradeId=None):
        request_body = {
            "method": "get",
            "url": f"/v1/wallet/game/transfer/failed/tradeId/{tradeId}"
        }
        response = self.send_request(**request_body)
        return response.json()

    def get_failed_id(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        target = self.get_failed_list()
        ret = jsonpath.jsonpath(target, "$..tradeId")[0]
        return ret

    def get_failed_id_unused(self, plat_token=None):
        # if plat_token is not None:
        #     self.request_session.headers.update({"token": str(plat_token)})
        # target = self.get_failed_list(failedTransferStatus=0)
        # ret = jsonpath.jsonpath(target, "$..tradeId")
        # if ret is False:
        self._create_failed_transfer_record_v2()
        target = self.get_failed_list(failedTransferStatus=0)
        ret = jsonpath.jsonpath(target, "$..tradeId")

        return ret[-1]
