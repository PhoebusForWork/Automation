# -*- coding: utf-8 -*-
import time
import jsonpath
from pylib.platform.platApiBase import PlatformAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader


env = EnvReader()
platform_host = env.PLATFORM_HOST


class PlatformInfo(PlatformAPI):
    # 取得平台資訊
    def get_platform_info(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/platform"
        }

        response = self.send_request(**request_body)
        return response.json()


class AccountAdmin(PlatformAPI):
    # 搜索帳號列表
    def search_admin_list(
            self, plat_token=None, account=None,
            displayName=None, phone=None, isLeader=None,
            deptId=None, status=None, deptIdList=None,
            roleIdList=None, startLoginTime=None, endLoginTime=None,
            isNonDept=None, page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/account/admin",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 新增帳號
    def add_admin(
            self, plat_token=None,
            account=None, password=None, phone=None,
            sipNum=None, fixSipNum=None, isLeader=None,
            deptId=None, roleIds=None, expiredTime=None, displayName=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/account/admin",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 帳號詳情
    def admin_info(self, plat_token=None, adminId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/account/admin/{adminId}",
            "params": {"adminId": adminId}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯帳號
    def edit_admin(
            self, plat_token=None, adminId=None,
            phone=None, sipNum=None,
            fixSipNum=None, isLeader=None,
            deptId=None, roleIds=None, expiredTime=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/account/admin/{adminId}",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 刪除帳號
    def delete_admin(self, plat_token=None, adminId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "delete",
            "url": f"/v1/account/admin/{adminId}",
            "params": {"adminId": adminId}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 帳號狀態修改, status: 0停用;1啟用;2刪除
    def admin_status(self, plat_token=None, adminId=None, status=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/account/admin/{adminId}/status",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        self.print_response(response)
        return response.json()

    # 修改密碼
    def edit_password(self, plat_token=None, oldPassword=None, newPassword=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/account/admin/password",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        self.print_response(response)
        return response.json()

    # 重置密碼
    def reset_password(self, plat_token=None, adminId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/account/admin/{adminId}/resetPassword",
            "params": {"adminId": adminId}
        }

        response = self.send_request(**request_body)
        return response.json()

    def add_account_auto(self, plat_token=None):
        now = time.time()
        auto_account = "auto" + str(int(now * 10))
        resp = self.add_admin(plat_token=plat_token, account=auto_account, password="abc123456",
                              isLeader=True, deptId='6', roleIds=['5'], displayName=auto_account)
        if resp["data"] == "success":
            return auto_account
        else:
            raise ValueError("創建帳號失敗")

    def find_admin_id(self, plat_token=None):
        response = self.search_admin_list(plat_token=plat_token, size=200)
        total = response['data']['total']
        size = response['data']['size']
        if total >= size:
            add_size = size + total
            response = self.search_admin_list(plat_token=plat_token, size=add_size)
        check_resp = "$.data.records[?(@.lastLoginTime == None).id]"
        admin_id = jsonpath.jsonpath(response, check_resp)
        return str(admin_id[-1])


class AccountAuthority(PlatformAPI):
    # 權限總列表
    def authority_list(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/account/authority/list"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 選單樹列表
    def authority_menu(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/account/authority/menu"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 權限列表
    def authority_permission(self, plat_token=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/account/authority/permission"
        }

        response = self.send_request(**request_body)
        return response.json()


class AccountDept(PlatformAPI):
    # 結點列表
    def dept_list(self, plat_token=None, roleId=None, departmentStatus=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/account/dept/list",
            "params": {"roleId": roleId, "departmentStatus": departmentStatus}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 人員關係列表
    def admin_list(
            self, plat_token=None, account=None,
            password=None, phone=None, sipNum=None,
            fixSipNum=None, isLeader=None, deptId=None,
            status=None, deptIdList=None, roleIdList=None,
            startLoginTime=None, endLoginTime=None, isNonDept=None,
            expiredTime=None, displayName=None, page=None, size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/account/dept/admin/list",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 新增節點
    def add_dept(self, plat_token=None, department=None, pid=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/account/dept",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 修改節點
    def edit_dept(self, plat_token=None, departmentId=None, department=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/account/dept/{departmentId}",
            "json": {"department": department},
            "params": {"departmentId": departmentId}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 刪除節點
    def delete_dept(self, plat_token=None, departmentId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "delete",
            "url": f"/v1/account/dept/{departmentId}",
            "params": {"departmentId": departmentId}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 設置負責人
    def dept_leader(self, plat_token=None, adminId=None, isLeader=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/account/dept/leader",
            "json": {"adminId": adminId, "isLeader": isLeader}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 關聯已存在帳號
    def dept_admin(self, plat_token=None, adminIdList=None, departmentId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/account/dept/admin",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 解除關聯
    def delete_dept_admin(self, plat_token=None, adminId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/account/dept/leader",
            "params": {"adminId": adminId}
        }

        response = self.send_request(**request_body)
        return response.json()

    def find_dept_id(self, plat_token=None):
        response = self.dept_list(plat_token=plat_token)
        dept_id = jsonpath.jsonpath(response, "$..id")
        return str(dept_id[-1])


class AccountRole(PlatformAPI):
    # 角色列表
    def role_list(self, plat_token=None, role=None, authorityId=None, departmentId=None, page=None, size=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/account/role/list",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 創建角色
    def add_role(self, plat_token=None, role=None, remark=None, authorityIds=None, departmentIds=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/account/role",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯角色
    def edit_role(
            self, plat_token=None, role_id=None, role=None,
            remark=None, authorityIds=None, departmentIds=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/account/role/{role_id}",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 角色狀態
    def role_status(self, plat_token=None, role_id=None, status=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/account/role/{role_id}/status",
            "json": {"status": status}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 顯示角色權限
    def role_authorities(self, plat_token=None, roleId=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/account/role/{roleId}/authorities",
            "params": {"roleId": roleId}
        }

        response = self.send_request(**request_body)
        return response.json()

    def find_role_id(self, plat_token=None):
        response = self.role_list(plat_token=plat_token, size=10,)
        total = response['data']['total']
        size = response['data']['size']
        if total >= size:
            add_size = size + total
            response = self.role_list(plat_token=plat_token, size=add_size)
        role_id = jsonpath.jsonpath(response, "$..id")
        return str(role_id[-1])
