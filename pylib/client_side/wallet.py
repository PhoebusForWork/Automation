# -*- coding: utf-8 -*-
import configparser
import os
from ..client_side.webApiBase import WEB_API  # 執行RF時使用


if os.getenv('MODE') is None:
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    web_host = config['host']['web_host']
else:
    web_host = os.getenv('WEB_HOST')


class Wallet(WEB_API):

    def get_wallet_user_info(self, userId=25, web_token=None,
                             ):  # 顯示中心錢包及各遊戲錢包金額和渠道狀態
        if web_token is not None:
            self.ws.headers.update({"token": str(web_token)})
        response = self.ws.get(web_host+"/v1/wallet/game/transfer/user/info",
                               json={}
                               )
        self._printresponse(response)
        return response.json()

    def wallet_game_transfer_withdraw(self, web_token=None, channelCode=None, amount=None
                                      ):  # 從指定遊戲渠道轉錢回中心錢包
        if web_token is not None:
            self.ws.headers.update({"token": str(web_token)})
        response = self.ws.post(web_host+"/v1/wallet/game/transfer/user/withdraw",
                                json={
                                    "channelCode": channelCode,
                                    "amount": amount
                                }
                                )
        self._printresponse(response)
        return response.json()

    def wallet_game_transfer_withdraw_all(self, web_token=None
                                          ):  # 一鍵回收
        if web_token is not None:
            self.ws.headers.update({"token": str(web_token)})
        response = self.ws.post(web_host+"/v1/wallet/game/transfer/user/withdraw/all",
                                json={}
                                )
        self._printresponse(response)
        return response.json()

    def wallet_game_transfer_deposit(self, web_token=None, channelCode=None, amount=None
                                     ):  # 將錢轉出至遊戲渠道
        if web_token is not None:
            self.ws.headers.update({"token": str(web_token)})
        response = self.ws.post(web_host+"/v1/wallet/game/transfer/user/deposit",
                                json={
                                    "channelCode": channelCode,
                                    "amount": amount
                                }
                                )
        self._printresponse(response)
        return response.json()

    def get_wallet_front_user_fund(self, web_token=None,
                                   ):  # 取得使用者資金明細
        if web_token is not None:
            self.ws.headers.update({"token": str(web_token)})
        response = self.ws.get(web_host+"/v1/wallet/front/user/fund",
                               json={},
                               params={
                                   "from": "2022-10-01T00:00:00Z", "to": "2023-10-07T00:00:00Z"}
                               )
        self._printresponse(response)
        return response.json()
