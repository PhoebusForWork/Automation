from re import M
import requests
import json
import datetime
# import sign
from ..website import sign
import configparser
from ..website.webApiBase import WEB_API #執行RF時使用


config = configparser.ConfigParser()
config.read('config/config.ini')
web_host = config['host']['web_host']
platfrom_host = config['host']['platfrom_host']

class userDetail(WEB_API):
    
    def getDetail(self): # 取得圖形驗證廠商
        # self.ws = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ws.get(web_host+"/v1/user/detail" ,
                                data = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editDetail(self,avatar=None,nickname=None,birthday=None,sex=None): # 取得圖形驗證廠商
        # self.ws = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ws.put(web_host+"/v1/user/detail" ,
                                json = {
                                        "avatar": avatar,
                                        "nickname": nickname,
                                        "birthday": birthday,
                                        "sex": sex
                                        },
                                params = {}
        )
        self._printresponse(response)
        return response.json()