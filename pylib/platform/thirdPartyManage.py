# -*- coding: utf-8 -*-
from ..platform.platApiBase import PlatformAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader

env = EnvReader()
platform_host = env.PLATFORM_HOST


# 用戶驗證碼找回
class UserValidCode(PlatformAPI):
    # 查找用戶驗證碼
    # 驗證碼類型 0:預設, 1:註冊, 2:登陸, 3:重設密碼, 4:撞庫驗證, 5:原手機號解綁, 6:綁定新手機號, 7:原郵箱地址解綁, 8:綁定新郵箱地址
    def get_user_valid_code(self, type=None, userName=None, device=None):
        request_body = {
            "method": "get",
            "url": "/v1/userValidCode",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 查找用戶驗證碼類型列表
    def get_type_list(self):
        request_body = {
            "method": "get",
            "url": "/v1/userValidCode/typeList"
        }
        response = self.send_request(**request_body)
        return response.json()


# 三方接口管理
class ThirdPartyManage(PlatformAPI):
    # 三方接口:權重更新
    def update_third_weighting(self, id=None, weight=None):
        request_body = {
            "method": "put",
            "url": "/v1/thirdPartyManage/weighting",
            "json": [{"id": id, "weight": weight}]
        }
        response = self.send_request(**request_body)
        return response.json()

    # 三方接口:開關更新
    def update_third_switched(self, id, isEnable):
        request_body = {
            "method": "put",
            "url": "/v1/thirdPartyManage/switched",
            "json": [{"id": id, "isEnable": isEnable}]
        }
        response = self.send_request(**request_body)
        return response.json()

    # 客服接口-群組管理-查詢
    def get_customer_group(self, groupTypeName=None, groupName=None,
                           customerServiceId=None,
                           page=None, size=None, language=None):
        request_body = {
            "method": "get",
            "url": "/v1/thirdPartyManage/customerServiceGroup",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 客服接口-群組管理-保存
    def save_customer_group(self, id=None, customerServiceId=None, language=None):
        request_body = {
            "method": "put",
            "url": "/v1/thirdPartyManage/customerServiceGroup",
            "parmas": {"language": language},
            "json": [{"id": id, "customerServiceId": customerServiceId}]
        }
        response = self.send_request(**request_body)
        return response.json()

    # 三方接口:查詢
    def get_third_interface(self, type=None):
        request_body = {
            "method": "get",
            "url": "/v1/thirdPartyManage",
            "params": {"type": type}
        }
        response = self.send_request(**request_body)
        return response.json()

    # 三方接口:圖形驗證接口-查詢
    def get_captcha(self):
        request_body = {
            "method": "get",
            "url": "/v1/thirdPartyManage/captcha"
        }
        response = self.send_request(**request_body)
        return response.json()

    # 三方接口:銀行卡接口-查詢
    def get_bank_card(self):
        request_body = {
            "method": "get",
            "url": "/v1/thirdPartyManage/bankcard"
        }
        response = self.send_request(**request_body)
        return response.json()

    # 客服接口-群組管理-最後更新時間
    def get_customer_group_last_update_time(self, language=None):
        request_body = {
            "method": "get",
            "url": "/v1/thirdPartyManage/customerServiceGroup/lastUpdateTime",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 客服接口-群組管理-群組類型下拉選單
    def get_customer_group_type(self, language=None):
        request_body = {
            "method": "get",
            "url": "/v1/thirdPartyManage/customerServiceGroup/groupType",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 客服接口-群組管理-客服下拉選單
    def get_customer_service_list(self, language=None):
        request_body = {
            "method": "get",
            "url": "/v1/thirdPartyManage/customerServiceGroup/customerServiceList",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()
