# -*- coding: utf-8 -*-
from pylib.client_side.webApiBase import WebAPI
from utils.data_utils import EnvReader
from utils.api_utils import KeywordArgument as KA

env = EnvReader()
web_host = env.WEB_HOST


# APP版本
class App(WebAPI):
    # 檢查是否有版本更新
    def get_new_version(self, os_type=None, app_type=None, version=None):
        request_body = {
            "method": "get",
            "url": "/v1/app/new/version",
            "params": {"os-type": os_type, "appType": app_type, "version": version}
        }
        response = self.send_request(**request_body)
        return response.json()

    # 最新的版本資訊
    def get_last_version(self, os_type=None, app_type=None):
        request_body = {
            "method": "get",
            "url": "/v1/app/last/version",
            "params": {"os-type": os_type, "appType": app_type}
        }
        response = self.send_request(**request_body)
        return response.json()


# 檔案上傳
class File(WebAPI):
    # 上傳影片
    def upload_video(self, videoPathType):
        request_body = {
            "method": "post",
            "url": "/v1/file/video",
            "params": {"videoPathType": videoPathType},
        }
        response = self.send_request(**request_body)
        return response.json()

    # 上傳圖片
    def upload_image(self, imagePathType, file):
        request_body = {
            "method": "post",
            "url": "/v1/file/image",
            "params": {"imagePathType": imagePathType},
            "json": {"file": file}
        }
        response = self.send_request(**request_body)
        return response.json()


# 基本配置
class Config(WebAPI):
    # 取得預設可用語系列表(無須登入)
    def get_language(self):
        request_body = {
            "method": "get",
            "url": "/v1/config/language"
        }
        response = self.send_request(**request_body)
        return response.json()

    # 取得動態資料 (無須登入)
    def get_dynamic_data(self, keys: list):
        request_body = {
            "method": "get",
            "url": "/v1/config/dynamic-data",
            "params": KA.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 取得預設可用幣別列表(無須登入)
    def get_currency(self):
        request_body = {
            "method": "get",
            "url": "/v1/config/currency"
        }
        response = self.send_request(**request_body)
        return response.json()

    # 頭像連結列表
    def get_avatar_urls(self):
        request_body = {
            "method": "get",
            "url": "/v1/config/avatar/urls"
        }
        response = self.send_request(**request_body)
        return response.json()


# 站點配置
class Website(WebAPI):
    # 站點配置圖片
    def get_icon(self, language):
        request_body = {
            "method": "get",
            "url": "/v1/website/icon",
            "params": KA.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()


# 站點錯誤碼
class BasicsErrorCode(WebAPI):
    # 確認版號取得最新錯誤碼(比對現在版本)
    def get_latest_version(self, version, language):
        request_body = {
            "method": "get",
            "url": f"/v1/basics/errorCode/version/{version}",
            "params": {"language": language}
        }
        response = self.send_request(**request_body)
        return response.json()

    # 確認版號取的最新錯誤(直接拿最新)
    def get_version(self, version, language):
        request_body = {
            "method": "get",
            "url": "/v1/basics/errorCode/version",
            "params": {"language": language}
        }
        response = self.send_request(**request_body)
        return response.json()
