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

class accountDept(PLAT_API):

    def deptList(self,     #結點列表
                    platUid = None,platToken = None,
                    roleId = None,departmentStatus = None
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/dept/list",
                                json = {},
                                params = {
                                    "roleId" : roleId,
                                    "departmentStatus" : departmentStatus,
                                }
        )
        self._printresponse(response)
        return response.json()

    def admimList(self,     #人員關係列表
                    platUid = None,
                    platToken = None,
                    account = None,
                    password = None,
                    phone = None,
                    sipNum = None,
                    fixSipNum = None,
                    isLeader = None,
                    deptId = None,
                    status = None,
                    deptIdList = None,
                    roleIdList = None,
                    startLoginTime = None,
                    endLoginTime = None,
                    isNonDept = None,
                    expiredTime = None,
                    displayName = None,
                    page = None,
                    size = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/dept/admin/list",
                                json = {},
                                params = {
                                    "phone": phone,
                                    "sipNum": sipNum,
                                    "fixSipNum": fixSipNum,
                                    "isLeader": isLeader,
                                    "deptId": deptId,
                                    "roleIdList": roleIdList,
                                    "expiredTime": expiredTime,
                                    "account": account,
                                    "password": password,
                                    "displayName": displayName,
                                    "status" : status,
                                    "deptIdList" : deptIdList,
                                    "startLoginTime" : startLoginTime,
                                    "endLoginTime" : endLoginTime,
                                    "isNonDept" : isNonDept,
                                    "page" : page,
                                    "size" : size,
                                }

        )
        self._printresponse(response)
        return response.json()

    def addDept(self,     #新增節點
                    platUid = None,platToken = None,
                    department = None,pid = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/account/dept",
                                json = {
                                    "department" : department,
                                    "pid" : pid,
                                },
                                params = {},
        )
        self._printresponse(response)
        return response.json()

    def editDept(self,     #修改節點
                    platUid = None,platToken = None,
                    departmentId = None,department = None
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/dept/{}".format(departmentId),
                                json = {
                                    "department" : department,
                                },
                                params = {
                                    "departmentId" : departmentId,
                                }
        )
        self._printresponse(response)
        return response.json()

    def deleteDept(self,     #刪除節點
                    platUid = None,platToken = None,
                    departmentId = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.delete(platfrom_host+"/v1/account/dept/{}".format(departmentId),
                                json = {},
                                params = {
                                    "departmentId" : departmentId,
                                }
        )
        self._printresponse(response)
        return response.json()

    def deptLeader(self,     #設置負責人
                    platUid = None,platToken = None,
                    adminId = None,isLeader = None
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/dept/leader",
                                json = {
                                    "adminId" : adminId,
                                    "isLeader" : isLeader,
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def deptAdmin(self,     #關聯已存在帳號
                    platUid = None,platToken = None,
                    adminIdList = None,departmentId = None
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/dept/admin",
                                json = {
                                    "adminIdList" : adminIdList,
                                    "departmentId" : departmentId,
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def deleteDeptAdmin(self,     #解除關聯
                    platUid = None,platToken = None,
                    adminId = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/dept/leader",
                                json = {},
                                params = {
                                    "adminId" : adminId,
                                }
        )
        self._printresponse(response)
        return response.json()
