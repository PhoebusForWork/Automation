from ..platform.platApiBase import PlatformAPI  # 執行RF時使用
from ..client_side.wallet import Wallet
from utils.api_utils import KeywordArgument
from utils.redis_utils import Redis
from utils.xxl_job_utils import XxlJobs
from utils.data_utils import EnvReader
import time
import jsonpath


env = EnvReader()
platform_host = env.PLATFORM_HOST


class WalletManage(PlatformAPI):

    def water_clear_all(self,  # 一鍵流水清零
                        plat_token=None,
                        userId=None,
                        remark=None,
                        ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/water/manage/withdrawWater/waterAndValidWater/clear",
                                json={
                                    "userId": userId,
                                    "remark": remark
                                },
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def withdraw_water_clear(self,  # 提現流水清零
                             plat_token=None,
                             userId=None,
                             remark=None,
                             ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/water/manage/withdrawWater/water/clear",
                                json={
                                    "userId": userId,
                                    "remark": remark
                                },
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def withdraw_limit_water_clear(self,  # 限制流水清零
                                   plat_token=None,
                                   userId=None,
                                   remark=None,
                                   ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/water/manage/withdrawLimitWater/water/clear",
                                json={
                                    "userId": userId,
                                    "remark": remark
                                },
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def get_withdraw_water_total(self,  # 獲取提現流水匯總
                                 plat_token=None,
                                 userId=None,
                                 ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/water/manage/withdrawLimitWater/water/clear",
                               json={},
                               params={
                                   "userId": userId
                               }
                               )
        self.print_response(response)
        return response.json()

    def get_withdraw_water_clear_pending_list(self,  # 獲取提現流水清零列表
                                              plat_token=None,
                                              userId=None,
                                              orderId=None,
                                              orderType=None,
                                              adminName=None,
                                              waterStatus=None,
                                              page=None,
                                              size=None,
                                              ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/water/manage/withdrawWater/clearPendingList",
                               json={},
                               params=KeywordArgument.body_data()
                               )
        self.print_response(response)
        return response.json()

    def get_withdraw_limit_water_total(self,  # 獲取提現限制流水匯總
                                       plat_token=None,
                                       userId=None,
                                       ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/water/manage/withdrawLimitWater/total",
                               json={},
                               params={
                                   "userId": userId,
                               }
                               )
        self.print_response(response)
        return response.json()

    def get_withdraw_limit_water_clear_pending_list(self,  # 獲取提現限制流水清零列表
                                                    plat_token=None,
                                                    userId=None,
                                                    orderId=None,
                                                    orderType=None,
                                                    adminName=None,
                                                    waterStatus=None,
                                                    limitGameType=None,
                                                    limitGameCode=None,
                                                    page=None,
                                                    size=None,
                                                    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/water/manage/withdrawLimitWater/clearPendingList",
                               json={},
                               params=KeywordArgument.body_data()
                               )
        self.print_response(response)
        return response.json()


class WalletUser(PlatformAPI):

    def get_wallets(self,  # 取得所有錢包現狀
                    plat_token=None,
                    userId=None,
                    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+f"/v1/wallet/user/{userId}/wallets",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_trade_info(self,  # 取得使用者交易信息
                       plat_token=None,
                       userId=None,
                       From=None, to=None,
                       types=None,  # 交易类型:0轉帳|6返水|7存款|8紅利|9提款|10上分|12充值補分|13充值減分|14加幣|15減幣
                       status=None,  # 交易状态:0轉帳中|1成功|2失敗
                       page=None, size=None,

                       ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+f"/v1/wallet/user/{userId}/trade/info",
                               json={},
                               params={
                                   "from": From,
                                   "to": to,
                                   "types": types,
                                   "status": status,
                                   "page": page,
                                   "size": size,
                               }
                               )
        self.print_response(response)
        return response.json()

    def get_fund(self,  # 取得用戶財務信息
                        plat_token=None,
                        userId=None,
                        From=None, to=None,
                 ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+f"/v1/wallet/user/{userId}/fund",
                               json={},
                               params={
                                   "from": From,
                                   "to": to,
                               }
                               )
        self.print_response(response)
        return response.json()


class WalletGameTransfer(PlatformAPI):

    def update_balance_all(self,  # 刷新所有子錢包餘額
                           plat_token=None,
                           userId=None,
                           ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+f"/v1/wallet/game/transfer/user/{userId}/update/balance/all",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def withdraw_all(self,  # 後台一鍵回收
                     plat_token=None,
                     userId=None,
                     ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+f"/v1/wallet/game/transfer/user/{userId}/withdraw/all",
                                json={},
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def deposit(self,  # 後台轉入指定渠道
                plat_token=None,
                userId=None,
                channelCode=None,
                amount=None,
                ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+f"/v1/wallet/game/transfer/user/{userId}/deposit",
                                json={
                                    "channelCode": channelCode,
                                    "amount": amount,
                                },
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def get_game_transfer(self,  # 轉賬記錄
                          plat_token=None,
                          timeType=None,  # 時間類型 1:轉帳時間|2:更新時間
                          startTime='2022-01-01T00:00:00Z', endTime='2023-01-01T00:00:00Z',
                          username=None,
                          minAmount=None, maxAmount=None,
                          transactionStatus=None,  # 轉帳狀態 0:轉帳中|1:成功|2:失敗|3:錯誤
                          fromChannelCode=None, toChannelCode=None,
                          tradeId=None,
                          page=None, size=None,
                          ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+f"/v1/wallet/game/transfer",
                               json={},
                               params=KeywordArgument.body_data()
                               )
        self.print_response(response)
        return response.json()


class WalletGameTransferFailed(PlatformAPI):

    @staticmethod
    def _create_failed_transfer_record():
        cs_wallet = Wallet()
        data = cs_wallet.login(deviceId="345", username='AutoTester',
                               password="abc123456").json()['data']
        cs_wallet.wallet_game_transfer_withdraw_all()
        time.sleep(2)
        # 回收後進行redis MOCK配置
        set_plt_result = Redis(platform='plt', select=3)
        set_plt_result.conn.hset(
            name='MOCK::AWC', key='recheckResult', value='"UNKNOWN"')
        set_cs_result = Redis(platform='cs', select=12)
        set_cs_result.conn.hset(
            name='MOCK::AWC', key='transferResult', value='"UNKNOWN"')
        set_plt_IrregularTransfer = Redis(platform='plt', select=4)
        set_plt_IrregularTransfer.conn.set(
            name='IrregularTransfer::isTesting', value='true')

        retry_times = 6  # 目前case是消耗3以倍數定值
        for _ in range(retry_times):
            cs_wallet.wallet_game_transfer_deposit(
                channelCode="AWC", amount=10)

        XxlJobs.game_transfer_executor()
        time.sleep(2)

        set_plt_result.conn.hdel(
            'MOCK::AWC', 'recheckResult')
        set_cs_result.conn.hdel(
            'MOCK::AWC', 'transferResult')
        set_plt_IrregularTransfer.conn.delete('IrregularTransfer::isTesting')

    def get_approver(self,  # 顯示所有異常處理人
                     plat_token=None,
                     ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/wallet/game/transfer/failed/approver",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_failed_list(self,  # 轉帳異常處理列表
                        plat_token=None,
                        timeType=None,
                        startTime=None, endTime=None,
                        failedTransferStatus=None,
                        operator=None,
                        fromChannelCode=None, toChannelCode=None,
                        tradeId=None,
                        page=None, size=None,
                        ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/wallet/game/transfer/failed",
                               json={},
                               params=KeywordArgument.body_data()
                               )
        self.print_response(response)
        return response.json()

    def trade_manual_result(self,  # 手動處理異常轉帳
                            plat_token=None,
                            tradeId=None,
                            result=None,
                            remark=None,
                            ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+f"/v1/wallet/game/transfer/failed/tradeId/{tradeId}/manual/result",
                                json={
                                    "result": result,
                                    "remark": remark,
                                },
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def get_failed_id(self,
                      plat_token=None
                      ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        target = self.get_failed_list()
        ret = jsonpath.jsonpath(target, "$..tradeId")[0]
        return ret

    def get_failed_id_unused(self,
                             plat_token=None
                             ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        target = self.get_failed_list(failedTransferStatus=0)
        ret = jsonpath.jsonpath(target, "$..tradeId")
        if ret is False:
            self._create_failed_transfer_record()
            target = self.get_failed_list(failedTransferStatus=0)
            ret = jsonpath.jsonpath(target, "$..tradeId")

        return ret[-1]
