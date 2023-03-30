# -*- coding: utf-8 -*-
from pylib.client_side.webApiBase import WebAPI
from utils.data_utils import EnvReader

env = EnvReader()
web_host = env.WEB_HOST


class Config(WebAPI):  # 客戶詳細資料
    # 獲取用戶明細資料
    def get_avatar_urls(self):
        request_body = {
            "method": "get",
            "url": "/v1/config/avatar/urls"
        }

        response = self.send_request(**request_body)
        return response.json()
