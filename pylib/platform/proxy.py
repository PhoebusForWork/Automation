# -*- coding: utf-8 -*-

import jsonpath
import random
import string
from ..platform.platApiBase import PlatformAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader
from utils.generate_utils import Make
from datetime import datetime, timedelta


env = EnvReader()
platform_host = env.PLATFORM_HOST


class ProxyChannel(PlatformAPI):
    # 新增代理渠道
    def add_channel(self, plat_token=None, channel=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/proxy/channel",
            "json": {"channel": channel}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯代理渠道
    def edit_channel(self, plat_token=None, channel=None, channelId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/channel/{channelId}",
            "json": {"channel": channel}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 移除代理渠道
    def delete_channel(self, plat_token=None, channelId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "delete",
            "url": f"/v1/proxy/channel/{channelId}"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 顯示代理渠道
    def get_channel(self, plat_token=None, page=None, size=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/channel",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 顯示所有代理渠道
    def get_channel_all(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/channel/all"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取未綁定代理渠道
    def get_channel_available(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/channel/available"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取未綁定代理渠道
    def get_available_channel_auto(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/channel/available"
        }

        response = self.send_request(**request_body)
        ret = jsonpath.jsonpath(response.json(), "$..id")
        if ret is False:
            self.add_channel(plat_token, channel=''.join(
                random.choice(string.ascii_letters) for _ in range(10)))
            response = self.send_request(**request_body)
            ret = jsonpath.jsonpath(response.json(), "$..id")
            # self.print_response(ret)
        return ret[-1]


class ProxyGroup(PlatformAPI):
    # 新增代理團隊
    def add_group(self, plat_token=None, groupName=None, channelIds=[]):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/proxy/group",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯代理團隊
    def edit_group(self, plat_token=None, groupName=None, channelIds=[], groupId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/group/{groupId}",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯代理團隊
    def delete_group(self, plat_token=None, groupId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "delete",
            "url": f"/v1/proxy/group/{groupId}"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 取得團隊資訊
    def get_group_info(self, plat_token=None, page=None, size=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/group/groupsAndChannels",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 取得存在團隊id
    def get_exist_group_auto(self, plat_token=None, page=None, size=1000):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/group/groupsAndChannels",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        ret = jsonpath.jsonpath(response.json(), "$..records[(@.length-1)].id")
        self.print_response(response)
        return ret[0]


class ProxyCommissionTemplate(PlatformAPI):
    # 建立佣金模板
    def add_template(self, plat_token=None, name=None, isEnabled=None, isNeedToVerify=None, platformFeeShare=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/proxy/commission/template",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯佣金模板
    def edit_template(self, plat_token=None, id=1, name=None, isEnabled=None, isNeedToVerify=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/commission/template/{id}",
            "json": {"name": name, "isEnabled": isEnabled, "isNeedToVerify": isNeedToVerify}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取佣金模板
    def get_template(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/commission/template"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取佣金模板選單
    def get_template_list(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/commission/template/mapList"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取下級代理佣金設置
    def get_sub_condiction(self, plat_token=None, id=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/proxy/commission/template/{id}/subCommissionConditions"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯下級代理佣金設置
    def edit_sub_condiction(self, plat_token=None, id=None, subCommissionConditions=None, subSubCommissionConditions=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/commission/template/{id}/subCommissionConditions",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取結算分攤
    def get_settlement_shares(self, plat_token=None, id=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/proxy/commission/template/{id}/settlementShares"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯結算分攤
    def edit_settlement_shares(
            self, plat_token=None, id=None, activity=None,
            activityLimit=None, rebate=None, rebateLimit=None, bet=None, betCount=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/commission/template/{id}/settlementShares",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取平台費分攤
    def get_platform_fee_shares(self, plat_token=None, id=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/proxy/commission/template/{id}/platformFeeShares"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯平台費分攤
    def edit_platform_fee_shares(
            self, plat_token=None, id=None, channelCode=None,
            gameType=None, fee=None, platformFeeLimit=None, data=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        # data example
        #  [
        #        {
        #            "channelCode": channelCode,
        #            "platformFee": [{
        #                "gameType": gameType,
        #                "fee": fee
        #            }],
        #            "platformFeeLimit": platformFeeLimit
        #        }
        #    ]
        request_body = {
            "method": "put",
            "url": f"/v1/proxy/commission/template/{id}/platformFeeShares",
            "json": data,
            "params": {"currency": "USD"},
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取設置返佣
    def get_commission_conditions(self, plat_token=None, id=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/proxy/commission/template/{id}/commissionConditions"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯設置返佣
    def edit_commission_conditions(
            self, plat_token=None, id=None, json=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        # json example
        #    [
        #        {
        #            "profit": profit,
        #            "commissionLimit": commissionLimit,
        #            "commission": commission,
        #            "validUserCount": validUserCount
        #        }
        #    ]
        request_body = {
            "method": "put",
            "url": f"/v1/proxy/commission/template/{id}/commissionConditions",
            "json": json
        }

        response = self.send_request(**request_body)
        return response.json()


class Proxy(PlatformAPI):
    # 獲取代理列表
    def get_proxy(
            self, plat_token=None,
            From=Make.generate_custom_date(months=-1), to=Make.date('end'),
            minBalance=None, maxBalance=None,
            commissionId=None, queryType=None,
            input=None, groupName=None,
            channel=None, page=None, size=None,
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 校驗代理帳號
    def account_validate(self, plat_token=None, accounts=[]):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/proxy/account/validate",
            "json": {"accounts": accounts}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 創建代理
    def add_proxy(
            self, plat_token=None,
            proxyAccount=None, pwd=None, email=None,
            countryCode=None, telephone=None, proxyChannelId=None,
            commissionId=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/proxy",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 修改子代理上限
    def edit_sub_count(self, plat_token=None, proxyId=None, subCount=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/{proxyId}/subCount",
            "json": {"subCount": subCount}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 申請佣金模式變更
    def edit_sub_commission(self, plat_token=None, proxyId=None, commissionId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/{proxyId}/commission",
            "json": {"commissionId": commissionId}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯代理渠道
    def edit_channel(self, plat_token=None, proxyId=None, channelId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/{proxyId}/channel",
            "json": {"channelId": channelId}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢交易信息
    def get_trade_info(
            self, plat_token=None, userId=None,
            # 交易类型: 1會員上分(充值額度)|2代理佣金提現|3代理紅利|4代理充值補分(充值上分額度)|5代理充值減分|6代理加幣|7代理減幣|8加幣-代理佣金|9加幣-代理獎金|10減幣-代理佣金|11減幣-代理獎金|12佣金|13充值|14提現|15調整紅利額度|16調整公司額度
            tradeTypes=None,
            From=None, to=None,
            page=None, size=None,
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/tradeInfo",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 搜尋代理域名
    def get_domain_query(self, plat_token=None, 
                         queryType=None, input=None, 
                         commissionId=None, page=None, size=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/domain/query",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()
    
    # 更新代理備註
    def edit_remark(self, plat_token=None, proxyId=None, remark=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/{proxyId}/remark",
            "json": {"remark": remark}
        }

        response = self.send_request(**request_body)
        return response.json()
    
    # 查詢代理銀行卡
    def get_bankcards(self, plat_token=None, proxyId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/proxy/{proxyId}/bankcards"
        }

        response = self.send_request(**request_body)
        return response.json()
    
    # 申請刪除代理提款銀行卡
    def unbind_bankcard(self, plat_token=None, proxyId=None, cardId=None, remark=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": f"/v1/proxy/{proxyId}/bankcard-unbind/apply",
            "json": {"cardId": cardId, "remark": remark}
        }

        response = self.send_request(**request_body)
        return response.json()
    
    # 風險分析重複IP
    def get_risk_same_ip(self, plat_token=None, proxyId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/proxy/{proxyId}/risk/analysis/same/ip"
        }

        response = self.send_request(**request_body)
        return response.json()
    
    # 代理登入日誌
    def get_login_info(self, plat_token=None, proxyId=None,
                       From=None, to=None, type=None,
                       keyword=None, osType=None, page=None, size=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/proxy/{proxyId}/login/info"
        }

        response = self.send_request(**request_body)
        return response.json()
    
    # 查詢代理列表顯示資訊
    def get_risk_same_ip(self, plat_token=None, proxyId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/proxy/{proxyId}/detail/display"
        }

        response = self.send_request(**request_body)
        return response.json()

class ProxyOperation(PlatformAPI):
    # 代理用戶操作記錄
    def get_operation_log(self, plat_token=None, proxyId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/proxy/operation/log/{proxyId}"
        }

        response = self.send_request(**request_body)
        return response.json()

class ProxyManage(PlatformAPI):
    # 獲取代理審核列表
    def get_manage_list(
            self, plat_token=None,
            registerStartTime="2023-01-01T00:00:00Z", registerEndTime="2026-12-31T23:59:59Z",
            proxyAccount=None, proxyName=None,
            # 代理狀態 0:待審核|1:一審通過|2:一審不通過|3:二審通過|4:二審不通過
            approver=None, proxyManageStatus=None, page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/user/manage/list",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取代理審批人列表
    def get_manage_approver(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/user/manage/list/approver"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 代理審批一審
    def approval_first(self, plat_token=None, id=None, isApprove=None, remark=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/user/manage/{id}/first/approval",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 代理審批二審
    def approval_second(self, plat_token=None, id=None, isApprove=None, remark=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/user/manage/{id}/second/approval",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 批量駁回待審核訂單
    def clean_proxy_approval(self, token=None, size=100, account=None):
        jsdata = self.get_manage_list(plat_token=token, size=size, proxyManageStatus=0, proxyAccount=account)
        jsdata2 = self.get_manage_list(plat_token=token, size=size, proxyManageStatus=1, proxyAccount=account)
        ret = jsonpath.jsonpath(jsdata, "$..id")
        ret2 = jsonpath.jsonpath(jsdata2, "$..id")
        try:
            if ret:
                for i in ret:
                    self.approval_first(plat_token=token, id=i, isApprove=False, remark="rej")
            if ret2:
                for i in ret2:
                    self.approval_second(plat_token=token, id=i, isApprove=False, remark="rej")
        except Exception:
            pass

    def get_first_approval_id(self, token=None):
        jsdata = self.get_manage_list(plat_token=token, proxyManageStatus=0)
        ret = jsonpath.jsonpath(jsdata, "$..id")
        if ret is False:
            add = Proxy()
            add.add_proxy(plat_token=token, proxyAccount="AutoTestProxy" + str(random.randrange(99999)),
                          pwd="abc123456",email="AutoTestProxy@gmailtest.com", countryCode='86', telephone=str(random.randrange(10000000000, 19999999999)), 
                          proxyChannelId=1,commissionId=1)
            jsdata = self.get_manage_list(plat_token=token, proxyManageStatus=0)
            ret = jsonpath.jsonpath(jsdata, "$..id")
        return str(ret[0])

    def get_second_approval_id(self, token=None):
        jsdata = self.get_manage_list(plat_token=token, proxyManageStatus=1)
        ret = jsonpath.jsonpath(jsdata, "$..id")
        if ret is False:
            add = Proxy()
            add.add_proxy(plat_token=token, proxyAccount="AutoTestProxy" + str(random.randrange(99999)),
                          pwd="abc123456",email="AutoTestProxy@gmailtest.com", countryCode='86', telephone=str(random.randrange(10000000000, 19999999999)), 
                          proxyChannelId=1,commissionId=1)

            jsdata = self.get_manage_list(plat_token=token, proxyManageStatus=0)  # 獲取待一審訂單
            ret = jsonpath.jsonpath(jsdata, "$..id")

            self.approval_first(id=str(ret[0]), isApprove=True, remark="auto_test")
            jsdata = self.get_manage_list(plat_token=token, proxyManageStatus=1)  # 獲取待二審訂單
            ret = jsonpath.jsonpath(jsdata, "$..id")
        return str(ret[0])

    def get_second_approval_success_id(self, token=None):
        jsdata = self.get_manage_list(plat_token=token, proxyManageStatus=4)
        ret = jsonpath.jsonpath(jsdata, "$..id")
        if ret is False:
            add = Proxy()
            add.add_proxy(plat_token=token, proxyAccount="AutoTestProxy" + str(random.randrange(99999)),
                          pwd="abc123456",email="AutoTestProxy@gmailtest.com", countryCode='86', telephone=str(random.randrange(10000000000, 19999999999)), 
                          proxyChannelId=1,commissionId=1)

            jsdata = self.get_manage_list(plat_token=token, proxyManageStatus=0)  # 獲取待一審訂單
            ret = jsonpath.jsonpath(jsdata, "$..id")
            self.approval_first(id=str(ret[0]), isApprove=True, remark="auto_test")

            jsdata = self.get_manage_list(plat_token=token, proxyManageStatus=1)  # 獲取待二審訂單
            ret = jsonpath.jsonpath(jsdata, "$..id")
            self.approval_second(id=str(ret[0]), isApprove=False, remark="auto_test")

            jsdata = self.get_manage_list(plat_token=token, proxyManageStatus=4)  # 獲取待二審結束
            ret = jsonpath.jsonpath(jsdata, "$..id")

        return str(ret[0])


class ProxyCredit(PlatformAPI):
    # 查詢上分紀錄
    def get_credit_detail(
            self, plat_token=None, proxyId=None, tradeType=None,
            From="2022-01-01T00:00:00Z", to="2022-12-31T23:59:59Z",
            tradeId=None, relationUsername=None,
            minAmount=None, maxAmount=None, page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/credit/detail",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 調整充值額度
    def edit_credit(self, plat_token=None, userId=None, amount=None, changeType=None, status=None,):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/proxy/credit",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()


class ProxyCommission(PlatformAPI):
    # 佣金結算查詢
    def get_proxy_commission(
            self, plat_token=None, settleDate=None, proxyName=None, proxyAccount=None,
            commissionTemplateId=None, groupName=None, channelName=None,
            minAmount=None, maxAmount=None, proxyManageStatus=None,
            grantStatus=None, page=None, size=None,
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/commission",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢公司總輸贏
    def get_win_total(self, plat_token=None, detailId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/commission/winTotal",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢下級會員佣金
    def get_sub_user_commission(self, plat_token=None, detailId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/commission/subUserCommission",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢下級代理佣金
    def get_sub_proxy_commission(self, plat_token=None, detailId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/commission/subProxyCommission",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 佣金結算歷史查詢
    def get_history(
            self, plat_token=None, settleDate=None, minAmount=None, maxAmount=None,
            proxyName=None, proxyAccount=None, commissionTemplateId=None,
            proxyManageStatus=None, approver=None, page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/commission/history",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 結算狀態列表
    def get_grant_status(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/commission/grantStatus"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢成本分攤
    def get_cost_share(self, plat_token=None, detailId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/proxy/commission/costShare",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 佣金發放一審
    def first_approve(self, plat_token=None, detailId=None, remark=None, isPass=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/commission/{detailId}/firstApprove",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 佣金發放二審
    def second_approve(self, plat_token=None, detailId=None, remark=None, isPass=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/proxy/commission/{detailId}/secondApprove",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()


# 代理訊息
class ProxyDomain(PlatformAPI):
    # 編輯代理域名
    def edit_proxy_domain(self, proxyId=None, domain_list: dict = {}):
        request_body = {
            "method": "put",
            "url": f"/v1/proxy/domain/{proxyId}",
            "json": domain_list
        }

        response = self.send_request(**request_body)
        return response.json()

    # 取得推廣域名
    def get_promotion_link(self, proxyId=None):
        request_body = {
            "method": "get",
            "url": f"/v1/proxy/domain/{proxyId}/promotionLink"
        }

        response = self.send_request(**request_body)
        return response.json()
    
 # 佣金調整審核
class CommissionAdjust(PlatformAPI):
    # 查詢列表
    def get_proxy_commission_adjust(self, plat_token=None,
                From=None, to=None, proxyAccount=None, 
                applicant=None, approver=None, status=None, page=None, size=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        request_body = {
            "method": "get",
            "url": f"/v1/commission/adjust",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()   
    
    # 審核狀態
    def get_proxy_commission_adjust_proxyManageStatus(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        request_body = {
            "method": "get",
            "url": f"/v1/commission/adjust/proxyManageStatus"
        }

        response = self.send_request(**request_body)
        return response.json()   
    
    # 佣金結算審批人列表
    def get_proxy_commission_adjust_approverList(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        request_body = {
            "method": "get",
            "url": f"/v1/commission/adjust/approverList"
        }

        response = self.send_request(**request_body)
        return response.json()   
    
    # 佣金調整申請
    def post_commission_adjust(self, plat_token=None, detailId=None, reason=None, amount=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        request_body = {
            "method": "post",
            "url": f"/v1/commission/adjust/{detailId}",
            "json": {"reason": reason, "amount": amount}
        }

        response = self.send_request(**request_body)
        return response.json()   
    
    # 佣金調整一審
    def edit_commission_adjust_first_approve(self, plat_token=None, id=None, remark=None, isPass=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        request_body = {
            "method": "put",
            "url": f"/v1/commission/adjust/{id}/firstApprove",
            "json": {"remark": remark, "isPass": isPass}
        }

        response = self.send_request(**request_body)
        return response.json()   

    # 佣金調整二審
    def edit_commission_adjust_second_approve(self, plat_token=None, id=None, remark=None, isPass=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        request_body = {
            "method": "put",
            "url": f"/v1/commission/adjust/{id}/secondApprove",
            "json": {"remark": remark, "isPass": isPass}
        }

        response = self.send_request(**request_body)
        return response.json()   