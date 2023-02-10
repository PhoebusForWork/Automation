# -*- coding: utf-8 -*-
from ..platform.platApiBase import PLAT_API
from utils.data_utils import EnvReader

env = EnvReader()
platform_host = env.PLATFORM_HOST


class platform(PLAT_API):

    def getPltInfo(self,  # 搜索帳號列表
                   plat_token=None,
                   ):
        if plat_token != None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/platform",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()
