from ..client_side.webApiBase import WebAPI
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
    def valid_sms(self, device=None, requestType=None):
        request_body = {
            "method": "post",
            "url": "/v1/validation/sms",
            "json": KeywordArgument.body_data()
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
