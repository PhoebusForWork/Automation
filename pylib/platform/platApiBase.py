# -*- coding: utf-8 -*-
import requests
import json
import datetime
# import sign #單獨執行python時使用
# from ..website import sign #執行RF時使用
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')  # 在rf_api_test層執行時使用
# config.read('../../config/config.ini') #在website路徑執行時使用
platfrom_host = config['host']['platform_host']


class PLAT_API:

    def __init__(self):

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

    def _printresponse(self, response):  # 印出回傳
        print('\n\n--------------HTTPS response  *  begin ------------------')
        print(response.status_code)

        for k, v in response.headers.items():
            print(f'{k};{v}')

        print('')
        printR = json.loads(response.text)
        print(json.dumps(printR, sort_keys=True, indent=4,
              separators=(',', ': '), ensure_ascii=False))
        # print(response.content.decode('utf-8'))
        print('--------------HTTPS response  *  end ------------------\n\n')

    def firstLoginPassword(self, username='phoebusliu', oldPassword='abc123456', newPassword='abc123456'):  # 新帳戶更新密碼
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
        # self.ps.headers.update({"uid":str(response.json()['data']['adminId'])})
        # self.ps.headers.update({"token":str(response.json()['data']['token'])})
        # print(response.json()['data']['token'])
        return response.json()

    def Login(self, username='phoebusliu', password='abc123456', imgCode='a'):  # 用戶登陸
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
        # print(response.json()['data']['token'])
        # return response.json()
        return response

    def LogOut(self, platToken=None):  # 用戶登陸
        if platToken != None:
            self.ps.headers.update({"token": platToken})
        self.s = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ps.post(platfrom_host+"/v1/account/logout",
                                json={},
                                )
        # self._printresponse(response)
        # self.ps.headers.update({"uid":str(response.json()['data']['adminId'])})
        # self.ps.headers.update({"token":str(response.json()['data']['token'])})
        # print(response.json()['data']['token'])
        return response.json()

    def ImgCode(self, uuid=124):  # 獲取驗證碼
        self.s = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ps.post(platfrom_host+"/v1/account/login/imgCode",
                                json={
                                },
                                params={
                                    "uuid": uuid,
                                },
                                )
        # self._printresponse(response)
        # self.ps.headers.update({"uid":str(response.json()['data']['adminId'])})
        # self.ps.headers.update({"token":str(response.json()['data']['token'])})
        # print(response.json()['data'])
        return response.json()['data']['code']


if __name__ == "__main__":
    pass
