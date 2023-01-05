# -*- coding: utf-8 -*-

import json
import random
import time
from pylib.platform.platApiBase import PLAT_API
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')  # 在rf_api_test層執行時使用
web_host = config['host']['web_host']
platfrom_host = config['host']['platform_host']


class accountAdmin(PLAT_API):

    def searchAdminList(self,  # 搜索帳號列表
                        platUid=None, platToken=None,
                        account=None, displayName=None, phone=None,
                        isLeader=None, deptId=None, status=None,
                        deptIdList=None, roleIdList=None, startLoginTime=None,
                        endLoginTime=None, isNonDept=None,
                        page=None, size=None,
                        ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/admin",
                               json={},
                               params={
                                   "account": account,
                                   "displayName": displayName,
                                   "phone": phone,
                                   "isLeader": isLeader,
                                   "deptId": deptId,
                                   "status": status,
                                   "deptIdList": deptIdList,
                                   "roleIdList": roleIdList,
                                   "startLoginTime": startLoginTime,
                                   "endLoginTime": endLoginTime,
                                   "isNonDept": isNonDept,
                                   "page": page,
                                   "size": size,
                               }
                               )
        self._printresponse(response)
        return response.json()

    def addAdmin(self,  # 新增帳號
                 platUid=None,
                 platToken=None,
                 account=None,
                 password=None,
                 phone=None,
                 sipNum=None,
                 fixSipNum=None,
                 isLeader=None,
                 deptId=None,
                 roleIds=None,
                 expiredTime=None,
                 displayName=None,
                 ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/account/admin",
                                json={
                                    "phone": phone,
                                    "sipNum": sipNum,
                                    "fixSipNum": fixSipNum,
                                    "isLeader": isLeader,
                                    "deptId": deptId,
                                    "roleIds": roleIds,
                                    "expiredTime": expiredTime,
                                    "account": account,
                                    "password": password,
                                    "displayName": displayName
                                },
                                params={}

                                )
        self._printresponse(response)
        return response.json()

    def adminInfo(self,  # 帳號詳情
                  platUid=None,
                  platToken=None,
                  adminId=None,
                  ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/admin/{}".format(adminId),
                               json={},
                               params={
            "adminId": adminId,
        }

        )
        self._printresponse(response)
        return response.json()

    def editAdmin(self,  # 編輯帳號
                  platUid=None,
                  platToken=None,
                  adminId=None,
                  phone=None,
                  sipNum=None,
                  fixSipNum=None,
                  isLeader=None,
                  deptId=None,
                  roleIds=None,
                  expiredTime=None,
                  ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/admin/{}".format(adminId),
                               json={
            "phone": phone,
            "sipNum": sipNum,
            "fixSipNum": fixSipNum,
            "isLeader": isLeader,
            "deptId": deptId,
            "roleIds": roleIds,
            "expiredTime": expiredTime,
        },
            params={
            "adminId": adminId,
        }

        )
        self._printresponse(response)
        return response.json()

    def deleteAdmin(self,  # 刪除帳號
                    platUid=None,
                    platToken=None,
                    adminId=None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.delete(platfrom_host+"/v1/account/admin/{}".format(adminId),
                                  json={},
                                  params={
            "adminId": adminId,
        }
        )
        self._printresponse(response)
        return response.json()

    def adminStatus(self,  # 帳號狀態修改
                    platUid=None,
                    platToken=None,
                    adminId=None,
                    status=None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/admin/{}/status".format(adminId),
                               json={},
                               params={
            "adminId": adminId,
            "status": status,  # 0停用;1啟用;2刪除
        }
        )
        self._printresponse(response)
        return response.json()

    def editPassword(self,  # 修改密碼
                     platUid=None,
                     platToken=None,
                     oldPassword=None,
                     newPassword=None,
                     ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/admin/password",
                               json={
                                   "oldPassword": oldPassword,
                                   "newPassword": newPassword,
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def resetPassword(self,  # 重置密碼
                      platUid=None,
                      platToken=None,
                      adminId=None,
                      ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/admin/{}/resetPassword".format(adminId),
                               json={},
                               params={
            "adminId": adminId,
        }
        )
        self._printresponse(response)
        return response.json()

    def add_account_auto(self, platToken = None):
        now = time.time()
        auto_account = "auto" + str(int(now))
        print(auto_account)
        resp = self.addAdmin(platToken=platToken, account=auto_account, password="abc123456",isLeader=True, deptId='6', roleIds=['5'], displayName=auto_account)

        print(resp)

        if resp["data"] == "success":
            return auto_account
        else:
            raise ValueError("創建帳號失敗")