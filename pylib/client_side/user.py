# -*- coding: utf-8 -*-
import jsonpath
from ..client_side.webApiBase import WebAPI
from utils.api_utils import KeywordArgument
from utils.generate_utils import Make
from utils.data_utils import EnvReader


env = EnvReader()
web_host = env.WEB_HOST


# 客戶詳細資料
class Detail(WebAPI):
    # 獲取用戶明細資料
    def get_detail(self):
        request_body = {
            "method": "get",
            "url": "/v1/user/detail"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯用戶明細資料
    def edit_detail(self, avatar=None, nickname=None, birthday=None, sex=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/detail",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()


# 用戶安全中心
class Security(WebAPI):
    # 取得用戶安全中心資訊
    def get_security_info(self):
        request_body = {
            "method": "get",
            "url": "/v1/user/security/info"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 綁定郵箱地址
    def bind_email(self, email=None, code=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/security/email/binding",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 解綁郵箱地址
    def unbind_email(self, code=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/security/email/unbind",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 更換手機號
    def edit_mobile(self, newMobile=None, nmCode=None, omCode=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/security/mobile",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 修改密碼
    def edit_pwd(self, newPwd=None, oldPwd=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/security/pwd",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()


# 用戶-安全中心
class Trade(WebAPI):
    # 查詢資金明細
    def balance_history(
            self, webUid=None, web_token=None, orderType="", startTime="",
            endTime="", status="-1", page="", size=""
    ):
        if webUid is not None:
            self.request_session.headers.update({"uid": str(webUid)})
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "post",
            "url": "/api/gl/balance/history/v2",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取用戶體育注單列表
    def history_sport_list(
            self, webUid=None, web_token=None, endTime="2022-04-01 23:59:59", startTime="2022-04-01 23:59:59",
            channelId=None, gameId=None, page=None, size=None, status=None
    ):
        if webUid is not None:
            self.request_session.headers.update({"uid": str(webUid)})
            self.request_session.headers.update({"token": str(web_token)})

        request_body = {
            "method": "post",
            "url": "/api/game/v2/history/sportList",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()


# 用戶送貨地址
class Address(WebAPI):
    # 依使用者查詢地址
    def get_user_address(self):
        request_body = {
            "method": "get",
            "url": "/v1/user/address"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢單筆地址
    def get_user_address_one(self, id=1):
        request_body = {
            "method": "get",
            "url": f"/v1/user/address/{id}"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 新增地址
    def add_user_address(
            self, recipient=None, telephone=None, cityId=None, district=None, street=None, detailAddress=None
    ):
        request_body = {
            "method": "post",
            "url": "/v1/user/address",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 更新地址
    def edit_user_address(
            self, recipient=None, telephone=None, cityId=None, district=None, street=None, detailAddress=None, id=None
    ):
        request_body = {
            "method": "put",
            "url": "/v1/user/address",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 刪除用戶地址
    def delete_user_address(self, id=1):
        request_body = {
            "method": "delete",
            "url": f"/v1/user/address/{id}"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 省列表
    def get_provinces(self):
        request_body = {
            "method": "get",
            "url": "/v1/user/address/provinces"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 省下城市列表
    def get_city(self, provinceId=None):
        request_body = {
            "method": "get",
            "url": f"/v1/user/address/province/{provinceId}/city"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 移除非默認地址
    def clear_user_address(self, web_token=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})
        resp = self.get_user_address()
        ret = jsonpath.jsonpath(resp, "$.data[?(@.isDefault != 1)].id")
        if ret is not False:
            for i in ret:
                self.delete_user_address(id=i)

    # 獲取可刪除地址
    def get_user_address_not_default(self, web_token=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})
        resp = self.get_user_address()
        ret = jsonpath.jsonpath(resp, "$.data[?(@.isDefault != 1)].id")
        if ret is not False:
            return ret[0]
        else:
            self.add_user_address(
                recipient="AutoTest", telephone=Make.mobile(), cityId=1, detailAddress="詳細地址")
            resp = self.get_user_address()
            ret = jsonpath.jsonpath(resp, "$.data[?(@.isDefault != 1)].id")
            return ret[0]
