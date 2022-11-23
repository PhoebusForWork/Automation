# -*- coding: utf-8 -*-
import requests
import json
import inspect
import datetime
# import sign #單獨執行python時使用
# from ..website import sign #執行RF時使用
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')  # 在rf_api_test層執行時使用
# config.read('../../config/config.ini') #在website路徑執行時使用
platfrom_host = config['host']['platform_host']
cs_host = config["host"]['web_host']


class API_Controller:

    def __init__(self):

        self.timestamp = str(int(datetime.datetime.now().timestamp()))
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

    def HttpsClient(self, reqMethod, reqUrl, json, params, token=None):
        if token != None:
            self.ps.headers.update({"token": str(token)})
        if reqMethod == 'post':
            response = self.ps.post(
                platfrom_host+reqUrl, json=json, params=params)
        elif reqMethod == 'put':
            response = self.ps.put(platfrom_host+reqUrl,
                                   json=json, params=params)
        elif reqMethod == 'get':
            response = self.ps.get(platfrom_host+reqUrl,
                                   json=json, params=params)
        elif reqMethod == 'delete':
            response = self.ps.delete(
                platfrom_host+reqUrl, json=json, params=params)
        else:
            response = "沒有符合的請求模式"
        self._printresponse(response)
        return response


class Cs_API_Controller:

    def __init__(self):

        self.timestamp = str(int(datetime.datetime.now().timestamp()))

        self.cs = requests.Session()
        self.cs.headers = {
            "os_type": "0",
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

    def HttpsClient(self, reqMethod, reqUrl, json, params, token=None):
        if token is not None:
            self.cs.headers.update({"token": str(token)})
        if reqMethod == 'post':
            response = self.cs.post(cs_host+reqUrl,
                                    json=json, params=params)
        elif reqMethod == 'put':
            response = self.cs.put(cs_host+reqUrl,
                                   json=json, params=params)
        elif reqMethod == 'get':
            response = self.cs.get(cs_host+reqUrl,
                                   json=json, params=params)
        elif reqMethod == 'delete':
            response = self.cs.delete(cs_host+reqUrl,
                                      json=json, params=params)
        else:
            response = "沒有符合的請求模式"
        self._printresponse(response)
        return response


class KeywordArgument:

    @staticmethod
    def body_data():
        caller = inspect.stack()[1][0]
        args, _, _, values = inspect.getargvalues(caller)
        r = dict()
        for i in args:
            r[i] = values[i]
        return r


if __name__ == "__main__":
    pass
