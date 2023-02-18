# -*- coding: utf-8 -*-
from utils.data_utils import EnvReader
from utils.api_utils import API_Controller


env = EnvReader()
platform_host = env.PLATFORM_HOST


class PlatformAPI(API_Controller):
    def __init__(self):
        super().__init__(platform='plt')

    def first_login_password(self, username='phoebusliu', oldPassword='abc123456', newPassword='abc123456'):  # 新帳戶更新密碼
        response = self.request_session.put(platform_host+"/v1/account/login/resetPassword",
                               json={
                                   "account": username,
                                   "oldPassword": oldPassword,
                                   "newPassword": newPassword,
                                   "loginIp": "string"
                               },
                               )
        self.print_response(response)
        return response.json()

    def login(self, username='phoebusliu', password='abc123456', imgCode='a'):  # 用戶登陸
        response = self.request_session.post(platform_host+"/v1/account/login",
                                json={
                                    "account": username,
                                    "password": password,
                                    "imgCode": imgCode,
                                    "uuid": "124"
                                },
                                )
        self.print_response(response)
        try:
            self.request_session.headers.update(
                {"token": str(response.json()['data']['token'])})
        except:
            print("登入失敗")
        return response

    def logout(self, platform_token=None):  # 用戶登陸
        if platform_token is not None:
            self.request_session.headers.update({"token": platform_token})
        response = self.request_session.post(platform_host+"/v1/account/logout",
                                json={},
                                )
        return response.json()

    def imgcode(self, uuid=124):  # 獲取驗證碼
        response = self.request_session.post(platform_host+"/v1/account/login/imgCode",
                                json={
                                },
                                params={
                                    "uuid": uuid,
                                },
                                )
        return response.json()['data']['code']


if __name__ == "__main__":
    pass
