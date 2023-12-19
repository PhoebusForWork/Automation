# -*- coding: utf-8 -*-
import jsonpath
from ..client_side.webApiBase import WebAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader
from utils.generate_utils import Make

env = EnvReader()
web_host = env.WEB_HOST


class Activity(WebAPI):
    # 活動類型列表
    def get_activity_category(self):
        request_body = {
            "method": "get",
            "url": "/v1/activity/category",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 參加活動
    def join_activity_1(self):
        request_body = {
            "method": "post",
            "url": "/v1/activity/first-recharge/join",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 參加活動
    def join_activity(self, code=None, timeType=0 ):
        request_body = {
            "method": "post",
            "url": "/v1/activity/join",
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 參加活動狀態
    def get_join_activity_status(self):
        request_body = {
            "method": "get",
            "url": "/v1/activity/join/status",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 活動列表
    def get_activity_list(self):
        request_body = {
            "method": "post",
            "url": "/v1/activity/list",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 推薦活動列表
    def get_recommend_list(self):
        request_body = {
            "method": "get",
            "url": "/v1/activity/recommend/list",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 活動獎勵列表
    def find_rewards(self):
        request_body = {
            "method": "get",
            "url": "/v1/activity/reward/list",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 一鍵領獎
    def claim_all(self):
        request_body = {
            "method": "post",
            "url": "/v1/activity/reward/orders/claim",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 領獎
    def claim_reward(self):
        request_body = {
            "method": "post",
            "url": "/v1/activity/reward/orders/{orderId}/claim",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 針對活動已符合領取資格的會員，跳出彈窗提醒用戶有未領取的彩金
    def get_unclaimed_reward_list(self):
        request_body = {
            "method": "get",
            "url": "/v1/activity/reward/unclaimed/list",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()
