# -*- coding: utf-8 -*-
import requests
import json
import inspect
import datetime
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')
platfrom_host = config['host']['platform_host']
cs_host = config["host"]['web_host']


class API_Controller:

    def __init__(self, platfrom='plt'):

        self.timestamp = str(int(datetime.datetime.now().timestamp()))
        self.s = requests.Session()
        # 這邊字串轉為dict要使用eval不可用dict會掛
        self.s.headers = eval(config["API_headers"][platfrom])
        if platfrom == 'plt':
            self.host = config["host"]['platform_host']
        elif platfrom == 'xxl':
            self.host = config["host"]['xxl_host']
        else:
            self.host = config["host"]['web_host']

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
        if token is not None:
            self.s.headers.update({"token": str(token)})
        if reqMethod == 'post':
            response = self.s.post(
                self.host+reqUrl, json=json, params=params)
        elif reqMethod == 'put':
            response = self.s.put(
                self.host+reqUrl, json=json, params=params)
        elif reqMethod == 'get':
            response = self.s.get(self.host+reqUrl,
                                  json=json, params=params)
        elif reqMethod == 'delete':
            response = self.s.delete(
                self.host+reqUrl, json=json, params=params)
        else:
            response = "沒有符合的請求模式"
        self._printresponse(response)
        return response


class KeywordArgument:

    @staticmethod
    def body_data(filter=['self', 'plat_token']):
        caller = inspect.stack()[1][0]
        args, _, _, values = inspect.getargvalues(caller)
        r = dict()
        for i in args:
            if i not in filter and values[i] is not None:
                r[i] = values[i]
        return r


if __name__ == "__main__":
    pass
