# -*- coding: utf-8 -*-
from .platApiBase import PlatformAPI  # 執行RF時使用
from utils.api_utils import KeywordArgument
from utils.generate_utils import Make
from utils.data_utils import EnvReader
import jsonpath


env = EnvReader()
platform_host = env.PLATFORM_HOST


class Change(PlatformAPI):  # 資金配置管理

    def change_apply(self,  # 申請變更
                     plat_token=None,
                     # 0:玩家, 1:代理
                     userType=0,
                     usernames=[],
                     # 调整类型(1:加币, 2:减币, 3:加币(红利), 4:减币(红利), 5:增加提现流水, 6:减少提现流水, 7:充值补分, 8:充值减分)
                     changeType: int = 1,
                     # 子类型(1:会员充值, 2:代理充值, 3:会员额度, 4:提现补单, 5:转账补单, 6:代理佣金(加币), 7:代理奖金(减币), 8:活动红利, 9:返水部分)
                     changeSubType: int = 1,
                     amount: int = None,
                     # 流水沒填會噴錯
                     water=None,
                     platformType=None, gameId=None, reason: str = 'string'
                     ):
        if plat_token != None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/fund/change/apply",
                                json=KeywordArgument.body_data(),
                                params={}
                                )
        self.print_response(response)
        return response.json()


class ChangeAudit(PlatformAPI):  # 資金配置管理

    def get_applier_list(self,  # 查詢申請人列表
                         plat_token=None,

                         ):
        if plat_token != None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.get(platform_host+"/v1/fund/change/audit/applier/list",
                               json=KeywordArgument.body_data(),
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def get_list(self,  # 查詢資金審核列表
                 plat_token=None,
                 page=None, size=None,
                 id=None,
                 minAmount=None, maxAmount=None,
                 userType=None,  # 用户类型：0玩家，1代理
                 userName=None,
                 changeType=None,  # 操作类型：1红包，2平台奖励，3活动红利，-1人工扣回
                 applier=None,
                 status=None,  # 审核状态：0待审核，1一审通过，2一审拒绝，3二审通过，4二审拒绝
                 startTime=Make.date('start'), endTime=Make.date('end')
                 ):
        if plat_token != None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.post(platform_host+"/v1/fund/change/audit/list",
                                json=KeywordArgument.body_data(),
                                params={}
                                )
        self.print_response(response)
        return response.json()

    def approve_first(self,  # 一審
                      plat_token=None,
                      id=None, status=False,  # 审核结果：true 通过， false 不通过
                      remark='AutoTester'
                      ):
        if plat_token != None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/fund/change/audit/approve/first",
                               json=KeywordArgument.body_data(),
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def approve_second(self,  # 二審
                       plat_token=None,
                       id=None, status=False,  # 审核结果：true 通过， false 不通过
                       remark='AutoTester'
                       ):
        if plat_token != None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.request_session.put(platform_host+"/v1/fund/change/audit/approve/second",
                               json=KeywordArgument.body_data(),
                               params={}
                               )
        self.print_response(response)
        return response.json()

    def approve_all(self,  #
                    plat_token=None,
                    userName='AutoTester',
                    status: bool = False,  # 审核结果：true 通过， false 不通过
                    ):
        if plat_token != None:
            self.request_session.headers.update({"token": str(plat_token)})
        response = self.get_list(size=50, status=0, userName=userName)
        target = jsonpath.jsonpath(response, '$..records[*].id')
        if status is True:
            for i in target:
                remark = '自動審合通過'
                self.approve_first(id=i, status=status, remark=remark)
                self.approve_second(id=i, status=status, remark=remark)
        else:
            for i in target:
                remark = '自動審核駁回'
                self.approve_first(id=i, status=status, remark=remark)
        return response
