# -*- coding: utf-8 -*-

import jsonpath,random,string

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

    def getAvailableChannel_auto(self,     #獲取未綁定代理渠道
                    platUid = None,platToken = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/channel/available",
                                json = {},
                                params = {}
        )
        ret = jsonpath.jsonpath(response.json(),"$..data[0].id")
        print(ret)
        if ret != False :
            return ret[0]
        else:
            self.addChannel(platToken,channel=''.join(random.choice(string.ascii_letters) for x in range(10)))
            response = self.ps.get(platfrom_host+"/v1/proxy/channel/available",json = {},params = {})
            ret = jsonpath.jsonpath(response.json(),"$..data[0].id")
            # self._printresponse(ret)
            return ret[0]
        

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

    def getExistGroup_auto(self,     #取得存在團隊id
                    platUid = None,platToken = None,
                    page = None,size = 1000,
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
        ret = jsonpath.jsonpath(response.json(),"$..records[(@.length-1)].id")
        self._printresponse(response)
        return ret[0]

class proxyCommission(PLAT_API):

    def addTemplate(self,     # 建立佣金模板
                    platToken = None,
                    name = None,isEnabled = None,
                    isNeedToVerify = None
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/proxy/commission/template",
                                json = {
                                    "name" : name, 
                                    "isEnabled" : isEnabled,
                                    "isNeedToVerify" : isNeedToVerify
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editTemplate(self,     # 編輯佣金模板
                    platToken = None,
                    id = 1,
                    name = None,isEnabled = None,
                    isNeedToVerify = None
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/commission/template/{}".format(id),
                                json = {
                                    "name" : name, 
                                    "isEnabled" : isEnabled,
                                    "isNeedToVerify" : isNeedToVerify
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getTemplate(self,     # 獲取佣金模板
                    platToken = None
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/commission/template",
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getTemplateList(self,     # 獲取佣金模板選單
                    platToken = None
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/commission/template/mapList",
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getSubConfig(self,     # 獲取下級代理佣金設置
                    platToken = None,
                    id = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/commission/template/{}/subCommissionConfig".format(id),
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()
        
    def editSubConfig(self,     # 編輯下級代理佣金設置
                    platToken = None,
                    id = None,
                    subCommissionConfigList = None,
                    subSubCommissionConfigList = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/commission/template/{}/subCommissionConfig".format(id),
                                json = {
                                    "subCommissionConfigList" : [subCommissionConfigList],
                                    "subSubCommissionConfigList" : [subSubCommissionConfigList],
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getSettlementShares(self,     # 獲取結算分攤
                    platToken = None,
                    id = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/commission/template/{}/settlementShares".format(id),
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editSettlementShares(self,     # 編輯結算分攤
                    platToken = None,
                    id = None,activity = None,
                    activityLimit = None,rebate = None,
                    rebateLimit = None,bet = None,betCount = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/commission/template/{}/settlementShares".format(id),
                                json = {
                                        "activity": activity,
                                        "activityLimit": activityLimit,
                                        "rebate": rebate,
                                        "rebateLimit": rebateLimit,
                                        "bet": bet,
                                        "betCount": betCount
                                        },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getPlatSettlementShares(self,     # 獲取平台費分攤
                    platToken = None,
                    id = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/commission/template/{}/platformFeeShares".format(id),
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editPlatSettlementShares(self,     # 編輯平台費分攤
                    platToken = None,
                    id = None,channelCode = None,
                    gameType = None,fee = None,
                    platformFeeLimit = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/commission/template/{}/platformFeeShares".format(id),
                                json = [
                                        {
                                            "channelCode": channelCode,
                                            "platformFee": [{
                                                "gameType": gameType,
                                                "fee": fee
                                            }],
                                            "platformFeeLimit": platformFeeLimit
                                        }
                                        ],
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getCommissionConfig(self,     # 獲取設置返佣
                    platToken = None,
                    id = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/commission/template/{}/commissionConfig".format(id),
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editCommissionConfig(self,     # 獲取設置返佣
                    platToken = None,
                    id = None,profit = None,
                    commissionLimit = None,commission = None,
                    validUserCount = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/commission/template/{}/commissionConfig".format(id),
                                json = [
                                        {
                                            "profit": profit,
                                            "commissionLimit": commissionLimit,
                                            "commission": commission,
                                            "validUserCount": validUserCount
                                        }
                                        ],
                                params = {}
        )
        self._printresponse(response)
        return response.json()

class  proxy(PLAT_API):

    def getProxy(self,     # 獲取代理列表
                    platToken = None,
                    registerFrom = "2022-01-01T00:00:00Z",registerTo = "2022-12-31T00:00:00Z",
                    minBalance = None,maxBalance = None,
                    creditStatus = None,queryType = None,
                    input = None,groupName = None,
                    channel = None,page = None,size = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy",
                                json = {},
                                params = {
                                    "registerFrom" : registerFrom,
                                    "registerTo" : registerTo,
                                    "minBalance" : minBalance,
                                    "maxBalance" : maxBalance,
                                    "creditStatus" : creditStatus,
                                    "queryType" : queryType,
                                    "input" : input,
                                    "groupName" : groupName,
                                    "channel" : channel,
                                    "page" : page,
                                    "size" : size,
                                }
        )
        self._printresponse(response)
        return response.json()

    def accountValidate(self,     # 校驗代理帳號
                    platToken = None,
                    accounts = []
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/proxy/account/validate",
                                json = {
                                        "accounts" : accounts,
                                        },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def addProxy(self,     # 創建代理
                    platToken = None,
                    proxyAccount = None,
                    proxyName = None,password = None,
                    telephone = None,proxyChannelId = None,
                    commissionId = None,registerIp = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/proxy",
                                json = {
                                        "proxyAccount": proxyAccount,
                                        "proxyName": proxyName,
                                        "password": password,
                                        "telephone": telephone,
                                        "proxyChannelId": proxyChannelId,
                                        "commissionId": commissionId,
                                        "registerIp": registerIp
                                        },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editsubCount(self,     #修改子代理上限
                    platToken = None,
                    proxyId = None,
                    subCount = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/{}/subCount".format(proxyId),
                                json = {
                                        "subCount": subCount
                                        },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editsubCommission(self,     #申請佣金模式變更
                    platToken = None,
                    proxyId = None,
                    commissionId = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/{}/commission".format(proxyId),
                                json = {
                                        "commissionId": commissionId
                                        },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editChannel(self,     #編輯代理渠道
                    platToken = None,
                    proxyId = None,
                    channelId = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/{}/channel".format(proxyId),
                                json = {
                                        "channelId": channelId
                                        },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getDetailEdit(self,     #查詢代理列表編輯資訊
                    platToken = None,
                    userId = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/{}/detail/edit".format(userId),
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getDetailDisplay(self,     #查詢代理列表顯示資訊
                    platToken = None,
                    userId = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/{}/detail/display".format(userId),
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getCommissionAvg(self,     #查詢三個月平均佣金
                    platToken = None,
                    proxyId = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/{}/commission/avg".format(proxyId),
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def getTradeInfo(self,     #查詢交易信息
                    platToken = None,
                    userId = None,
                    tradeTypes = None, # 交易类型: 1會員上分(充值額度)|2代理佣金提現|3代理紅利|4代理充值補分(充值上分額度)|5代理充值減分|6代理加幣|7代理減幣|8加幣-代理佣金|9加幣-代理獎金|10減幣-代理佣金|11減幣-代理獎金|12佣金|13充值|14提現|15調整紅利額度|16調整公司額度
                    From = None,to = None,
                    page = None,size = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/tradeInfo",
                                json = {},
                                params = {
                                    "userId" : userId,
                                    "tradeTypes" : tradeTypes,
                                    "from" : From,"to" : to,
                                    "page" : page,"size" : size,
                                }
        )
        self._printresponse(response)
        return response.json()

    def getDomainQuery(self,     #搜尋代理域名
                    platToken = None,
                    type = None,accountOrName = None,
                    commissionId = None,page = None,size = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/domain/query",
                                json = {},
                                params = {
                                    "type" : type,
                                    "accountOrName" : accountOrName,
                                    "commissionId" : commissionId,
                                    "page" : page,
                                    "size" : None,
                                }
        )
        self._printresponse(response)
        return response.json()

class  proxyManage(PLAT_API):

    def getManageList(self,     # 獲取代理審核列表
                    platToken = None,
                    registerStartTime = "2022-01-01T00:00:00Z",registerEndTime = "2022-12-31T23:59:59Z",
                    proxyAccount = None,proxyName = None,
                    approver = None,proxyManageStatus = None,#代理狀態 0:待審核|1:一審通過|2:一審不通過|3:二審通過|4:二審不通過
                    page = None,size = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/user/manage/list",
                                json = {},
                                params = {
                                    "registerStartTime" : registerStartTime,
                                    "registerEndTime" : registerEndTime,
                                    "proxyAccount" : proxyAccount,
                                    "proxyName" : proxyName,
                                    "approver" : approver,
                                    "proxyManageStatus" : proxyManageStatus,
                                    "page" : page,
                                    "size" : size,
                                }
        )
        self._printresponse(response)
        return response.json()

    def getManageApprover(self,     # 獲取代理審批人列表
                    platToken = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/user/manage/list/approver",
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def approvalFirst(self,     # 代理審批一審
                    platToken = None,
                    id = None,isApprove = None,remark = None
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/user/manage/{}/first/approval".format(id),
                                json = {
                                    "isApprove" : isApprove,
                                    "remark" : remark,
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def approvalSecond(self,     # 代理審批二審
                    platToken = None,
                    id = None,isApprove = None,remark = None
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/user/manage/{}/second/approval".format(id),
                                json = {
                                    "isApprove" : isApprove,
                                    "remark" : remark,
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def cleanProxyApproval(self,token = None,size=100): #批量駁回待審核訂單
        jsdata = self.getManageList(platToken=token,size=size,proxyManageStatus=0)
        jsdata2 = self.getManageList(platToken=token,size=size,proxyManageStatus=1)
        ret = jsonpath.jsonpath(jsdata,"$..id")
        ret2 = jsonpath.jsonpath(jsdata2,"$..id")
        print(ret)
        try:
            for i in ret:
                    self.approvalFirst(platToken=token,id=i,isApprove=False,remark="rej")  
            for i in ret2:
                    self.approvalSecond(platToken=token,id=i,isApprove=False,remark="rej")  
        except:
            pass

    def getFirstApprovalId(self,token=None):
        jsdata = self.getManageList(platToken=token,proxyManageStatus=0)
        ret = jsonpath.jsonpath(jsdata,"$..id")
        if ret == False : 
            add = proxy()
            add.addProxy(platToken=token,proxyAccount="產生訂單號碼"+str(random.randrange(99999)),password="abc123456",telephone=str(random.randrange(10000000000,19999999999)),commissionId=1)
            jsdata = self.getManageList(platToken=token,proxyManageStatus=0)
            ret = jsonpath.jsonpath(jsdata,"$..id")
        return str(ret[0])

    def getSecondApprovalId(self,token=None):
        jsdata = self.getManageList(platToken=token,proxyManageStatus=1)
        ret = jsonpath.jsonpath(jsdata,"$..id")
        if ret == False : 
            add = proxy()
            add.addProxy(platToken=token,proxyAccount="產生訂單號碼"+str(random.randrange(99999)),password="abc123456",telephone=str(random.randrange(10000000000,19999999999)),commissionId=1)
            jsdata = self.getManageList(platToken=token,proxyManageStatus=0)#獲取待一審訂單
            ret = jsonpath.jsonpath(jsdata,"$..id")
            print(ret)
            self.approvalFirst(id=str(ret[0]),isApprove=True,remark="auto_test")
            jsdata = self.getManageList(platToken=token,proxyManageStatus=1)#獲取待二審訂單
            ret = jsonpath.jsonpath(jsdata,"$..id")
        return str(ret[0])

    def getSecondApprovalSuccessId(self,token=None):
        jsdata = self.getManageList(platToken=token,proxyManageStatus=4)
        ret = jsonpath.jsonpath(jsdata,"$..id")
        if ret == False : 
            add = proxy()
            add.addProxy(platToken=token,proxyAccount="產生訂單號碼"+str(random.randrange(99999)),password="abc123456",telephone=str(random.randrange(10000000000,19999999999)),commissionId=1)
            jsdata = self.getManageList(platToken=token,proxyManageStatus=0)#獲取待一審訂單
            ret = jsonpath.jsonpath(jsdata,"$..id")
            self.approvalFirst(id=str(ret[0]),isApprove=True,remark="auto_test")
            jsdata = self.getManageList(platToken=token,proxyManageStatus=1)#獲取待二審訂單
            ret = jsonpath.jsonpath(jsdata,"$..id")
            self.approvalSecond(id=str(ret[0]),isApprove=False,remark="auto_test")
            jsdata = self.getManageList(platToken=token,proxyManageStatus=4)#獲取待二審結束
            ret = jsonpath.jsonpath(jsdata,"$..id")
        return str(ret[0])
        

class  proxyCredit(PLAT_API):

    def getCreditDetail(self,     # 查詢上分紀錄
                    platToken = None,
                    proxyId = None,tradeType = None,
                    startTime = "2022-01-01T00:00:00Z",endTime = "2022-12-31T23:59:59Z",
                    tradeId = None,relationUsername = None,
                    minAmount = None,maxAmount = None,
                    page = None,size = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/proxy/credit/detail",
                                json = {},
                                params = {
                                    "proxyId" : proxyId,
                                    "tradeType" : tradeType,
                                    "startTime" : startTime,
                                    "endTime" : endTime,
                                    "tradeId" : tradeId,
                                    "relationUsername" : relationUsername,
                                    "minAmount" : minAmount,
                                    "maxAmount" : maxAmount,
                                    "page" : page,
                                    "size" : size,
                                }
        )
        self._printresponse(response)
        return response.json()

    def editCredit(self,     # 調整充值額度
                    platToken = None,
                    userId = None,amount = None,
                    changeType = None,status = None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token":str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/proxy/credit",
                                json = {
                                    "userId" : userId,
                                    "amount" : amount,
                                    "changeType" : changeType,
                                    "status" : status,
                                },
                                params = {}
        )
        self._printresponse(response)
        return response.json()