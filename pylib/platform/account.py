# -*- coding: utf-8 -*-
import time
import jsonpath
from pylib.platform.platApiBase import PlatformAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader


env = EnvReader()
platform_host = env.PLATFORM_HOST


class AccountAdmin(PlatformAPI):
    # 搜索帳號列表
    def search_admin_list(
            self,
            plat_token=None,
            account=None,
            display_name=None,
            phone=None,
            is_leader=None,
            dept_id=None,
            status=None,
            dept_id_list=None,
            role_id_list=None,
            start_login_time=None,
            end_login_time=None,
            is_non_dept=None,
            page=None,
            size=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/account/admin",
            "params": {
                "account": account,
                "displayName": display_name,
                "phone": phone,
                "isLeader": is_leader,
                "deptId": dept_id,
                "status": status,
                "deptIdList": dept_id_list,
                "roleIdList": role_id_list,
                "startLoginTime": start_login_time,
                "endLoginTime": end_login_time,
                "isNonDept": is_non_dept,
                "page": page,
                "size": size
            }
        }

        response = self.send_request(**request_body)
        return response.json()

    # 新增帳號
    def add_admin(
            self,
            plat_token=None,
            account=None,
            password=None,
            phone=None,
            sip_num=None,
            fix_sip_num=None,
            is_leader=None,
            dept_id=None,
            role_ids=None,
            expired_time=None,
            display_name=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/account/admin",
            "json": {
                "phone": phone,
                "sipNum": sip_num,
                "fixSipNum": fix_sip_num,
                "isLeader": is_leader,
                "deptId": dept_id,
                "roleIds": role_ids,
                "expiredTime": expired_time,
                "account": account,
                "password": password,
                "displayName": display_name
            }
        }

        response = self.send_request(**request_body)
        return response.json()

    # 帳號詳情
    def admin_info(self, plat_token=None, admin_id=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/account/admin/{format(admin_id)}",
            "params": {"adminId": admin_id}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯帳號
    def edit_admin(
            self,
            plat_token=None,
            admin_id=None,
            phone=None,
            sip_num=None,
            fix_sip_num=None,
            is_leader=None,
            dept_id=None,
            role_ids=None,
            expired_time=None
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/account/admin/{format(admin_id)}",
            "json": {
                "phone": phone,
                "sipNum": sip_num,
                "fixSipNum": fix_sip_num,
                "isLeader": is_leader,
                "deptId": dept_id,
                "roleIds": role_ids,
                "expiredTime": expired_time
            },
            "params": {"adminId": admin_id}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 刪除帳號
    def delete_admin(self, plat_token=None, admin_id=None, ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "delete",
            "url": f"/v1/account/admin/{format(admin_id)}",
            "params": {"adminId": admin_id}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 帳號狀態修改, status: 0停用;1啟用;2刪除
    def admin_status(self, plat_token=None, admin_id=None, status=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/account/admin/{format(admin_id)}/status",
            "params": {"adminId": admin_id, "status": status}
        }

        response = self.send_request(**request_body)
        self.print_response(response)
        return response.json()

    # 修改密碼
    def edit_password(self, plat_token=None, old_password=None, new_password=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/account/admin/password",
            "json": {"oldPassword": old_password, "newPassword": new_password}
        }

        response = self.send_request(**request_body)
        self.print_response(response)
        return response.json()

    # 重置密碼
    def reset_password(self, plat_token=None, admin_id=None, ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/account/admin/{format(admin_id)}/resetPassword",
            "params": {"adminId": admin_id}
        }

        response = self.send_request(**request_body)
        return response.json()

    def add_account_auto(self, plat_token=None):
        now = time.time()
        auto_account = "auto" + str(int(now * 10))
        resp = self.add_admin(plat_token=plat_token, account=auto_account, password="abc123456",
                              is_leader=True, dept_id='6', role_ids=['5'], display_name=auto_account)
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
    def authority_list(self, plat_token=None,):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/account/authority/list"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 選單樹列表
    def authority_menu(self, plat_token=None,):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/account/authority/menu"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 權限列表
    def authority_permission(self, plat_token=None,):
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
    def dept_list(self, plat_token=None, role_id=None, department_status=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/account/dept/list",
            "params": {"roleId": role_id, "departmentStatus": department_status}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 人員關係列表
    def admin_list(
            self,
            plat_token=None,
            account=None,
            password=None,
            phone=None,
            sipNum=None,
            fixSipNum=None,
            isLeader=None,
            deptId=None,
            status=None,
            deptIdList=None,
            roleIdList=None,
            startLoginTime=None,
            endLoginTime=None,
            isNonDept=None,
            expiredTime=None,
            displayName=None,
            page=None,
            size=None,
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
    def add_dept(self, plat_token=None, department=None, pid=None,):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/account/dept",
            "json": {"department": department, "pid": pid}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 修改節點
    def edit_dept(self, plat_token=None, department_id=None, department=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/account/dept/{format(department_id)}",
            "json": {"department": department},
            "params": {"departmentId": department_id}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 刪除節點
    def delete_dept(self, plat_token=None, department_id=None, ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "delete",
            "url": f"/v1/account/dept/{format(department_id)}",
            "params": {"departmentId": department_id}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 設置負責人
    def dept_leader(self, plat_token=None, admin_id=None, is_leader=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/account/dept/leader",
            "json": {"adminId": admin_id, "isLeader": is_leader}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 關聯已存在帳號
    def dept_admin(self, plat_token=None, admin_id_list=None, department_id=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/account/dept/admin",
            "json": {"adminIdList": admin_id_list, "departmentId": department_id}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 解除關聯
    def delete_dept_admin(self, plat_token=None, admin_id=None, ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": "/v1/account/dept/leader",
            "params": {"adminId": admin_id}
        }

        response = self.send_request(**request_body)
        return response.json()

    def find_dept_id(self, plat_token=None):
        response = self.dept_list(plat_token=plat_token)
        dept_id = jsonpath.jsonpath(response, "$..id")
        return str(dept_id[-1])


class AccountRole(PlatformAPI):
    # 角色列表
    def role_list(self, plat_token=None, role=None, authority_id=None, department_id=None, page=None, size=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": "/v1/account/role/list",
            "params": {
                "role": role,
                "authorityId": authority_id,
                "departmentId": department_id,
                "page": page,
                "size": size
            }
        }

        response = self.send_request(**request_body)
        return response.json()

    # 創建角色
    def add_role(self, plat_token=None, role=None, remark=None, authority_ids=None, department_ids=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "post",
            "url": "/v1/account/role",
            "json": {
                "role": role,
                "remark": remark,
                "authorityIds": authority_ids,
                "departmentIds": department_ids,
            }
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯角色
    def edit_role(
            self,
            plat_token=None,
            role_id=None,
            role=None,
            remark=None,
            authority_ids=None,
            department_ids=None,
    ):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/account/role/{format(role_id)}",
            "json": {
                "role": role,
                "remark": remark,
                "authorityIds": authority_ids,
                "departmentIds": department_ids,
            }
        }

        response = self.send_request(**request_body)
        return response.json()

    # 角色狀態
    def role_status(self, plat_token=None, role_id=None, status=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "put",
            "url": f"/v1/account/role/{format(role_id)}/status",
            "json": {"status": status}
        }

        response = self.send_request(**request_body)
        return response.json()

    # 顯示角色權限
    def role_authorities(self, plat_token=None, role_id=None):
        if plat_token is not None:
            self.request_session.headers.update({"token": str(plat_token)})

        request_body = {
            "method": "get",
            "url": f"/v1/account/role/{format(role_id)}/authorities",
            "params": {"roleId": role_id}
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
