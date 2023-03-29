# -*- coding: utf-8 -*-
from utils.data_utils import EnvReader
from utils.api_utils import API_Controller, KeywordArgument


env = EnvReader()
web_host = env.WEB_HOST


class WebAPI(API_Controller):
    def __init__(self, token=None):
        super().__init__(platform='cs')
        if token:
            self.request_session.headers.update({"token": token})

    def login(self, deviceId="123", osType="WEB", username='qwe220805', password='abc123456', code=None):
        self.request_session.headers.update({"device-id": deviceId})
        self.request_session.headers.update({"os-type": osType})

        request_body = {
            "method": "post",
            "url": "/v1/user/login",
            "json": {
                "username": username,
                "pwd": password,
                "captchaValidation":
                    {
                        "channelName": "string",
                        "imgToken": "string"
                    },
                "code": code
            }
        }

        response = self.send_request(**request_body)
        try:
            self.request_session.headers.update(
                {"token": str(response.json()['data']['token'])})
        except:
            print("登錄失敗")
        return response

    # 登出
    def logout(self):
        request_body = {
            "method": "post",
            "url": "/v1/user/logout"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 註冊帳號
    def user_register(
            self, deviceId="123", osType="WEB", mobile='13224455667', code="000000", countryCode=86,
            username='tester001', password="", confirmPassword=None, proxyCode=None
    ):
        self.request_session.headers.update({"device-id": deviceId})
        self.request_session.headers.update({"os-type": osType})

        request_body = {
            "method": "post",
            "url": "/v1/user/register",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        self.request_session.headers.update({"uid": str(response.json()['data']['userId'])})
        self.request_session.headers.update({"token": str(response.json()['data']['token'])})
        return response.json()

    # 忘記密碼,發送驗證碼
    def user_send_code(self, username=None, telephone=None):
        request_body = {
            "method": "post",
            "url": "/v1/user/sendCode",
            "json": {
                "username": username,
                "telephone": telephone,
                "captchaValidation":
                    {
                        "channelName": "string",
                        "imgToken": "string"
                    }
            }
        }

        response = self.send_request(**request_body)
        return response.json()

    # 用戶重設密碼
    def reset_pwd(self, deviceId="123", osType="WEB", code=None, username=None, telephone=None, newPwd=None):
        self.request_session.headers.update({"device-id": deviceId})
        self.request_session.headers.update({"os-type": osType})

        request_body = {
            "method": "put",
            "url": "/v1/user/pwd",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 手機快捷登陸
    def mobile_login(self, deviceId="123", osType="WEB", telephone=None, code=None):
        self.request_session.headers.update({"device-id": deviceId})
        self.request_session.headers.update({"os-type": osType})

        request_body = {
            "method": "post",
            "url": "/v1/user/loginByMobile",
            "json": {
                "telephone": telephone,
                "code": code,
                "captchaValidation":
                    {
                        "channelName": "string",
                        "imgToken": "string"
                    }
            }
        }

        response = self.send_request(**request_body)
        try:
            self.request_session.headers.update(
                {"uid": str(response.json()['data']['userId'])})
            self.request_session.headers.update(
                {"token": str(response.json()['data']['token'])})
        except:
            print("登入失敗")
        return response.json()
