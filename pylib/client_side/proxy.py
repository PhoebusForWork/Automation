# -*- coding: utf-8 -*-
import jsonpath
from ..client_side.webApiBase import WebAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader


env = EnvReader()
web_host = env.WEB_HOST


# 代理
class Proxy(WebAPI):
    # 判斷代理域名(判斷當前一級域名是否為代理域名並取得代理推廣碼 無需登入)
    def parse_domain(self, origin_url=None):
        self.request_session.headers.update({"Origin_url": origin_url})
        request_body = {
            "method": "get",
            "url": "/v1/proxy/parseDomain"
        }
        response = self.send_request(**request_body)
        return response.json()
