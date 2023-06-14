# -*- coding: utf-8 -*-
from pylib.platform.platApiBase import PlatformAPI
from pylib.platform.wallet import WalletManage
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader
from utils.generate_utils import Make
import jsonpath

env = EnvReader()
platform_host = env.PLATFORM_HOST


class File(PlatformAPI):
    # 上傳影片
    def upload_video(self, plat_token=None, file=None, videoPathType=None):
        self.request_session.headers.update({"Content-Type": None})
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/file/video",
            "params": {"videoPathType": videoPathType},
            "files": file
        }

        response = self.send_request(**request_body)
        return response.json()

    # 上傳圖片, imagePathType: 1:game|2:activity|3:avatar
    def upload_image(self, plat_token=None, file=None, imagePathType=None):
        self.request_session.headers.update({"Content-Type": None})
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/file/image",
            "params": {"imagePathType": imagePathType},
            "files": file
        }

        response = self.send_request(**request_body)
        return response.json()


class Avatar(PlatformAPI):
    # 新增頭像
    def add_avatar(self, plat_token=None, title=None, url=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/config/avatar",
            "json": {"title": title, "url": url}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 修改頭像
    def edit_avatar(self, plat_token=None, title=None, url=None, id=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/config/avatar",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 刪除頭像
    def delete_avatar(self, id: str = None):
        request_body = {
            "method": "delete",
            "url": f"/v1/config/avatar/{id}"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 依頭像ID進行查詢
    def get_avatar_one(self, plat_token=None, id: str = None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/config/avatar/{id}"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 依條件進行查詢
    def get_avatar(self, plat_token=None, title=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/config/avatars",
            "params": {"title": title}
        }

        response = self.send_request(**request_body)
        return response.json()

    def find_avatar_id(self, ):
        response = self.get_avatar()
        dept_id = jsonpath.jsonpath(response, "$..id")
        return str(dept_id[-1])

    # 獲取可刪除頭像
    def get_delete_avatar(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        response = self.get_avatar(title="待刪除頭像")
        ret = jsonpath.jsonpath(response, "$..id")
        if ret is False:
            self.add_avatar(title="待刪除頭像", url="justForTest")
            response = self.get_avatar(title="待刪除頭像")
            ret = jsonpath.jsonpath(response, "$..id")
        return ret[-1]


class CountryCodeRelation(PlatformAPI):
    # 電信商查詢
    def get_manage(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/countryCodeRelationManage"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 修改電信商
    def edit_manage(self, plat_token=None, thirdPartyId=None, countryCodeId=None, weight=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/countryCodeRelationManage",
            "json": [
                {"thirdPartyId": thirdPartyId,
                 "countryCodeId": countryCodeId,
                 "weight": weight
                 }
            ]
        }

        response = self.send_request(**request_body)
        return response.json()


class Report(PlatformAPI):
    def post_report_type(self, reportType=None):
        request_body = {
            "method": "post",
            "url": f"/v1/report/{reportType}",
            "json":
                {"startTime": Make.date('start'),
                 "endTime": Make.date('end'),
                 "currency": "CNY"
                 }
        }
        response = self.send_request(**request_body)
        return response.json()

    def get_report_download(self, id=None, reportType=None):
        request_body = {
            "method": "get",
            "url": "/v1/report/",
            "params": [
                {"id": id,
                 "reportType": reportType,
                 }]
        }
        response = self.send_request(**request_body)
        return response.json()


class Make_config_data(PlatformAPI):
    def make_action_log_data(self, plat_token=None,):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})
        resp_Avatar = Avatar(token=plat_token)
        resp_Avatar.add_avatar(title='rttest', url='/rt/test')  # 新增頭像
        get_id = resp_Avatar.find_avatar_id()  # 取得頭像最後一個id

        resp_Avatar.delete_avatar(id=get_id)  # 製造刪除頭像紀錄

        water_clear_resp = WalletManage(token=plat_token)
        water_clear_resp.water_clear_all(userId=1, currency="CNY")  # 製造一鍵流水清零紀錄

        report_resp = Report(token=plat_token)
        report_resp.post_report_type(reportType="PLT_REPORT_USER_FINANCE_REPORT_DOWNLOAD")  # 製造導出紀錄
        return
