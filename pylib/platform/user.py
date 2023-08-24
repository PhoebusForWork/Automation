# -*- coding: utf-8 -*-
from ..platform.platApiBase import PlatformAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader
import jsonpath

env = EnvReader()
platform_host = env.PLATFORM_HOST
# VIP層級
class UserVip(PlatformAPI):


    # 編輯VIP層級
    def edit_vip(
            self, plat_token=None, id=None, name=None,
            rechargeTotal=None, betTotal=None, levelGift=None, birthdayGift=None, festivalGift=None,
            redEnvelop=None, limitBet=None, limitRecharge=None, isVip=None, remark=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/user/vip/config/{id}",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯VIP專享
    def edit_vip_only(self, plat_token=None, vipId=None, isVip=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/user/vip/config/{vipId}/isVip",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取VIP配置
    def get_vip_info(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/user/vip/config"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取VIP列表
    def get_vip_list(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/user/vip/config/mapList"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取存在vip_id
    def get_vip_id_exist(self, plat_token=None):
        response = self.get_vip_info(plat_token=plat_token)
        target = jsonpath.jsonpath(response, '$..data[*]')
        return target[-1]

# 客戶管理
class User(PlatformAPI):
    # 查詢客戶列表
    def get_user_list(
            self, plat_token=None, From=None, to=None, minBalance=None, maxBalance=None,
            status=None, vipId=None, groupId=None, isRegisterTime=None, searchType=None,
            keyword=None, page=None, size=None, isOnline=None, isWhiteList=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/user",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 客戶列表查詢條件
    def user_params(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/user/params"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢客戶資訊
    def get_user_info(self, plat_token=None, userId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/user/{userId}"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢客戶財務資訊
    def get_user_amount(self, plat_token=None, userId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/user/{userId}/account"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 更新客戶備註(不需審核)
    def user_remark(self, plat_token=None, userId=None, remark=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/user/{userId}/remark",
            "json": {"remark": remark}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 更新客戶真實姓名(不需審核)
    def user_really_name(self, plat_token=None, userId=None, reallyName=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/user/{userId}/reallyName",
            "json": {"reallyName": reallyName}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 設置客戶撞庫白名單
    def set_white_list(self, plat_token=None, userId=None, isWhiteList=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/user/{userId}/isWhiteList",
            "params": {"isWhiteList": isWhiteList}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 開通代理角色
    def user_convert_proxy(self, plat_token=None, userId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/user/convertProxy",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 校驗會員帳號是否存在
    def username_validate(self, plat_token=None, usernames=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/user/username/validate",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 同设备号查询
    def user_device(self, plat_token=None,
                    deviceId=None, usernames=None, userType=None,
                    page=None, size=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/user/userDevice",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 申請鎖定 lockStatus(鎖定類別) LOGIN：登入, RECHARGE：充值, WITHDRAW：提領, TRANSFER：轉帳
    def user_lock_status(self, plat_token=None, userIds=None, lockStatus=None, isLock=None, remark=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/user/lockStatus",
            "json": {
                "userIds": userIds,
                "userLockTypeList": [
                    {
                        "lockStatus": lockStatus,
                        "isLock": isLock
                    }
                ],
                "remark": remark
            }
        }

        response = self.send_request(**request_body)
        return response.json()

    # 修改客戶VIP層級
    def edit_user_vip(self, plat_token=None, userId=None, vipId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/userVip/{userId}",
            "params": {"userId": userId, "vipId": vipId}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢客戶VIP層級
    def get_user_vip_info(self, plat_token=None, userName=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/userVip",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 風險套利重複ip
    def risk_analysis_same_ip(self, plat_token=None, userId=None, page=None, size=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/user/{userId}/risk/analysis/same/ip",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 風險套利分析查詢
    def risk_analysis_arbitrage(
            self, plat_token=None, id=None, From=None, to=None,
            username=None, userType=None, reallyName=None, page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/user/{id}/risk/analysis/arbitrage",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 登入日誌
    def login_info(
            self, plat_token=None, id=None, From='2022-01-01T00:00:00Z', to='2022-12-31T23:59:59Z',
            type=None, keyword=None, osType=None, page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/user/{id}/login/info",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 客戶登入統計
    def login_stat(self, plat_token=None, userId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/user/login/stat/{userId}"
        }

        response = self.send_request(**request_body)
        return response.json()

    def get_client_user(self, plat_token=None):
        target = self.get_user_list(plat_token=plat_token, From='2022-01-01T00:00:00Z', status=0,
                                    to='2025-01-15T00:00:00Z', page=None, size=1000)
        client_user = jsonpath.jsonpath(target, "$..records[?(@.userType==0).userId]")
        return client_user[0]

# VIP積分
class UserVipPointRatio(PlatformAPI):
    # VIP積分設定清單
    def get_point_point_ratio(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/vip/point-ratio"
        }

        response = self.send_request(**request_body)
        return response.json()

    #IP積分特定幣別修改記錄
    def get_point_point_ratio_records(self, plat_token=None,currency="CNY"):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/vip/point-ratio/records?currency={currency}"
        }

        response = self.send_request(**request_body)
        return response.json()

    #修改VIP積分幣別排序
    def sort_point_point_ratio(self, plat_token=None,currency="CNY", position=0):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/vip/point-ratio?currency={currency}&position={position}"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 修改VIP積分設定
    def edit_point_ratio(self, plat_token=None, currency=None, ratio=0, showAmount=0 ):

        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": f"/v1/vip/point-ratio?currency={currency}",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取特定幣別的 vip_point_ratio
    def get_vip_Point_Ratio(self, plat_token=None, currency=None):
        response = self.get_point_ratio(plat_token)
        target = jsonpath.jsonpath(response, "$..data[?(@.currency=='"+ currency+"')]")
        return target[-1]

# 審批操作
class UserManage(PlatformAPI):
    # 查詢審批列表
    def get_user_manage_list(
            self, plat_token=None, approveTimeType=0,
            From="2023-01-01T00:00:00Z", to="2023-12-31T23:59:59Z",
            username=None, userType=None, optType=None, creator=None,
            firstApprover=None, secondApprover=None, status=None, page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/user/manage",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢審批參數
    def get_user_manage_query_params(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/user/manage/query/params"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 後台操作記錄
    def get_user_manage_log(
            self, plat_token=None, userId=None, From=None, to=None,
            optType=None, creator=None, page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/user/manage/log/{userId}",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 一審 審核狀態 1:核准 / 2:駁回
    def first_approval(self, plat_token=None, id=None, status=None, remark=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/user/manage/{id}/first/approval",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 二審 第二審批狀態 4:核准 / 5:駁回
    def second_approval(self, plat_token=None, id=None, status=None, remark=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/user/manage/{id}/second/approval",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 修改上級代理
    def user_manage_parent(self, plat_token=None, userId=None, parentUsername=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/user/manage/parent",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯會員聯絡資料
    def user_manage_contact(self, plat_token=None, userId=None, telephone=None, email=None, birthday=None, remark=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/user/manage/contact",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    def clean_approval(self, plat_token=None, optType=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        jsdata = self.get_user_manage_list(optType=optType, size=100, status=0)
        ret = jsonpath.jsonpath(jsdata, "$..id")
        jsdata2 = self.get_user_manage_list(optType=optType, size=100, status=3)
        ret2 = jsonpath.jsonpath(jsdata2, "$..id")
        if ret:
            for i in ret:
                self.first_approval(id=i, status=2, remark="auto_rej")
        if ret2:
            for i in ret2:
                self.second_approval(id=i, status=5, remark="auto_rej")

    def get_manage_id(self, plat_token=None, phase=1):  # 一審訂單:1 二審訂單:2
        FIRST = 0
        SECOND = 3
        userId = 12
        if env.env:
            userId = 2
        phase = FIRST if phase == 1 else SECOND
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        jsdata = self.get_user_manage_list(plat_token=plat_token, status=phase)
        ret = jsonpath.jsonpath(jsdata, "$..id")
        if ret is False:
            self.user_manage_parent(userId=userId, parentUsername='proxy001')
            jsdata = self.get_user_manage_list(plat_token=plat_token, status=FIRST)
            ret = jsonpath.jsonpath(jsdata, "$..id")
            if phase == SECOND:
                self.first_approval(id=ret[0], status=1)
        return ret[0]

# 客戶VIP層級變更紀錄
class UserVipLevelRecord(PlatformAPI):
    def get_vip_level_record(self, plat_token=None,
                             From=None, to=None, username=None, actionType=None,
                             operator=None, page=None, size=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/user/manage/parent",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()
class UserOperation(PlatformAPI):
    # 用戶操作記錄列表
    def get_log_list(self, From='2023-01-01T00:00:00Z', to='2024-01-01T00:00:00Z',
                     username=None, ip=None, page=None, size=None,
                     plat_token=None,
                     ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/user/operation/log",
            "params": {"from": From, "to": to,
                       "username": username, "ip": ip,
                       "page": page, "size": size}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 用戶操作記錄
    def get_account_log(self, userId=None, page=None, size=None,
                        plat_token=None,
                        ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/user/operation/log/{userId}",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()
