# -*- coding: utf-8 -*-
import requests
import json
import datetime
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')
platfrom_host = config['host']['platform_host']


class PLAT_API:

    def __init__(self, token=None):

        self.timestemp = str(int(datetime.datetime.now().timestamp()))
        self.ps = requests.Session()
        self.ps.headers = {
            "Connection": "keep-alive",
            "Content-Length": "64",
            "os_type": "0",
            "device_id": "3263782594",
            "version": "1.0",
            "sign": "0fc750ae19a42db64dff8c57aec07f07",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "timestamp": "1636102887000"
        }
        if token:
            self.ps.headers.update({"token": token})

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

    def first_login_password(self, username='phoebusliu', oldPassword='abc123456', newPassword='abc123456'):  # 新帳戶更新密碼
        self.s = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ps.put(platfrom_host+"/v1/account/login/resetPassword",
                               json={
                                   "account": username,
                                   "oldPassword": oldPassword,
                                   "newPassword": newPassword,
                                   "loginIp": "string"
                               },
                               )
        self._printresponse(response)
        return response.json()

    def login(self, username='phoebusliu', password='abc123456', imgCode='a'):  # 用戶登陸
        self.s = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ps.post(platfrom_host+"/v1/account/login",
                                json={
                                    "account": username,
                                    "password": password,
                                    "imgCode": imgCode,
                                    "uuid": "124"
                                },
                                )
        self._printresponse(response)
        # self.ps.headers.update({"uid":str(response.json()['data']['adminId'])})
        try:
            self.ps.headers.update(
                {"token": str(response.json()['data']['token'])})
        except:
            print("登入失敗")
        return response

    def logout(self, plat_token=None):  # 用戶登陸
        if plat_token != None:
            self.ps.headers.update({"token": plat_token})
        self.s = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ps.post(platfrom_host+"/v1/account/logout",
                                json={},
                                )
        return response.json()

    def imgcode(self, uuid=124):  # 獲取驗證碼
        self.s = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ps.post(platfrom_host+"/v1/account/login/imgCode",
                                json={
                                },
                                params={
                                    "uuid": uuid,
                                },
                                )
        return response.json()['data']['code']


if __name__ == "__main__":
    pass
