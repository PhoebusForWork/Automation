# -*- coding: utf-8 -*-

import json
from bs4 import PageElement

from itsdangerous import NoneAlgorithm
from ..platform.platApiBase import PLAT_API  # 執行RF時使用
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')  # 在rf_api_test層執行時使用
web_host = config['host']['web_host']
platfrom_host = config['host']['platform_host']


class thirdPartyManage(PLAT_API):

    def getThirdInterface(self,  # 獲取三方接口列表
                          platUid=None, platToken=None,
                          type=None,
                          ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/thirdPartyManage",
                               json={},
                               params={
                                   "type": type,
                               }
                               )
        self._printresponse(response)
        return response.json()

    def editThirdInterface(self,  # 編輯三方接口列表
                           platUid=None, platToken=None,
                           id=None, name=None, template=None,
                           weighting=None, isEnabled=None,
                           ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/thirdPartyManage",
                               json=[{
                                   "id": id,
                                   "name": name,
                                   "template": template,
                                   "weighting": weighting,
                                   "isEnabled": isEnabled,
                               }],
                               params={}
                               )
        self._printresponse(response)
        return response.json()
