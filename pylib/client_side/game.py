# -*- coding: utf-8 -*-
import configparser
from ..client_side.webApiBase import WEB_API  # 執行RF時使用


config = configparser.ConfigParser()
config.read('config/config.ini')
web_host = config['host']['web_host']
platfrom_host = config['host']['platform_host']


class Game(WEB_API):

    def get_game_list(self, web_token=None,
                      ignoreGameIds=[], os_type="WEB"  # (WEB/H5/ANDROID/IOS)
                      ):  # 遊戲列表
        if web_token is not None:
            self.ws.headers.update({"token": str(web_token)})
        response = self.ws.get(web_host+"/v1/game/list",
                               json={},
                               params={"ignoreGameIds": ignoreGameIds,
                                       "os-type": os_type}
                               )
        self._printresponse(response)
        return response.json()

    def get_game_usual(self, web_token=None,
                       ):  # 常用遊戲列表
        if web_token is not None:
            self.ws.headers.update({"token": str(web_token)})
        response = self.ws.get(web_host+"/v1/game/usual",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def game_redirect(self, web_token=None,
                      gameCode='AWC_LIVE_SEXY', backUrl="https://tttint.onlinegames22.com/wallet/login", subGameCode=None, os_type="", token=None
                      ):  # 遊戲跳轉
        if web_token is not None:
            self.ws.headers.update({"token": str(web_token)})
        response = self.ws.get(web_host+"/v1/game/redirect/{}/url".format(gameCode),
                               json={},
                               params={"gameCode": gameCode, "backUrl": backUrl,
                                       "subGameCode": subGameCode, "os-type": os_type, "token": token}
                               )
        self._printresponse(response)
        return response.json()


class GameOrder(WEB_API):

    def get_game_order(self, web_token=None,
                       orderType=2, gameCode=None,
                       settleStatus=None,
                       startTime="2022-10-17T00:00:00Z", endTime="2022-10-17T23:59:59Z",
                       page=None, size=None
                       ):  # 查詢注單
        if web_token is not None:
            self.ws.headers.update({"token": str(web_token)})
        response = self.ws.get(web_host+"/v1/game/order",
                               json={},
                               params={
                                   "orderType": orderType,
                                   "gameCode": gameCode,
                                   "settleStatus": settleStatus,
                                   "startTime": startTime,
                                   "endTime": endTime,
                                   "page": page,
                                   "size": size,
                               }
                               )
        self._printresponse(response)
        return response.json()

    def get_game_order_summary(self, web_token=None,
                               orderType=2, gameCode=None,
                               settleStatus=None,
                               startTime="2022-10-17T00:00:00+08:00", endTime="2022-10-17T23:59:59+08:00",
                               ):  # 注單總和查詢
        if web_token is not None:
            self.ws.headers.update({"token": str(web_token)})
        response = self.ws.get(web_host+"/v1/game/order/summary",
                               json={},
                               params={
                                   "orderType": orderType,
                                   "gameCode": gameCode,
                                   "settleStatus": settleStatus,
                                   "startTime": startTime,
                                   "endTime": endTime,
                               }
                               )
        self._printresponse(response)
        return response.json()