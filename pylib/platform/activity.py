# -*- coding: utf-8 -*-
import time
import jsonpath
from pylib.platform.platApiBase import PlatformAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader
import jsonpath

env = EnvReader()
platform_host = env.PLATFORM_HOST


class ActivityManagement(PlatformAPI):
    # 取得活動列表
    def get_activity_list(self, name=None, currency="USD"):
        request_body = {
            "method": "post",
            "url": "/v1/activity/list",
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 新增活動
    def add_activity(self):
        request_body = {
            "method": "post",
            "url": "/v1/activity",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 修改活動
    def update_activity(self):
        request_body = {
            "method": "put",
            "url": "/v1/activity",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 活動類型列表
    def get_activity_category(self):
        request_body = {
            "method": "get",
            "url": "/v1/activity/category",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 顯示所有操作者
    def get_activity_list_operator(self):
        request_body = {
            "method": "get",
            "url": "/v1/activity/list/operator",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 活動參賽名單-取消
    def get_activity_participation_cancel(self):
        request_body = {
            "method": "get",
            "url": "/v1/activity/participation/cancel",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 活動參賽名單
    def get_activity_participation_list(self, userName=None):
        request_body = {
            "method": "post",
            "url": "/v1/activity/participation/page",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 新增推薦活動
    def add_recommend_activity(self):
        request_body = {
            "method": "post",
            "url": "/v1/activity/recommend",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 調整推薦活動
    def update_recommend_activity(self):
        request_body = {
            "method": "put",
            "url": "/v1/activity/recommend",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 推薦活動列表
    def get_recommend_list(self, activityId=None, activityName=None):
        request_body = {
            "method": "post",
            "url": "/v1/activity/recommend/list",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 刪除推薦活動
    def delete_recommend_activity(self, activityRecommendId=None):
        request_body = {
            "method": "delete",
            "url": f"/v1/activity/recommend/{activityRecommendId}",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 活動獎勵
    def get_reward_list(self):
        request_body = {
            "method": "post",
            "url": "/v1/activity/reward/list",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 活動下拉選單
    def get_select_activity_list(self):
        request_body = {
            "method": "get",
            "url": "/v1/activity/select",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 修改活動狀態
    def update_activity_status(self):
        request_body = {
            "method": "post",
            "url": "/v1/activity/update/status",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 刪除活動
    def delete_activity(self, id=None):
        request_body = {
            "method": "delete",
            "url": f"/v1/activity/{id}",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 取得單一活動資訊
    def get_activity(self, id=None):
        request_body = {
            "method": "get",
            "url": f"/v1/activity/{id}",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 取得活動ID
    def get_activity_id(self, code=None, name=None, currency="CNY"):
        request_body = {
            "method": "post",
            "url": "/v1/activity/list",
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        activity_id = jsonpath.jsonpath(response.json(), f"$.data.records[?(@.code=='{code}')].id")

        return activity_id[0]

    # 取得推薦活動ID
    def get_recommend_id(self, code=None, activityId=None, activityName=None ):
        activity_id = self.get_activity_id(code=code, name=activityName)
        request_body = {
            "method": "post",
            "url": "/v1/activity/recommend/list",
            "json": {"activityId": activityId, "activityName": activityName}
        }
        response = self.send_request(**request_body)
        recommend_activity_id = jsonpath.jsonpath(response.json(), "$..id")
        return recommend_activity_id[0]
