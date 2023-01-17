from re import M
import datetime
import configparser
from ..client_side.webApiBase import WEB_API  # 執行RF時使用


config = configparser.ConfigParser()
config.read('config/config.ini')
web_host = config['host']['web_host']
platfrom_host = config['host']['platform_host']


class validation(WEB_API):

    def valid_captcha(self):  # 取得圖形驗證廠商
        response = self.ws.get(web_host+"/v1/validation/captcha",
                               data={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    # 1:註冊, 2:手機快捷登陸, 3:重設密碼, 4:撞庫驗證, 5:原手機號解綁, 6:綁定新手機號, 7:原郵箱地址解綁, 8:綁定新郵箱地址

    def valid_email(self, device=None, requestType=None):  # 發送郵箱驗證訊息
        response = self.ws.post(web_host+"/v1/validation/email",
                                json={
                                    "device": device,
                                    "requestType": requestType,
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def valid_sms(self, device=None, requestType=None):  # 發送短信驗證訊息
        response = self.ws.post(web_host+"/v1/validation/sms",
                                json={
                                    "device": device,
                                    "requestType": requestType,
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def valid_voice(self, device=None, requestType=None):  # 發送短信驗證訊息
        response = self.ws.post(web_host+"/v1/validation/voice",
                                json={
                                    "device": device,
                                    "requestType": requestType,
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()
