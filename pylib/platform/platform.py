# -*- coding: utf-8 -*-
from ..platform.platApiBase import PlatformAPI
from utils.data_utils import EnvReader

env = EnvReader()
platform_host = env.PLATFORM_HOST


class platform(PlatformAPI):

    def getPltInfo(self,  # 搜索帳號列表
                   plat_token=None,
                   ):
        if plat_token != None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/platform",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()
