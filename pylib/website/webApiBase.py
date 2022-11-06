# -*- coding: utf-8 -*-
import requests
import json
import datetime
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')  # 在rf_api_test層執行時使用
web_host = config['host']['web_host']
platfrom_host = config['host']['platform_host']


class WEB_API:

    def __init__(self):

        self.timestemp = str(int(datetime.datetime.now().timestamp()))
        self.ws = requests.Session()
        self.ws.headers = {
            "timestamp": self.timestemp,
            "os-type": "WEB",
            "appType": "0",
            "uid": "",
            "device_id": "3263782594",
            "token": None,
            "version": "1.0",
            "env_auth": "vs",
            "accept": "*/*",
            "Content-Type": "application/json"
        }

    def _printresponse(self, response):  # 印出回傳
        print('\n\n--------------HTTPS response  *  begin ------------------')
        print(response.status_code)

        for k, v in response.headers.items():
            print(f'{k};{v}')

        print('')
        printR = json.loads(response.text)
        print(json.dumps(printR, sort_keys=True, indent=4,
              separators=(',', ': '), ensure_ascii=False))
        print('--------------HTTPS response  *  end ------------------\n\n')

    def Login(self, deviceId="123", osType="WEB", username='qwe220805', password='abc123456', code=None):

        timestemp = str(int(datetime.datetime.now().timestamp()))
        self.ws.headers.update({"device-id": deviceId})
        self.ws.headers.update({"os-type": osType})

        response = self.ws.post(web_host+"/v1/user/login",
                                json={
                                    "username": username,
                                    "pwd": password,
                                    "captchaValidation": {
                                        "channelName": "string",
                                        "imgToken": "string"
                                    },
                                    "code": code
                                },
                                params={}

                                )
        self._printresponse(response)
        try:
            self.ws.headers.update(
                {"token": str(response.json()['data']['token'])})
        except:
            print("登錄失敗")
        return response

    def logout(self):  # 登出

        response = self.ws.post(web_host+"/v1/user/logout",
                                json={},
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def userRegister(self, deviceId="123", osType="WEB",  # 註冊帳號
                     mobile='13224455667', code="000000", countryCode=86,
                     username='tester001', password="", confirmPassword=None,
                     proxyCode=None):

        self.ws.headers.update({"device-id": deviceId})
        self.ws.headers.update({"os-type": osType})
        response = self.ws.post(web_host+"/v1/user/register",
                                json={
                                    "mobile": mobile,
                                    "code": code,
                                    "countryCode": countryCode,
                                    "username": username,
                                    "password": password,
                                    "confirmPassword": confirmPassword,
                                    "proxyCode": proxyCode,
                                    "deviceId": deviceId,
                                }
                                )
        self._printresponse(response)
        self.ws.headers.update({"uid": str(response.json()['data']['userId'])})
        self.ws.headers.update(
            {"token": str(response.json()['data']['token'])})
        return response.json()

    def userSendCode(self,  # 忘記密碼,發送驗證碼
                     username=None, telephone=None,
                     ):
        response = self.ws.post(web_host+"/v1/user/sendCode",
                                json={
                                    "username": username,
                                    "telephone": telephone,
                                    "captchaValidation": {
                                        "channelName": "string",
                                        "imgToken": "string"
                                    }
                                }
                                )
        self._printresponse(response)
        return response.json()

    def resetPwd(self, deviceId="123", osType="WEB",  # 用戶重設密碼
                 code=None,
                 username=None, telephone=None,
                 newPwd=None):

        self.ws.headers.update({"device-id": deviceId})
        self.ws.headers.update({"os-type": osType})
        response = self.ws.put(web_host+"/v1/user/pwd",
                               json={
                                        "username": username,
                                        "telephone": telephone,
                                        "newPwd": newPwd,
                                        "code": code
                               }
                               )
        self._printresponse(response)
        return response.json()

    def mobileLogin(self, deviceId="123", osType="WEB",  # 手機快捷登陸
                    telephone=None, code=None):

        self.ws.headers.update({"device-id": deviceId})
        self.ws.headers.update({"os-type": osType})

        response = self.ws.post(web_host+"/v1/user/loginByMobile",
                                json={
                                    "telephone": telephone,
                                    "code": code,
                                    "captchaValidation": {
                                        "channelName": "string",
                                        "imgToken": "string"
                                    },
                                },
                                params={}
                                )
        self._printresponse(response)
        try:
            self.ws.headers.update(
                {"uid": str(response.json()['data']['userId'])})
            self.ws.headers.update(
                {"token": str(response.json()['data']['token'])})
        except:
            print("登入失敗")
        return response.json()
