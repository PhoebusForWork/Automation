# -*- coding: utf-8 -*-
import configparser
from ..website.webApiBase import WEB_API  # 執行RF時使用


config = configparser.ConfigParser()
config.read('config/config.ini')
web_host = config['host']['web_host']
platfrom_host = config['host']['platform_host']


class Wallet(WEB_API):

    def get_wallet_user_info(self, userId=25, webToken=None,
                             ):  # 顯示中心錢包及各遊戲錢包金額和渠道狀態
        if webToken is not None:
            self.ws.headers.update({"token": str(webToken)})
        response = self.ws.get(web_host+"/v1/wallet/game/transfer/user/{}/info".format(userId),
                               json={}
                               )
        self._printresponse(response)
        return response.json()

    def wallet_game_transfer_withdraw(self, webToken=None, userId=25, channelCode=None, amount=None
                                      ):  # 從指定遊戲渠道轉錢回中心錢包
        if webToken is not None:
            self.ws.headers.update({"token": str(webToken)})
        response = self.ws.post(web_host+"/v1/wallet/game/transfer/user/{}/withdraw".format(userId),
                                json={
                                    "channelCode": channelCode,
                                    "amount": amount
        }
        )
        self._printresponse(response)
        return response.json()

    def wallet_game_transfer_withdraw_all(self, webToken=None, userId=25,
                                          ):  # 一鍵回收
        if webToken is not None:
            self.ws.headers.update({"token": str(webToken)})
        response = self.ws.post(web_host+"/v1/wallet/game/transfer/user/{}/withdraw/all".format(userId),
                                json={}
                                )
        self._printresponse(response)
        return response.json()

    def wallet_game_transfer_deposit(self, webToken=None, userId=25, channelCode=None, amount=None
                                     ):  # 將錢轉出至遊戲渠道
        if webToken is not None:
            self.ws.headers.update({"token": str(webToken)})
        response = self.ws.post(web_host+"/v1/wallet/game/transfer/user/{}/deposit".format(userId),
                                json={
                                    "channelCode": channelCode,
                                    "amount": amount
        }
        )
        self._printresponse(response)
        return response.json()

    def get_wallet_front_user_fund(self, userId=25, webToken=None,
                                   ):  # 取得使用者資金明細
        if webToken is not None:
            self.ws.headers.update({"token": str(webToken)})
        response = self.ws.get(web_host+"/v1/wallet/front/user/{}/fund".format(userId),
                               json={},
                               params={
            "from": "2022-10-01T00:00:00Z", "to": "2023-10-07T00:00:00Z"}
        )
        self._printresponse(response)
        return response.json()
