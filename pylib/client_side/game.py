# -*- coding: utf-8 -*-
from pylib.client_side.webApiBase import WebAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader

env = EnvReader()
web_host = env.WEB_HOST


class Game(WebAPI):
    # 遊戲列表
    def get_game_list(
            self, web_token=None, ignoreGameIds=[],
            os_type="WEB"  # (WEB/H5/ANDROID/IOS)
    ):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "get",
            "url": "/v1/game/list",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 常用遊戲列表
    def get_game_usual(self, web_token=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "get",
            "url": "/v1/game/usual"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 遊戲跳轉
    def game_redirect(
            self, web_token=None, gameCode='AWC_LIVE_SEXY',
            backUrl="https://tttint.onlinegames22.com/wallet/login", subGameCode=None, os_type="", token=None
    ):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/game/redirect/{gameCode}/url",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()


class GameOrder(WebAPI):
    # 查詢注單
    def get_game_order(
            self, web_token=None, orderType=2, gameCode=None, settleStatus=None,
            startTime="2022-10-17T00:00:00Z", endTime="2022-10-17T23:59:59Z", page=None, size=None
    ):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "get",
            "url": "/v1/game/order",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 注單總和查詢
    def get_game_order_summary(
            self, web_token=None, orderType=2, gameCode=None, settleStatus=None,
            startTime="2022-10-17T00:00:00+08:00", endTime="2022-10-17T23:59:59+08:00"
    ):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "get",
            "url": "/v1/game/order/summary",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()
