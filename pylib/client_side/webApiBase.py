# -*- coding: utf-8 -*-
from utils.data_utils import EnvReader
from utils.api_utils import API_Controller


env = EnvReader()
web_host = env.WEB_HOST


class WebAPI(API_Controller):
    def __init__(self):
        super().__init__(platform='cs')

    def login(self, deviceId="123", osType="WEB", username='qwe220805', password='abc123456', code=None):
        self.request_session.headers.update({"device-id": deviceId})
        self.request_session.headers.update({"os-type": osType})

        response = self.request_session.post(web_host+"/v1/user/login",
                                             json={"username": username,
                                                   "pwd": password,
                                                   "captchaValidation": {
                                                       "channelName": "string",
                                                       "imgToken": "string"
                                                   },
                                                   "code": code
                                                   },
                                             params={}
                                             )
        self.print_response(response)
        try:
            self.request_session.headers.update(
                {"token": str(response.json()['data']['token'])})
        except:
            print("登錄失敗")
        return response

    def logout(self):  # 登出
        response = self.request_session.post(web_host+"/v1/user/logout",
                                             json={},
                                             params={}
                                             )
        self.print_response(response)
        return response.json()

    def user_register(self, deviceId="123", osType="WEB",  # 註冊帳號
                      mobile='13224455667', code="000000", countryCode=86,
                      username='tester001', password="", confirmPassword=None,
                      proxyCode=None):
        self.request_session.headers.update({"device-id": deviceId})
        self.request_session.headers.update({"os-type": osType})
        response = self.request_session.post(web_host+"/v1/user/register",
                                             json={"mobile": mobile,
                                                   "code": code,
                                                   "countryCode": countryCode,
                                                   "username": username,
                                                   "password": password,
                                                   "confirmPassword": confirmPassword,
                                                   "proxyCode": proxyCode,
                                                   "deviceId": deviceId,
                                                   }
                                             )
        self.print_response(response)
        self.request_session.headers.update({"uid": str(response.json()['data']['userId'])})
        self.request_session.headers.update(
            {"token": str(response.json()['data']['token'])})
        return response.json()

    def user_send_code(self,  # 忘記密碼,發送驗證碼
                       username=None, telephone=None,
                       ):
        response = self.request_session.post(web_host+"/v1/user/sendCode",
                                             json={"username": username,
                                                   "telephone": telephone,
                                                   "captchaValidation": {
                                                       "channelName": "string",
                                                       "imgToken": "string"
                                                   }
                                                   }
                                             )
        self.print_response(response)
        return response.json()

    def reset_pwd(self, deviceId="123", osType="WEB",  # 用戶重設密碼
                  code=None,
                  username=None, telephone=None,
                  newPwd=None):

        self.request_session.headers.update({"device-id": deviceId})
        self.request_session.headers.update({"os-type": osType})
        response = self.request_session.put(web_host+"/v1/user/pwd",
                                            json={"username": username,
                                                  "telephone": telephone,
                                                  "newPwd": newPwd,
                                                  "code": code
                                                  }
                                            )
        self.print_response(response)
        return response.json()

    def mobile_login(self, deviceId="123", osType="WEB",  # 手機快捷登陸
                     telephone=None, code=None):

        self.request_session.headers.update({"device-id": deviceId})
        self.request_session.headers.update({"os-type": osType})

        response = self.request_session.post(web_host+"/v1/user/loginByMobile",
                                json={"telephone": telephone,
                                      "code": code,
                                      "captchaValidation": {
                                          "channelName": "string",
                                          "imgToken": "string"},
                                      },
                                params={}
                                )
        self.print_response(response)
        try:
            self.request_session.headers.update(
                {"uid": str(response.json()['data']['userId'])})
            self.request_session.headers.update(
                {"token": str(response.json()['data']['token'])})
        except:
            print("登入失敗")
        return response.json()
