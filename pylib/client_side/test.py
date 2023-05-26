# -*- coding: utf-8 -*-
from ..client_side.webApiBase import WebAPI
from utils.data_utils import EnvReader


env = EnvReader()
web_host = env.WEB_HOST

# test-controller
class TransferMock(WebAPI):
    # 是否檢核註冊次數
    def set_env(self, is_pro: bool):
        request_body = {
            "method": "put",
            "url": "/v1/test/env/user",
            "params": {"isPro": is_pro}
        }
        response = self.send_request(**request_body)
        return response
