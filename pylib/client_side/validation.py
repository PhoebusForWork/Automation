from ..client_side.webApiBase import WebAPI
from ..client_side.user import Security
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader

env = EnvReader()
web_host = env.WEB_HOST


class Validation(WebAPI):
    # 取得圖形驗證廠商
    def valid_captcha(self):
        request_body = {
            "method": "get",
            "url": "/v1/validation/captcha"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 1:註冊, 2:手機快捷登陸, 3:重設密碼, 4:撞庫驗證, 5:原手機號解綁, 6:綁定新手機號, 7:原郵箱地址解綁, 8:綁定新郵箱地址

    # 發送郵箱驗證訊息
    def valid_email(self, device=None, requestType=None):
        request_body = {
            "method": "post",
            "url": "/v1/validation/email",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 發送短信驗證訊息
    # 請求種類 1:註冊, 2:手機快捷登陸, 3:重設密碼, 4:撞庫驗證, 5:原手機號解綁, 6:綁定新手機號, 7:原郵箱地址解綁, 8:綁定新郵箱地址, 9:提款短信驗證
    # def valid_sms(self, requestType=None, mobile=None, countryCode=None, channelName=None, imgToken=None):
    def valid_sms(self, mobile=None, requestType=None, countryCode=None, uuid=None):
        request_body = {
            "method": "post",
            "url": "/v1/validation/sms",
            "json": {
                      "requestType": requestType,
                      "mobile": mobile,
                      "countryCode": countryCode,
                      "uuid": uuid,
                      "captchaValidation": {
                          "channelName": "string",
                          "imgToken": "string"
                      }
                # {
                #     "channelName": channelName,
                #     "imgToken": imgToken
                # }
            }
        }
        response = self.send_request(**request_body)
        return response.json()

    # 發送短信驗證訊息
    def valid_voice(self, device=None, requestType=None):
        request_body = {
            "method": "post",
            "url": "/v1/validation/voice",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    def build_all_valid(self):
        # 請求種類 1:註冊, 2:手機快捷登陸, 3:重設密碼, 4:撞庫驗證, 5:原手機號解綁, 6:綁定新手機號, 7:原郵箱地址解綁, 8:綁定新郵箱地址, 9:提款短信驗證
        no_phone_type = [1, 2, 3, 4, 5, 6, 7, 8]
        for Type in no_phone_type:
            self.valid_sms(mobile='987654321', requestType=Type, countryCode=66, uuid=123)
        if self.request_session.headers['telephone'] is None:
            bind = Security(token=self.request_session.headers['token'])
            bind.mobile_binding(countryCode=66, mobile='987654321', code='000000')
