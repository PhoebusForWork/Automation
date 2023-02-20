# -*- coding: utf-8 -*-

import jsonpath
import random
import string
from ..platform.platApiBase import PlatformAPI  # 執行RF時使用
from utils.data_utils import EnvReader


env = EnvReader()
platform_host = env.PLATFORM_HOST


class ProxyChannel(PlatformAPI):

    def add_channel(self,  # 新增代理渠道
                    plat_token=None,
                    channel=None,
                    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/proxy/channel",
                                json={
                                    "channel": channel,
                                },
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def edit_channel(self,  # 編輯代理渠道
                     plat_token=None,
                     channel=None, channelId=None,
                     ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/proxy/channel/{}".format(channelId),
                               json={
            "channel": channel,
        },
            params={}
        )
        self.print_response(response)
        return response.json()

    def delete_channel(self,  # 移除代理渠道
                       plat_token=None,
                       channelId=None,
                       ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.delete(platform_host+"/v1/proxy/channel/{}".format(channelId),
                                  json={},
                                  params={}
                                  )
        self.print_response(response)
        return response.json()

    def get_channel(self,  # 顯示代理渠道
                    plat_token=None,
                    page=None, size=None,
                    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/channel",
                               json={},
                               params={
                                   "page": page,
                                   "size": size,
                               }
                               )
        self.print_response(response)
        return response.json()

    def get_channel_all(self,  # 顯示所有代理渠道
                        plat_token=None,
                        ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/channel/all",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_channel_available(self,  # 獲取未綁定代理渠道
                              plat_token=None,
                              ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/channel/available",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_available_channel_auto(self,  # 獲取未綁定代理渠道
                                   plat_token=None,
                                   ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/channel/available",
                               json={},
                               params={}
                               )
        ret = jsonpath.jsonpath(response.json(), "$..id")
        if ret is not False:
            return ret[-1]
        else:
            self.add_channel(plat_token, channel=''.join(
                random.choice(string.ascii_letters) for _ in range(10)))
            response = self.request_session.get(
                platform_host+"/v1/proxy/channel/available", json={}, params={})
            ret = jsonpath.jsonpath(response.json(), "$..id")
            # self.print_response(ret)
            return ret[-1]


class ProxyGroup(PlatformAPI):

    def add_group(self,  # 新增代理團隊
                  plat_token=None,
                  groupName=None, channelIds=[],
                  ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/proxy/group",
                                json={
                                    "groupName": groupName,
                                    "channelIds": channelIds,
                                },
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def edit_group(self,  # 編輯代理團隊
                   plat_token=None,
                   groupName=None, channelIds=[],
                   groupId=None,
                   ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/proxy/group/{}".format(groupId),
                               json={
            "groupName": groupName,
            "channelIds": channelIds,
        },
            params={}
        )
        self.print_response(response)
        return response.json()

    def delete_group(self,  # 編輯代理團隊
                     plat_token=None,
                     groupId=None,
                     ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.delete(platform_host+"/v1/proxy/group/{}".format(groupId),
                                  json={},
                                  params={}
                                  )
        self.print_response(response)
        return response.json()

    def get_group_info(self,  # 取得團隊資訊
                       plat_token=None,
                       page=None, size=None,
                       ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/group/groupsAndChannels",
                               json={},
                               params={
                                   "page": page,
                                   "size": size,
                               }
                               )
        self.print_response(response)
        return response.json()

    def get_exist_group_auto(self,  # 取得存在團隊id
                             plat_token=None,
                             page=None, size=1000,
                             ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        response = self.request_session.get(platform_host+"/v1/proxy/group/groupsAndChannels",
                               json={},
                               params={
                                   "page": page,
                                   "size": size,
                               }
                               )
        ret = jsonpath.jsonpath(response.json(), "$..records[(@.length-1)].id")
        self.print_response(response)
        return ret[0]


class ProxyCommissionTemplate(PlatformAPI):

    def add_template(self,     # 建立佣金模板
                     plat_token=None,
                     name=None, isEnabled=None,
                     isNeedToVerify=None
                     ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/proxy/commission/template",
                                json={
                                    "name": name,
                                    "isEnabled": isEnabled,
                                    "isNeedToVerify": isNeedToVerify
                                },
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def edit_template(self,     # 編輯佣金模板
                      plat_token=None,
                      id=1,
                      name=None, isEnabled=None,
                      isNeedToVerify=None
                      ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/proxy/commission/template/{}".format(id),
                               json={
            "name": name,
            "isEnabled": isEnabled,
            "isNeedToVerify": isNeedToVerify
        },
            params={}
        )
        self.print_response(response)
        return response.json()

    def get_template(self,     # 獲取佣金模板
                     plat_token=None
                     ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/commission/template",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_template_list(self,     # 獲取佣金模板選單
                          plat_token=None
                          ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/commission/template/mapList",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_sub_config(self,     # 獲取下級代理佣金設置
                       plat_token=None,
                       id=None,
                       ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+f"/v1/proxy/commission/template/{id}/subCommissionConfig",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def edit_sub_config(self,     # 編輯下級代理佣金設置
                        plat_token=None,
                        id=None,
                        subCommissionConfigList=None,
                        subSubCommissionConfigList=None,
                        ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+f"/v1/proxy/commission/template/{id}/subCommissionConfig",
                               json={
                                   "subCommissionConfigList": subCommissionConfigList,
                                   "subSubCommissionConfigList": subSubCommissionConfigList,
                               },
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_settlement_shares(self,     # 獲取結算分攤
                              plat_token=None,
                              id=None,
                              ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+f"/v1/proxy/commission/template/{id}/settlementShares",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def edit_settlement_shares(self,     # 編輯結算分攤
                               plat_token=None,
                               id=None, activity=None,
                               activityLimit=None, rebate=None,
                               rebateLimit=None, bet=None, betCount=None,
                               ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+f"/v1/proxy/commission/template/{id}/settlementShares",
                               json={
                                   "activity": activity,
                                   "activityLimit": activityLimit,
                                   "rebate": rebate,
                                   "rebateLimit": rebateLimit,
                                   "bet": bet,
                                   "betCount": betCount
                               },
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_plat_settlement_shares(self,     # 獲取平台費分攤
                                   plat_token=None,
                                   id=None,
                                   ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+f"/v1/proxy/commission/template/{id}/platformFeeShares",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def edit_plat_settlement_shares(self,     # 編輯平台費分攤
                                    plat_token=None,
                                    id=None, channelCode=None,
                                    gameType=None, fee=None,
                                    platformFeeLimit=None,
                                    data=FileNotFoundError
                                    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+f"/v1/proxy/commission/template/{id}/platformFeeShares",
                               json=data                               # [
                               #        {
                               #            "channelCode": channelCode,
                               #            "platformFee": [{
                               #                "gameType": gameType,
                               #                "fee": fee
                               #            }],
                               #            "platformFeeLimit": platformFeeLimit
                               #        }
                               #    ]
                               ,
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_commission_config(self,     # 獲取設置返佣
                              plat_token=None,
                              id=None,
                              ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+f"/v1/proxy/commission/template/{id}/commissionConfig",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def edit_commission_config(self,     # 獲取設置返佣
                               plat_token=None,
                               id=None, profit=None,
                               commissionLimit=None, commission=None,
                               validUserCount=None,
                               json=[]
                               ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+f"/v1/proxy/commission/template/{id}/commissionConfig",
                               json=json,
                               #    [
                               #        {
                               #            "profit": profit,
                               #            "commissionLimit": commissionLimit,
                               #            "commission": commission,
                               #            "validUserCount": validUserCount
                               #        }
                               #    ],
                               params={}
                               )
        self.print_response(response)
        return response.json()


class Proxy(PlatformAPI):

    def get_proxy(self,     # 獲取代理列表
                  plat_token=None,
                  From="2022-01-01T00:00:00Z", to="2022-12-31T00:00:00Z",
                  minBalance=None, maxBalance=None,
                  creditStatus=None, queryType=None,
                  input=None, groupName=None,
                  channel=None, page=None, size=None,
                  ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy",
                               json={},
                               params={
                                   "from": From,
                                   "to": to,
                                   "minBalance": minBalance,
                                   "maxBalance": maxBalance,
                                   "creditStatus": creditStatus,
                                   "queryType": queryType,
                                   "input": input,
                                   "groupName": groupName,
                                   "channel": channel,
                                   "page": page,
                                   "size": size,
                               }
                               )
        self.print_response(response)
        return response.json()

    def account_validate(self,     # 校驗代理帳號
                         plat_token=None,
                         accounts=[]
                         ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/proxy/account/validate",
                                json={
                                    "accounts": accounts,
                                },
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def add_proxy(self,     # 創建代理
                  plat_token=None,
                  proxyAccount=None,
                  proxyName=None, password=None,
                  telephone=None, proxyChannelId=None,
                  commissionId=None, registerIp=None,
                  ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/proxy",
                                json={
                                    "proxyAccount": proxyAccount,
                                    "proxyName": proxyName,
                                    "password": password,
                                    "telephone": telephone,
                                    "proxyChannelId": proxyChannelId,
                                    "commissionId": commissionId,
                                    "registerIp": registerIp
                                },
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def edit_sub_count(self,  # 修改子代理上限
                       plat_token=None,
                       proxyId=None,
                       subCount=None,
                       ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/proxy/{}/subCount".format(proxyId),
                               json={
            "subCount": subCount
        },
            params={}
        )
        self.print_response(response)
        return response.json()

    def edit_sub_commission(self,  # 申請佣金模式變更
                            plat_token=None,
                            proxyId=None,
                            commissionId=None,
                            ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/proxy/{}/commission".format(proxyId),
                               json={
            "commissionId": commissionId
        },
            params={}
        )
        self.print_response(response)
        return response.json()

    def edit_channel(self,  # 編輯代理渠道
                     plat_token=None,
                     proxyId=None,
                     channelId=None,
                     ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/proxy/{}/channel".format(proxyId),
                               json={
            "channelId": channelId
        },
            params={}
        )
        self.print_response(response)
        return response.json()

    def get_detail_edit(self,  # 查詢代理列表編輯資訊
                        plat_token=None,
                        userId=None,
                        ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/{}/detail/edit".format(userId),
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_detail_display(self,  # 查詢代理列表顯示資訊
                           plat_token=None,
                           userId=None,
                           ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/{}/detail/display".format(userId),
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_commission_avg(self,  # 查詢三個月平均佣金
                           plat_token=None,
                           proxyId=None,
                           ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/{}/commission/avg".format(proxyId),
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_trade_info(self,  # 查詢交易信息
                       plat_token=None,
                       userId=None,
                       # 交易类型: 1會員上分(充值額度)|2代理佣金提現|3代理紅利|4代理充值補分(充值上分額度)|5代理充值減分|6代理加幣|7代理減幣|8加幣-代理佣金|9加幣-代理獎金|10減幣-代理佣金|11減幣-代理獎金|12佣金|13充值|14提現|15調整紅利額度|16調整公司額度
                       tradeTypes=None,
                       From=None, to=None,
                       page=None, size=None,
                       ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/tradeInfo",
                               json={},
                               params={
                                   "userId": userId,
                                   "tradeTypes": tradeTypes,
                                   "from": From, "to": to,
                                   "page": page, "size": size,
                               }
                               )
        self.print_response(response)
        return response.json()

    def get_domain_query(self,  # 搜尋代理域名
                         plat_token=None,
                         type=None, accountOrName=None,
                         commissionId=None, page=None, size=None,
                         ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/domain/query",
                               json={},
                               params={
                                   "type": type,
                                   "accountOrName": accountOrName,
                                   "commissionId": commissionId,
                                   "page": page,
                                   "size": size,
                               }
                               )
        self.print_response(response)
        return response.json()


class ProxyManage(PlatformAPI):

    def get_manage_list(self,     # 獲取代理審核列表
                        plat_token=None,
                        registerStartTime="2023-01-01T00:00:00Z", registerEndTime="2023-12-31T23:59:59Z",
                        proxyAccount=None, proxyName=None,
                        # 代理狀態 0:待審核|1:一審通過|2:一審不通過|3:二審通過|4:二審不通過
                        approver=None, proxyManageStatus=None,
                        page=None, size=None,
                        ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/user/manage/list",
                               json={},
                               params={
                                   "registerStartTime": registerStartTime,
                                   "registerEndTime": registerEndTime,
                                   "proxyAccount": proxyAccount,
                                   "proxyName": proxyName,
                                   "approver": approver,
                                   "proxyManageStatus": proxyManageStatus,
                                   "page": page,
                                   "size": size,
                               }
                               )
        self.print_response(response)
        return response.json()

    def get_manage_approver(self,     # 獲取代理審批人列表
                            plat_token=None,
                            ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/user/manage/list/approver",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def approval_first(self,     # 代理審批一審
                       plat_token=None,
                       id=None, isApprove=None, remark=None
                       ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/proxy/user/manage/{}/first/approval".format(id),
                               json={
            "isApprove": isApprove,
            "remark": remark,
        },
            params={}
        )
        self.print_response(response)
        return response.json()

    def approval_second(self,     # 代理審批二審
                        plat_token=None,
                        id=None, isApprove=None, remark=None
                        ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/proxy/user/manage/{}/second/approval".format(id),
                               json={
            "isApprove": isApprove,
            "remark": remark,
        },
            params={}
        )
        self.print_response(response)
        return response.json()

    def clean_proxy_approval(self, token=None, size=100):  # 批量駁回待審核訂單
        jsdata = self.get_manage_list(
            plat_token=token, size=size, proxyManageStatus=0)
        jsdata2 = self.get_manage_list(
            plat_token=token, size=size, proxyManageStatus=1)
        ret = jsonpath.jsonpath(jsdata, "$..id")
        ret2 = jsonpath.jsonpath(jsdata2, "$..id")
        try:
            if ret:
                for i in ret:
                    self.approval_first(plat_token=token, id=i,
                                        isApprove=False, remark="rej")
            if ret2:
                for i in ret2:
                    self.approval_second(plat_token=token, id=i,
                                         isApprove=False, remark="rej")
        except:
            pass

    def get_first_approval_id(self, token=None):
        jsdata = self.get_manage_list(plat_token=token, proxyManageStatus=0)
        ret = jsonpath.jsonpath(jsdata, "$..id")
        if ret == False:
            add = Proxy()
            add.add_proxy(plat_token=token, proxyAccount="AutoTestProxy"+str(random.randrange(99999)),
                          password="abc123456", telephone=str(random.randrange(10000000000, 19999999999)), commissionId=1)
            jsdata = self.get_manage_list(
                plat_token=token, proxyManageStatus=0)
            ret = jsonpath.jsonpath(jsdata, "$..id")
        return str(ret[0])

    def get_second_approval_id(self, token=None):
        jsdata = self.get_manage_list(plat_token=token, proxyManageStatus=1)
        ret = jsonpath.jsonpath(jsdata, "$..id")
        if ret == False:
            add = Proxy()
            add.add_proxy(plat_token=token, proxyAccount="AutoTestProxy"+str(random.randrange(99999)),
                          password="abc123456", telephone=str(random.randrange(10000000000, 19999999999)), commissionId=1)
            jsdata = self.get_manage_list(
                plat_token=token, proxyManageStatus=0)  # 獲取待一審訂單
            ret = jsonpath.jsonpath(jsdata, "$..id")
            print(ret)
            self.approval_first(
                id=str(ret[0]), isApprove=True, remark="auto_test")
            jsdata = self.get_manage_list(
                plat_token=token, proxyManageStatus=1)  # 獲取待二審訂單
            ret = jsonpath.jsonpath(jsdata, "$..id")
        return str(ret[0])

    def get_second_approval_success_id(self, token=None):
        jsdata = self.get_manage_list(plat_token=token, proxyManageStatus=4)
        ret = jsonpath.jsonpath(jsdata, "$..id")
        if ret == False:
            add = Proxy()
            add.add_proxy(plat_token=token, proxyAccount="AutoTestProxy"+str(random.randrange(99999)),
                          password="abc123456", telephone=str(random.randrange(10000000000, 19999999999)), commissionId=1)
            jsdata = self.get_manage_list(
                plat_token=token, proxyManageStatus=0)  # 獲取待一審訂單
            ret = jsonpath.jsonpath(jsdata, "$..id")
            self.approval_first(
                id=str(ret[0]), isApprove=True, remark="auto_test")
            jsdata = self.get_manage_list(
                plat_token=token, proxyManageStatus=1)  # 獲取待二審訂單
            ret = jsonpath.jsonpath(jsdata, "$..id")
            self.approval_second(
                id=str(ret[0]), isApprove=False, remark="auto_test")
            jsdata = self.get_manage_list(
                plat_token=token, proxyManageStatus=4)  # 獲取待二審結束
            ret = jsonpath.jsonpath(jsdata, "$..id")
        return str(ret[0])


class ProxyCredit(PlatformAPI):

    def get_credit_detail(self,     # 查詢上分紀錄
                          plat_token=None,
                          proxyId=None, tradeType=None,
                          From="2022-01-01T00:00:00Z", to="2022-12-31T23:59:59Z",
                          tradeId=None, relationUsername=None,
                          minAmount=None, maxAmount=None,
                          page=None, size=None,
                          ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/credit/detail",
                               json={},
                               params={
                                   "proxyId": proxyId,
                                   "tradeType": tradeType,
                                   "from": From,
                                   "to": to,
                                   "tradeId": tradeId,
                                   "relationUsername": relationUsername,
                                   "minAmount": minAmount,
                                   "maxAmount": maxAmount,
                                   "page": page,
                                   "size": size,
                               }
                               )
        self.print_response(response)
        return response.json()

    def edit_credit(self,     # 調整充值額度
                    plat_token=None,
                    userId=None, amount=None,
                    changeType=None, status=None,
                    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/proxy/credit",
                               json={
                                   "userId": userId,
                                   "amount": amount,
                                   "changeType": changeType,
                                   "status": status,
                               },
                               params={}
                               )
        self.print_response(response)
        return response.json()


class ProxyCommission(PlatformAPI):

    def get_proxy_commission(self,     # 佣金結算查詢
                             plat_token=None,
                             settleDate=None,
                             proxyName=None,
                             proxyAccount=None,
                             commissionTemplateId=None,
                             groupName=None,
                             channelName=None,
                             minAmount=None, maxAmount=None,
                             proxyManageStatus=None,
                             grantStatus=None,
                             page=None, size=None,
                             ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/commission",
                               json={},
                               params={
                                   "settleDate": settleDate,
                                   "proxyName": proxyName,
                                   "proxyAccount": proxyAccount,
                                   "commissionTemplateId": commissionTemplateId,
                                   "groupName": groupName,
                                   "channelName": channelName,
                                   "minAmount": minAmount, "maxAmount": maxAmount,
                                   "proxyManageStatus": proxyManageStatus,
                                   "grantStatus": grantStatus,
                                   "page": page, "size": size,
                               }
                               )
        self.print_response(response)
        return response.json()

    def get_win_total(self,     # 查詢公司總輸贏
                      plat_token=None,
                      proxyId=None, settleDate=None,
                      ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/commission/winTotal",
                               json={},
                               params={
                                   "proxyId": proxyId,
                                   "settleDate": settleDate,
                               }
                               )
        self.print_response(response)
        return response.json()

    def get_sub_user_commission(self,     # 查詢下級會員佣金
                                plat_token=None,
                                proxyId=None, settleDate=None,
                                ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/commission/subUserCommission",
                               json={},
                               params={
                                   "proxyId": proxyId,
                                   "settleDate": settleDate,
                               }
                               )
        self.print_response(response)
        return response.json()

    def get_sub_proxy_commission(self,     # 查詢下級代理佣金
                                 plat_token=None,
                                 proxyId=None, settleDate=None,
                                 ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/commission/subProxyCommission",
                               json={},
                               params={
                                   "proxyId": proxyId,
                                   "settleDate": settleDate,
                               }
                               )
        self.print_response(response)
        return response.json()

    def get_history(self,     # 佣金結算歷史查詢
                    plat_token=None,
                    settleDate=None,
                    minAmount=None, maxAmount=None,
                    proxyName=None, proxyAccount=None,
                    commissionTemplateId=None,
                    proxyManageStatus=None,
                    approver=None,
                    page=None, size=None,
                    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/commission/history",
                               json={},
                               params={
                                   "settleDate": settleDate,
                                   "minAmount": minAmount, "maxAmount": maxAmount,
                                   "proxyName": proxyName, "proxyAccount": proxyAccount,
                                   "commissionTemplateId": commissionTemplateId,
                                   "proxyManageStatus": proxyManageStatus,
                                   "approver": approver,
                                   "page": page, "size": size,
                               }
                               )
        self.print_response(response)
        return response.json()

    def get_grant_status(self,     # 結算狀態列表
                         plat_token=None,
                         ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/commission/grantStatus",
                               json={},
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_costShare(self,     # 查詢成本分攤
                      plat_token=None,
                      proxyId=None, settleDate=None,
                      ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/proxy/commission/costShare",
                               json={},
                               params={
                                   "proxyId": proxyId,
                                   "settleDate": settleDate,
                               }
                               )
        self.print_response(response)
        return response.json()

    def first_approve(self,     # 佣金發放一審
                      plat_token=None,
                      detailId=None,
                      remark=None, isPass=None
                      ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+f"/v1/proxy/commission/{detailId}/firstApprove",
                               json={
                                   "remark": remark,
                                   "isPass": isPass
                               },
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def second_approve(self,     # 佣金發放二審
                       plat_token=None,
                       detailId=None,
                       remark=None, isPass=None
                       ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+f"/v1/proxy/commission/{detailId}/secondApprove",
                               json={
                                   "remark": remark,
                                   "isPass": isPass
                               },
                               params={}
                               )
        self.print_response(response)
        return response.json()
