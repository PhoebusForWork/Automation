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

class userSecurity(WEB_API):
    
    def getSecurityInfo(self): # 取得用戶安全中心資訊
        # self.ws = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ws.get(web_host+"/v1/user/security/info" ,
                                json = {},
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def emailBind(self,email=None,code=None): # 綁定郵箱地址
        # self.ws = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ws.put(web_host+"/v1/user/security/email/binding" ,
                                json = {
                                        "email": email,
                                        "code": code
                                        },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def emailUnbind(self,code=None): # 解綁郵箱地址
        # self.ws = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ws.put(web_host+"/v1/user/security/email/unbind" ,
                                json = {
                                        "code": code
                                        },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editMobile(self,newMobile=None,nmCode=None,omCode=None): # 更換手機號
        # self.ws = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ws.put(web_host+"/v1/user/security/mobile" ,
                                json = {
                                        "newMobile": newMobile,
                                        "nmCode": nmCode,
                                        "omCode": omCode
                                        },
                                params = {}
        )
        self._printresponse(response)
        return response.json()

    def editPwd(self,newPwd=None,oldPwd=None): #修改密碼
        # self.ws = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ws.put(web_host+"/v1/user/security/pwd" ,
                                json = {
                                        "newPwd": newPwd,
                                        "oldPwd": oldPwd,
                                        },
                                params = {}
        )
        self._printresponse(response)
        return response.json()