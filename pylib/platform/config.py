# -*- coding: utf-8 -*-
from pylib.platform.platApiBase import PlatformAPI
from pylib.platform.wallet import WalletManage
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader
from utils.generate_utils import Make
import jsonpath
import json

env = EnvReader()
platform_host = env.PLATFORM_HOST


# 報表
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


# 電信商管理
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
    def edit_manage(self, plat_token=None, item: list = []):
        """
        範例
        [{"thirdPartyId":1,"countryCodeId":2},{"thirdPartyId":1,"countryCodeId":3,"weight":0}]
        """
        request_body = {
            "method": "put",
            "url": "/v1/countryCodeRelationManage",
            "json": item
        }

        response = self.send_request(**request_body)
        return response.json()


# 操作日誌
class ActionLog(PlatformAPI):
    # 查詢後台用戶操作登入日誌
    # 操作类型 : SELECT, OTHER, INSERT, UPDATE, DELETE, GRANT, EXPORT, IMPORT, FORCE, GEN_CODE, CLEAN
    def get_action_log(self, From=None, to=None, account=None, userName=None,
                       departmentId=None, ip=None, businessType=None, page=None, size=None):
        request_body = {
            "method": "get",
            "url": "/v1/actionLog",
            "parmas": KeywordArgument.body_data().update({"from": From})
        }
        response = self.send_request(**request_body)
        return response.json()


# 電話區碼管理
class CountryCodeManage(PlatformAPI):
    # 電話區碼查詢
    def get_country_code(self):
        request_body = {
            "method": "get",
            "url": "/v1/countryCodeManage"
        }
        response = self.send_request(**request_body)
        return response.json()

    # 修改電話區碼
    def edit_country_code(self, id=None, isDisplay=None, isDefault=None):
        request_body = {
            "method": "put",
            "url": "/v1/countryCodeManage",
            "json": [
                {"id": id,
                 "isDisplay": isDisplay,
                 "isDefault": isDefault
                 }
            ]
        }
        response = self.send_request(**request_body)
        return response.json()


# 語系管理
class PlatformLanguage(PlatformAPI):
    # 站點語系查詢
    def get_language(self):
        request_body = {
            "method": "get",
            "url": "/v1/platform/language"
        }
        response = self.send_request(**request_body)
        return response.json()


# 幣別管理
class PlatformCurrency(PlatformAPI):
    # 站點幣別上下架修改
    def edit_curreny(self, code=None, status=None):
        request_body = {
            "method": "put",
            "url": f"/v1/platform/currency/{code}",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 站點幣別管理查詢
    def get_curreny(self):
        request_body = {
            "method": "get",
            "url": "/v1/platform/currency"
        }
        response = self.send_request(**request_body)
        return response.json()

    # 站點幣別下拉選單(排序)
    def get_curreny_drop_down(self, currency=None):
        request_body = {
            "method": "get",
            "url": "/v1/platform/currency/dropDown",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()


# 站點後台動態資料
class DynamicData(PlatformAPI):
    # 編輯動態資料
    def edit_dynamic_data(self, id=None, name=None, key=None, value=None):
        request_body = {
            "method": "put",
            "url": f"/v1/dynamic-data/{id}",
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 刪除動態資料
    def delete_dynamic_data(self, id=None):
        request_body = {
            "method": "delete",
            "url": f"/v1/dynamic-data/{id}",
        }
        response = self.send_request(**request_body)
        return response.json()

    # 查詢動態資料 (模糊查詢)
    def get_dynamic_data(self, name=None, key=None, value=None, page=None, size=None):
        request_body = {
            "method": "get",
            "url": "/v1/dynamic-data",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 建立動態資料
    def add_dynamic_data(self, name=None, key=None, value=None):
        request_body = {
            "method": "post",
            "url": "/v1/dynamic-data",
            "json": {
                "name": name,
                "key": key,
                "value": json.dumps(value, ensure_ascii=False)
            }
        }
        response = self.send_request(**request_body)
        return response.json()

    # 確認動態資料
    def check_dynamic_data(self):
        jsdata = self.get_dynamic_data(key='auto_testing')
        ret = jsonpath.jsonpath(jsdata, "$..key")
        if ret is False:
            self.add_dynamic_data(name="測試資料", key="auto_testing", value={"test": "test"})


# 檔案上傳
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


# 基本配置
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


class Make_config_data(PlatformAPI):
    def make_action_log_data(self):
        plat_token = self.request_session.headers["token"]
        resp_Avatar = Avatar(token=plat_token)
        resp_Avatar.add_avatar(title='rttest', url='/rt/test')  # 新增頭像
        get_id = resp_Avatar.find_avatar_id()  # 取得頭像最後一個id

        resp_Avatar.delete_avatar(id=get_id)  # 製造刪除頭像紀錄

        water_clear_resp = WalletManage(token=plat_token)
        water_clear_resp.water_clear_all(userId=1, currency="CNY")  # 製造一鍵流水清零紀錄

        report_resp = Report(token=plat_token)
        report_resp.post_report_type(reportType="PLT_REPORT_USER_FINANCE_REPORT_DOWNLOAD")  # 製造導出紀錄
        return


class Domain(PlatformAPI):
    # 新增應用域名
    def add_domain(self, domain="http://" + Make.name(8) + ".com"):
        request_body = {
            "method": "post",
            "url": "/v1/application/domain",
            "json": {"domain": domain, "applicationType": [0],
                     "purchaseTime": "2023-07-14T09:03:05.310Z", "expiryTime": "2023-07-14T09:03:05.310Z"}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 應用域名列表
    def get_domain(self):
        request_body = {
            "method": "get",
            "url": "/v1/application/domain",
            "params": ""
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取域名 id
    def find_domain_id(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        response = self.get_domain()
        ret = jsonpath.jsonpath(response, "$..id")
        if ret is False:
            self.add_domain()
            response = self.get_domain()
            ret = jsonpath.jsonpath(response, "$..id")
        return ret[-1]


class AppVersion(PlatformAPI):
    # 新增 App 版本
    def add_app_version(self):
        request_body = {
            "method": "post",
            "url": "/v1/app/version",
            "json": {"version": "1.0.0", "title": "Automation Testing", "content": "Automation Testing",
                     "appType": 2, "osType": 3, "signType": 4, "url": "https://auto.com",
                     "isForce": True}
        }
        response = self.send_request(**request_body)
        return response.json()

    # App 版本列表
    def get_app_versions(self):
        request_body = {
            "method": "get",
            "url": "/v1/app/versions",
            "params": {"page": 1, "size": 20}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 獲取App 版本 id
    def find_app_version_id(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        response = self.get_app_versions()
        ret = jsonpath.jsonpath(response, "$..id")
        if ret is False:
            self.add_app_version()
            response = self.get_app_versions()
            ret = jsonpath.jsonpath(response, "$..id")
        return ret[0]

    def delete_app_version(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        app_version_id = self.find_app_version_id()
        request_body = {
            "method": "delete",
            "url": f"/v1/app/version/{app_version_id}",
        }

        response = self.send_request(**request_body)
        return response.json()
