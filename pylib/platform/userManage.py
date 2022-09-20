# -*- coding: utf-8 -*-

import json,jsonpath
from bs4 import PageElement

from itsdangerous import NoneAlgorithm
from ..platform.platApiBase import PLAT_API #執行RF時使用
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini') #在rf_api_test層執行時使用
web_host = config['host']['web_host']
platfrom_host = config['host']['platfrom_host']

class userManage(PLAT_API):

    def getUserManageList(self,     #查詢審批列表
                    platUid = None,platToken = None,
                    approveTimeType = 0,
                    From = "2022-01-01T00:00:00Z", to="2022-12-31T23:59:59Z",
                    username = None,userType = None,
                    optType = None,creator = None,
                    firstApprover = None,secondApprover = None,
                    status = None,page = None,size = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/manage",
                                json = {},
                                params = {
                                    "from" : From, "to":to,
                                    "status":status,"page":page,"size":size,
                                    "approveTimeType":approveTimeType,"username":username,
                                    "userType":userType,"optType":optType,"creator":creator,
                                    "firstApprover":firstApprover,"secondApprover":secondApprover,
                                }
        )
        self._printresponse(response)
        return response.json()

    def getUserManageQueryParams(self,     #查詢審批參數
                    platUid = None,platToken = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/manage/query/params",
                                json = {},
                                params = {},
        )
        self._printresponse(response)
        return response.json()

    def getUserManageLog(self,     #後台操作記錄
                    platUid = None,platToken = None,
                    userId = None,From = None, to=None,
                    optType = None,creator = None,
                    page = None,size = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/manage/log/{}".format(userId),
                                json = {},
                                params = {
                                    "from":From,"to":to,
                                    "optType":optType,"creator":creator,
                                    "page":page,"size":size,
                                },
        )
        self._printresponse(response)
        return response.json()

    def firstApproval(self,     #一審 審核狀態 1:核准 / 2:駁回
                    platUid = None,platToken = None,
                    id = None,status = None,remark = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/user/manage/{}/first/approval".format(id),
                                json = {
                                        "status": status,
                                        "remark": remark,
                                        },
                                params = {},
        )
        self._printresponse(response)
        return response.json()

    def secondApproval(self,     #二審 第二審批狀態 4:核准 / 5:駁回
                    platUid = None,platToken = None,
                    id = None,status = None,remark = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/user/manage/{}/second/approval".format(id),
                                json = {
                                        "status": status,
                                        "remark": remark,
                                        },
                                params = {},
        )
        self._printresponse(response)
        return response.json()

    def userManageParent(self,     #修改上級代理
                    platUid = None,platToken = None,
                    userId = None,parentUsername = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/user/manage/parent",
                                json = {
                                        "userId": userId,
                                        "parentUsername": parentUsername,
                                        },
                                params = {},
        )
        self._printresponse(response)
        return response.json()

    def userManageContact(self,     #編輯會員聯絡資料
                    platUid = None,platToken = None,
                    userId = None,telephone = None,
                    email = None,birthday = None,
                    remark = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/user/manage/parent",
                                json = {
                                        "userId": userId,
                                        "telephone": telephone,
                                        "email": email,
                                        "birthday": birthday,
                                        "remark": remark,
                                        },
                                params = {},
        )
        self._printresponse(response)
        return response.json()

    def cleanApproval(self,     #編輯會員聯絡資料
                    platToken = None,optType = None
                    ):
        if platToken != None:
            self.ps.headers.update({"token":str(platToken)})
        jsdata = self.getUserManageList(optType=optType,size=100,status=0)
        ret = jsonpath.jsonpath(jsdata,"$..id")
        if ret == False:
            pass
        else:
            for i in ret:
                self.firstApproval(id = i,status=2,remark="auto_rej")
        