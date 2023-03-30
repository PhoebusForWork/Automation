# -*- coding: utf-8 -*-
from ..platform.platApiBase import PlatformAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader

env = EnvReader()
platform_host = env.PLATFORM_HOST


class ThirdPartyManage(PlatformAPI):
    # 獲取三方接口列表
    def get_third_interface(self, plat_token=None, type=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/thirdPartyManage",
            "params": {"type": type}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯三方接口列表
    def edit_third_interface(
            self, plat_token=None, id=None, name=None, template=None,
            weighting=None, isEnabled=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/thirdPartyManage",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()
