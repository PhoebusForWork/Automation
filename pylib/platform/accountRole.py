# -*- coding: utf-8 -*-

import json
from bs4 import PageElement

from itsdangerous import NoneAlgorithm
from ..platform.platApiBase import PLAT_API #執行RF時使用
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini') #在rf_api_test層執行時使用
web_host = config['host']['web_host']
platfrom_host = config['host']['platfrom_host']

class accountRole(PLAT_API):

    def roleList(self,     #角色列表
                    platUid = None,platToken = None,
                    role = None,authorityId = None,
                    departmentId = None,
                    page = None,size = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/role/list",
                                json = {},
                                params = {
                                    "role" : role,
                                    "authorityId" : authorityId,
                                    "departmentId" : departmentId,
                                    "page" : page,
                                    "size" : size,
                                }
        )
        self._printresponse(response)
        return response.json()

    def addRole(self,     #創建角色
                    platUid = None,platToken = None,
                    role = None,remark = None,
                    authorityIds = None,
                    departmentIds = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/account/role",
                                json = {
                                    "role" : role,
                                    "remark" : remark,
                                    "authorityIds" : authorityIds,
                                    "departmentIds" : departmentIds,
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editRole(self,     #編輯角色
                    platUid = None,platToken = None,
                    roleId = None,
                    role = None,remark = None,
                    authorityIds = None,
                    departmentIds = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/role/{}".format(roleId),
                                json = {
                                    "role" : role,
                                    "remark" : remark,
                                    "authorityIds" : authorityIds,
                                    "departmentIds" : departmentIds,
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def roleStatus(self,     #角色狀態
                    platUid = None,platToken = None,
                    roleId = None,
                    status = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/role/{}/status".format(roleId),
                                json = {
                                    "status" : status,
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def roleAuthorities(self,     #顯示角色權限
                    platUid = None,platToken = None,
                    roleId = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/role/{}/authorities".format(roleId),
                                json = {},
                                params = {
                                    "roleId" : roleId,
                                }
        )
        self._printresponse(response)
        return response.json()