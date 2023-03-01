# -*- coding: utf-8 -*-
from utils.data_utils import EnvReader
from utils.api_utils import API_Controller, KeywordArgument

env = EnvReader()
control_host = env.CONTROL_HOST


class ControlAPI(API_Controller):

    def __init__(self):
        super().__init__(platform='control')

    def get_host_platform_info(self):  # 獲取站點資訊
        response = self.request_session.get(
            self.host + "/v1/host/platform",
            json={},
        )
        self.print_response(response)
        return response.json()

    def add_host_platform(
            self,
            code='vs',
            name='vs',
            language='ZH',
            supportLanguages=["ZH", "EN"],
            currency='CNY',
            supportCurrency=["CNY", "USD", "USDT_TRC20", "USDT_ERC20"],
            timezone=8,
            domains='api30-auto.prj300.xyz',
            status=1,
            sort=1):  # 建立站點
        response = self.request_session.post(
            self.host + "/v1/host/platform",
            json=KeywordArgument.body_data(),
        )
        self.print_response(response)
        return response.json()

    def edit_host_platform(
            self,
            platformId=1,
            code='vs',
            name='vs',
            language='ZH',
            supportLanguages=["ZH", "EN"],
            currency='CNY',
            supportCurrency=["CNY", "USD", "USDT_TRC20", "USDT_ERC20"],
            timezone=8,
            domains='api30-auto.prj300.xyz',
            status=1,
            sort=1):  # 建立站點
        response = self.request_session.put(
            self.host + f"/v1/host/platform/{platformId}",
            json=KeywordArgument.body_data(),
        )
        self.print_response(response)
        return response.json()

    def host_platform_sync_data(self):
        response = self.request_session.get(
            self.host + "/v1/host/platform/syncData",
            json={},
        )
        self.print_response(response)
        return response.json()


if __name__ == "__main__":
    pass
