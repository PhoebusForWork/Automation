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


class user(PLAT_API):

    def getUserList(self,  # 查詢客戶列表
                    platUid=None, platToken=None,
                    From=None, to=None,
                    minBalance=None, maxBalance=None,
                    status=None, vipId=None, groupId=None,
                    isRegisterTime=None, searchType=None,
                    keyword=None, page=None, size=None,
                    isOnline=None, isWhiteList=None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user",
                               json={},
                               params={
                                   "from": From, "to": to,
                                   "minBalance": minBalance, "maxBalance": maxBalance,
                                   "status": status, "vipId": vipId, "groupId": groupId,
                                   "isRegisterTime": isRegisterTime, "searchType": searchType,
                                   "keyword": keyword, "page": page, "size": size,
                                   "isOnline": isOnline, "isWhiteList": isWhiteList,
                               }
                               )
        self._printresponse(response)
        return response.json()

    def userParams(self,  # 客戶列表查詢條件
                   platUid=None, platToken=None,
                   ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/params",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def getUserInfo(self,  # 查詢客戶資訊
                    platUid=None, platToken=None,
                    userId=None
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/{}".format(userId),
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def getUserAmount(self,  # 查詢客戶財務資訊
                      platUid=None, platToken=None,
                      userId=None
                      ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/{}/account".format(userId),
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def userRemark(self,  # 更新客戶備註(不需審核)
                   platUid=None, platToken=None,
                   userId=None, remark=None,
                   ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/user/{}/remark".format(userId),
                               json={
            "remark": remark,
        },
            params={}
        )
        self._printresponse(response)
        return response.json()

    def userReallyName(self,  # 更新客戶真實姓名(不需審核)
                       platUid=None, platToken=None,
                       userId=None, reallyName=None,
                       ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/user/{}/reallyName".format(userId),
                               json={
            "reallyName": reallyName,
        },
            params={}
        )
        self._printresponse(response)
        return response.json()

    def setWhiteList(self,  # 設置客戶撞庫白名單
                     platUid=None, platToken=None,
                     userId=None, isWhiteList=None,
                     ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/user/{}/isWhiteList".format(userId),
                               json={},
                               params={
            "isWhiteList": isWhiteList,
        }
        )
        self._printresponse(response)
        return response.json()

    def userConvertProxy(self,  # 開通代理角色
                         platUid=None, platToken=None,
                         userId=None,
                         ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/user/convertProxy",
                               json={
                                   "userId": userId,
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def usernameValidate(self,  # 校驗會員帳號是否存在
                         platUid=None, platToken=None,
                         usernames=None,
                         ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/user/username/validate",
                                json={
                                    "usernames": usernames
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def userLockStatus(self,  # 申請鎖定 lockStatus(鎖定類別) LOGIN：登入, RECHARGE：充值, WITHDRAW：提領, TRANSFER：轉帳
                       platUid=None, platToken=None,
                       userIds=None, lockStatus=None, isLock=None,
                       remark=None,
                       ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/user/lockStatus",
                                json={
                                    "userIds": userIds,
                                    "userLockTypeList": [
                                        {
                                            "lockStatus": lockStatus,
                                            "isLock": isLock,
                                        }
                                    ],
                                    "remark": remark,
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def editUserVip(self,  # 修改客戶VIP層級
                    platUid=None, platToken=None,
                    userId=None, vipId=None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/userVip/{}".format(userId),
                               json={},
                               params={
            "userId": userId,
            "vipId": vipId,
        }
        )
        self._printresponse(response)
        return response.json()

    def getUserVipInfo(self,  # 查詢客戶VIP層級
                       platUid=None, platToken=None,
                       userName=None,
                       ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/userVip",
                               json={},
                               params={
                                   "userName": userName,
                               }
                               )
        self._printresponse(response)
        return response.json()


# --------------------------------------------------------------------------------------------


    def riskAnalysisSameIp(self,  # 風險套利重複ip
                           platUid=None, platToken=None,
                           userId=None, page=None, size=None,
                           ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/{}/risk/analysis/same/ip".format(userId),
                               json={},
                               params={
            "page": page,
            "size": size,
        }
        )
        self._printresponse(response)
        return response.json()

    def riskAnalysisSameIp(self,  # 風險套利重複ip
                           platUid=None, platToken=None,
                           id=None, page=None, size=None,
                           ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/{}/risk/analysis/same/ip".format(id),
                               json={},
                               params={
            "page": page,
            "size": size,
        }
        )
        self._printresponse(response)
        return response.json()

    def riskAnalysisArbitrage(self,  # 風險套利分析查詢
                              platUid=None, platToken=None,
                              id=None, registeredFrom=None, registeredTo=None,
                              username=None, userType=None, reallyName=None,
                              page=None, size=None,
                              ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/{}/risk/analysis/arbitrage".format(id),
                               json={},
                               params={
            "registeredFrom": registeredFrom, "registeredTo": registeredTo,
            "username": username, "userType": userType, "reallyName": reallyName,
            "page": page,
            "size": size,
        }
        )
        self._printresponse(response)
        return response.json()

    def loginInfo(self,  # 登入日誌
                  platUid=None, platToken=None,
                  id=None,
                  loginInStartTime='2022-01-01T00:00:00Z',
                  loginInEndTime='2022-12-31T23:59:59Z',
                  type=None, keyword=None, osType=None,
                  page=None, size=None,
                  ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/{}/login/info".format(id),
                               json={},
                               params={
            "loginInStartTime": loginInStartTime,
            "loginInEndTime": loginInEndTime,
            "type": type, "keyword": keyword, "osType": osType,
            "page": page, "size": size,
        }
        )
        self._printresponse(response)
        return response.json()

    def loginStat(self,  # 客戶登入統計
                  platUid=None, platToken=None,
                  userId=None,
                  ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/login/stat/{}".format(userId),
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()
