# -*- coding: utf-8 -*-
from ..platform.platApiBase import PLAT_API  # 執行RF時使用
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')
web_host = config['host']['web_host']
platfrom_host = config['host']['platform_host']


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
