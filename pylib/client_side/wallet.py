# -*- coding: utf-8 -*-
from ..client_side.webApiBase import WebAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader

env = EnvReader()
web_host = env.WEB_HOST


# 轉帳操作
class GameTransfer(WebAPI):
    # 從指定遊戲渠道轉錢回中心錢包
    def wallet_game_transfer_withdraw(self,
                                      currency=None,
                                      channelCode=None,
                                      amount=None):
        request_body = {
            "method": "post",
            "url": "/v1/wallet/game/transfer/user/withdraw",
            "params": {"currency": currency},
            "json": {
                "channelCode": channelCode,
                "amount": amount
            }
        }

        response = self.send_request(**request_body)
        return response.json()

    # 一鍵回收
    def wallet_game_transfer_withdraw_all(self,
                                          currency=None):
        request_body = {
            "method": "post",
            "url": "/v1/wallet/game/transfer/user/withdraw/all",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 將錢轉出至遊戲渠道
    def wallet_game_transfer_deposit(self,
                                     channelCode=None,
                                     amount=None,
                                     currency=None):
        request_body = {
            "method": "post",
            "url": "/v1/wallet/game/transfer/user/deposit",
            "params": {"currency": currency},
            "json": {
                "channelCode": channelCode,
                "amount": amount
            }
        }

        response = self.send_request(**request_body)
        return response.json()

    # 顯示中心錢包及各遊戲錢包金額和渠道狀態
    def get_wallet_user_info(self,
                             currency=None):
        request_body = {
            "method": "get",
            "url": "/v1/wallet/game/transfer/user/info",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()


# 錢包操作
class FrontUser(WebAPI):
    # 遊戲可回收餘額
    def get_refundable_balance(self, userId=None,
                               currency=None):
        request_body = {
            "method": "get",
            "url": f"/v1/wallet/front/user/{userId}/refundable/balance",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 取得使用者訂單資訊
    def get_trade_info(self, tradeId=None):
        request_body = {
            "method": "get",
            "url": f"/v1/wallet/front/user/trade/info/{tradeId}",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 取得使用者資金明細
    # 交易類型：充值7｜提款9｜轉帳0｜紅利/充值獎勵/紅包/平台獎勵/派彩/老用戶活動紅利 皆合併至紅利8｜返水6｜加幣13｜減幣14｜上級轉入10
    def get_wallet_front_user_fund(self, From=None, to=None,
                                   transactionType=None, transactionStatus=None,
                                   page=None, size=None):
        request_body = {
            "method": "get",
            "url": "/v1/wallet/front/user/fund",
            "params": {
                "from": From,
                "to": to,
                "transactionType": transactionType,
                "transactionStatus": transactionStatus,
                "page": page,
                "size": size
            }
        }

        response = self.send_request(**request_body)
        return response.json()

    # 取得使用者訂單資訊
    def get_balance(self):
        request_body = {
            "method": "get",
            "url": "/v1/wallet/front/user/balance"
        }
        response = self.send_request(**request_body)
        return response.json()


class TestGameTransferMock(WebAPI):
    # 顯示中心錢包及各遊戲錢包金額和渠道狀態
    def get_wallet_user_info(self):
        request_body = {
            "method": "get",
            "url": "/v1/wallet/game/transfer/user/info"
        }

        response = self.send_request(**request_body)
        return response.json()

    #  塞轉帳用的MOCK資料
    def add_mock(self,
                 channel_code=None,
                 gameBalance=None,
                 result=None):
        request_body = {
            "method": "post",
            "url": f"/v1/test/game/transfer/mock/{channel_code}",
            "json": {"url": None,
                     "gameBalance": gameBalance,
                     "result": result
                     }
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
