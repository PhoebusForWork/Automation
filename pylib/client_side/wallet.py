# -*- coding: utf-8 -*-
from ..client_side.webApiBase import WebAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader

env = EnvReader()
web_host = env.WEB_HOST


class Wallet(WebAPI):
    # 顯示中心錢包及各遊戲錢包金額和渠道狀態
    def get_wallet_user_info(self, web_token=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "get",
            "url": "/v1/wallet/game/transfer/user/info"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 從指定遊戲渠道轉錢回中心錢包
    def wallet_game_transfer_withdraw(self,
                                      web_token=None,
                                      channelCode=None,
                                      amount=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "post",
            "url": "/v1/wallet/game/transfer/user/withdraw",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 一鍵回收
    def wallet_game_transfer_withdraw_all(self, web_token=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "post",
            "url": "/v1/wallet/game/transfer/user/withdraw/all"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 將錢轉出至遊戲渠道
    def wallet_game_transfer_deposit(self,
                                     web_token=None,
                                     channelCode=None,
                                     amount=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "post",
            "url": "/v1/wallet/game/transfer/user/deposit",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 取得使用者資金明細
    def get_wallet_front_user_fund(self, web_token=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "get",
            "url": "/v1/wallet/front/user/fund",
            "params": {"from": "2022-10-01T00:00:00Z",
                       "to": "2023-10-07T00:00:00Z"}
        }

        response = self.send_request(**request_body)
        return response.json()


class TestGameTransferMock(WebAPI):
    # 顯示中心錢包及各遊戲錢包金額和渠道狀態
    def get_wallet_user_info(self, web_token=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "get",
            "url": "/v1/wallet/game/transfer/user/info"
        }

        response = self.send_request(**request_body)
        return response.json()

    #  塞轉帳用的MOCK資料
    def add_mock(self,
                 user_id,
                 web_token=None,
                 channel_code=None,
                 gameBalance=None,
                 result=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})
        request_body = {
            "method": "post",
            "url": f"/v1/test/game/transfer/mock/{channel_code}",
            "json": {
                    "url": None,
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
