# -*- coding: utf-8 -*-

import json

from itsdangerous import NoneAlgorithm
from ..platform.platApiBase import PLAT_API #執行RF時使用
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini') #在rf_api_test層執行時使用
web_host = config['host']['web_host']
platfrom_host = config['host']['platfrom_host']

class platform(PLAT_API):

    def getPltInfo(self,     #搜索帳號列表
                    platUid = None,platToken = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/platform",
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()