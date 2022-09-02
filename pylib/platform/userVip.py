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

class userVip(PLAT_API):

    def addVIP(self,     #新增VIP層級
                    platUid = None,platToken = None,
                    name = None, regStartTime = None,
                    regEndTime = None,rechargeTotal = None,
                    betTotal = None,levelGift = None,
                    birthdayGift = None,festivalGift = None,
                    redEnvelop = None,limitBet = None,
                    limitRecharge = None,isVip = None,
                    remark = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/user/vip/config",
                                json = {
                                    "name" : name, 
                                    "regStartTime" : regStartTime,
                                    "regEndTime" : regEndTime,
                                    "rechargeTotal" : rechargeTotal,
                                    "betTotal" : betTotal,
                                    "levelGift" : levelGift,
                                    "birthdayGift" : birthdayGift,
                                    "festivalGift" : festivalGift,
                                    "redEnvelop" : redEnvelop,
                                    "limitBet" : limitBet,
                                    "limitRecharge" : limitRecharge,
                                    "isVip" : isVip,
                                    "remark" : remark,
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editVIP(self,     #編輯VIP層級
                    platUid = None,platToken = None,
                    vipId = None,
                    name = None, regStartTime = None,
                    regEndTime = None,rechargeTotal = None,
                    betTotal = None,levelGift = None,
                    birthdayGift = None,festivalGift = None,
                    redEnvelop = None,limitBet = None,
                    limitRecharge = None,isVip = None,
                    remark = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/user/vip/config/{}".format(vipId),
                                json = {
                                    "name" : name, 
                                    "regStartTime" : regStartTime,
                                    "regEndTime" : regEndTime,
                                    "rechargeTotal" : rechargeTotal,
                                    "betTotal" : betTotal,
                                    "levelGift" : levelGift,
                                    "birthdayGift" : birthdayGift,
                                    "festivalGift" : festivalGift,
                                    "redEnvelop" : redEnvelop,
                                    "limitBet" : limitBet,
                                    "limitRecharge" : limitRecharge,
                                    "isVip" : isVip,
                                    "remark" : remark,
                                },
                                params = {
                                    "vipId" : vipId,
                                }
        )
        self._printresponse(response)
        return response.json()

    def editVipOnly(self,     #編輯VIP專享
                    platUid = None,platToken = None,
                    vipId = None,
                    isVip = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/user/vip/config/{}/isVip".format(vipId),
                                json = {},
                                params = {
                                    "vipId" : vipId,
                                    "isVip" : isVip,
                                }
        )
        self._printresponse(response)
        return response.json()
    
    def getVipInfo(self,     #獲取VIP配置
                    platUid = None,platToken = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/vip/config",
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getVipList(self,     #獲取VIP列表
                    platUid = None,platToken = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/user/vip/config/mapList",
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()