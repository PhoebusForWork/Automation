# -*- coding: utf-8 -*-
from utils.data_utils import EnvReader
from utils.api_utils import API_Controller, KeywordArgument

env = EnvReader()
control_host = env.CONTROL_HOST


class ControlAPI(API_Controller):

    def __init__(self):
        super().__init__(platform='control')

    # 獲取站點資訊
    def get_host_platform_info(self):
        request_body = {
            "method": "get",
            "url": "/v1/host/platform"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 建立站點
    def add_host_platform(
            self,
            code='ldpro',
            name='ldpro',
            language='ZH',
            supportLanguages=["ZH", "EN"],
            currency='CNY',
            supportCurrency=["CNY", "USD", "USDT_TRC20", "USDT_ERC20"],
            timezone=8,
            domains='api30-auto.prj300.xyz',
            status=1,
            sort=1
    ):
        request_body = {
            "method": "post",
            "url": "/v1/host/platform",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 建立站點
    def edit_host_platform(
            self,
            platformId=1,
            code='ldpro',
            name='ldpro',
            language='ZH',
            supportLanguages=["ZH", "EN"],
            currency='CNY',
            supportCurrency=["CNY", "USD", "USDT_TRC20", "USDT_ERC20"],
            timezone=8,
            domains='api30-auto.prj300.xyz',
            status=1,
            sort=1
    ):
        request_body = {
            "method": "put",
            "url": f"/v1/host/platform/{platformId}",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    def host_platform_sync_data(self):
        request_body = {
            "method": "get",
            "url": "/v1/host/platform/syncData"
        }

        response = self.send_request(**request_body)
        return response.json()
