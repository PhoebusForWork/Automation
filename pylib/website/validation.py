from re import M
import datetime
import configparser
from ..website.webApiBase import WEB_API  # 執行RF時使用


config = configparser.ConfigParser()
config.read('config/config.ini')
web_host = config['host']['web_host']
platfrom_host = config['host']['platform_host']


class validation(WEB_API):

    def validCaptcha(self):  # 取得圖形驗證廠商
        # self.ws = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ws.get(web_host+"/v1/validation/captcha",
                               data={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    # 1:註冊, 2:手機快捷登陸, 3:重設密碼, 4:撞庫驗證, 5:原手機號解綁, 6:綁定新手機號, 7:原郵箱地址解綁, 8:綁定新郵箱地址

    def validEmail(self, device=None, requestType=None):  # 發送郵箱驗證訊息
        # self.ws = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ws.post(web_host+"/v1/validation/email",
                                json={
                                    "device": device,
                                    "requestType": requestType,
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def validSms(self, device=None, requestType=None):  # 發送短信驗證訊息
        # self.ws = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ws.post(web_host+"/v1/validation/sms",
                                json={
                                    "device": device,
                                    "requestType": requestType,
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def validVoice(self, device=None, requestType=None):  # 發送短信驗證訊息
        # self.ws = requests.Session()
        timestemp = str(int(datetime.datetime.now().timestamp()))
        response = self.ws.post(web_host+"/v1/validation/voice",
                                json={
                                    "device": device,
                                    "requestType": requestType,
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()
