# -*- coding: utf-8 -*-
from utils.data_utils import EnvReader
from utils.api_utils import API_Controller


env = EnvReader()
platform_host = env.PLATFORM_HOST


class PlatformAPI(API_Controller):
    def __init__(self, token=None):
        super().__init__(platform='plt')
        if token:
            self.request_session.headers.update({"token": token})

    # 新帳戶更新密碼
    def first_login_password(self, username='phoebusliu', oldPassword='abc123456', newPassword='abc123456'):
        request_body = {
            "method": "put",
            "url": "/v1/account/login/resetPassword",
            "json": {
                "account": username,
                "oldPassword": oldPassword,
                "newPassword": newPassword,
                "loginIp": "string"
            }
        }

        response = self.send_request(**request_body)
        return response.json()

    # 用戶登陸
    def login(self, username='phoebusliu', password='abc123456', imgCode='a'):
        request_body = {
            "method": "post",
            "url": "/v1/account/login",
            "json": {
                "account": username,
                "password": password,
                "imgCode": imgCode,
                "uuid": "124"
            }
        }

        response = self.send_request(**request_body)
        try:
            self.request_session.headers.update(
                {"token": str(response.json()['data']['token'])})
        except Exception as e:
            print("登入失敗")
        return response

    # 用戶登陸
    def logout(self, platform_token=None):
        if platform_token is not None:
            self.request_session.headers.update({"token": platform_token})

        request_body = {
            "method": "post",
            "url": "/v1/account/logout"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取驗證碼
    def imgcode(self, uuid=124):
        request_body = {
            "method": "post",
            "url": "/v1/account/login/imgCode",
            "params": {"uuid": uuid}
        }

        response = self.send_request(**request_body)
        return response.json()['data']['code']
