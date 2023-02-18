# -*- coding: utf-8 -*-
from ..client_side.webApiBase import WebAPI  # 執行RF時使用
from utils.data_utils import EnvReader

env = EnvReader()
web_host = env.WEB_HOST


class Config(WebAPI):  # 客戶詳細資料

    def get_avatar_urls(self):  # 獲取用戶明細資料
        response = self.request_session.get(web_host+"/v1/config/avatar/urls",
                               data={},
                               params={}
                               )
        self.print_response(response)
        return response.json()
