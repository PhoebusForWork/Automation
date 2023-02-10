# -*- coding: utf-8 -*-
from ..platform.platApiBase import PLAT_API  # 執行RF時使用
import configparser
import os

if os.getenv('MODE') is None:
    config = configparser.ConfigParser()
    config.read('config/config.ini')  # 在rf_api_test層執行時使用
    platfrom_host = config['host']['platform_host']
else:
    platfrom_host = os.getenv('PLATFORM_HOST')


class platform(PLAT_API):

    def getPltInfo(self,  # 搜索帳號列表
                   plat_token=None,
                   ):
        if plat_token != None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platfrom_host+"/v1/platform",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()
