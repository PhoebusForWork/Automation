# -*- coding: utf-8 -*-

import json

from itsdangerous import NoneAlgorithm
from ..platform.platApiBase import PLAT_API #執行RF時使用
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini') #在rf_api_test層執行時使用
web_host = config['host']['web_host']
platfrom_host = config['host']['platfrom_host']

class accountAuthority(PLAT_API):

    def authorityList(self,     #權限總列表
                    platUid = None,platToken = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/authority/list",
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def authorityMenu(self,     #選單樹列表
                    platUid = None,platToken = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/authority/menu",
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def authorityPermission(self,     #權限列表
                    platUid = None,platToken = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/authority/permission",
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()