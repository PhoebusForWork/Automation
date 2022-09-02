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

class proxyChannel(PLAT_API):

    def addChannel(self,     #新增代理渠道
                    platUid = None,platToken = None,
                    channel = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/proxy/channel",
                                json = {
                                    "channel" : channel, 
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editChannel(self,     #編輯代理渠道
                    platUid = None,platToken = None,
                    channel = None,channelId = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/channel/{}".format(channelId),
                                json = {
                                    "channel" : channel, 
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def deleteChannel(self,     #移除代理渠道
                    platUid = None,platToken = None,
                    channelId = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.delete(platfrom_host+"/v1/proxy/channel/{}".format(channelId),
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getChannel(self,     #顯示代理渠道
                    platUid = None,platToken = None,
                    page = None,size = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/channel",
                                json = {},
                                params = {
                                    "page" : page,
                                    "size" : size,
                                }
        )
        self._printresponse(response)
        return response.json()

    def getChannelAll(self,     #顯示所有代理渠道
                    platUid = None,platToken = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/channel/all",
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()
    
    def getChannelAvailable(self,     #獲取未綁定代理渠道
                    platUid = None,platToken = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/channel/available",
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

class proxyGroup(PLAT_API):

    def addGroup(self,     #新增代理團隊
                    platUid = None,platToken = None,
                    groupName = None,channelIds = [],
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/proxy/group",
                                json = {
                                    "groupName" : groupName, 
                                    "channelIds" : channelIds,
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editGroup(self,     #編輯代理團隊
                    platUid = None,platToken = None,
                    groupName = None,channelIds = [],
                    groupId =None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/group/{}".format(groupId),
                                json = {
                                    "groupName" : groupName, 
                                    "channelIds" : channelIds,
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def deleteGroup(self,     #編輯代理團隊
                    platUid = None,platToken = None,
                    groupId =None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.delete(platfrom_host+"/v1/proxy/group/{}".format(groupId),
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getGroupinfo(self,     #取得團隊資訊
                    platUid = None,platToken = None,
                    page = None,size = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/group/groupsAndChannels",
                                json = {},
                                params = {
                                    "page" : page,
                                    "size" : size,
                                }
        )
        self._printresponse(response)
        return response.json()