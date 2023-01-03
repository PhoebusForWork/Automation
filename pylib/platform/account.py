# -*- coding: utf-8 -*-
from .platApiBase import PLAT_API  # 執行RF時使用
from utils.api_utils import KeywordArgument
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')  # 在rf_api_test層執行時使用
web_host = config['host']['web_host']
platfrom_host = config['host']['platform_host']


class AccountAdmin(PLAT_API):

    def search_admin_list(self,  # 搜索帳號列表
                          platUid=None, platToken=None,
                          account=None, displayName=None, phone=None,
                          isLeader=None, deptId=None, status=None,
                          deptIdList=None, roleIdList=None, startLoginTime=None,
                          endLoginTime=None, isNonDept=None,
                          page=None, size=None,
                          ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/admin",
                               json={},
                               params={
                                   "account": account,
                                   "displayName": displayName,
                                   "phone": phone,
                                   "isLeader": isLeader,
                                   "deptId": deptId,
                                   "status": status,
                                   "deptIdList": deptIdList,
                                   "roleIdList": roleIdList,
                                   "startLoginTime": startLoginTime,
                                   "endLoginTime": endLoginTime,
                                   "isNonDept": isNonDept,
                                   "page": page,
                                   "size": size,
                               }
                               )
        self._printresponse(response)
        return response.json()

    def add_admin(self,  # 新增帳號
                  platUid=None,
                  platToken=None,
                  account=None,
                  password=None,
                  phone=None,
                  sipNum=None,
                  fixSipNum=None,
                  isLeader=None,
                  deptId=None,
                  roleIds=None,
                  expiredTime=None,
                  displayName=None,
                  ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/account/admin",
                                json={
                                    "phone": phone,
                                    "sipNum": sipNum,
                                    "fixSipNum": fixSipNum,
                                    "isLeader": isLeader,
                                    "deptId": deptId,
                                    "roleIds": roleIds,
                                    "expiredTime": expiredTime,
                                    "account": account,
                                    "password": password,
                                    "displayName": displayName
                                },
                                params={}

                                )
        self._printresponse(response)
        return response.json()

    def admin_info(self,  # 帳號詳情
                   platUid=None,
                   platToken=None,
                   adminId=None,
                   ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/admin/{}".format(adminId),
                               json={},
                               params={
            "adminId": adminId,
        }

        )
        self._printresponse(response)
        return response.json()

    def edit_admin(self,  # 編輯帳號
                   platUid=None,
                   platToken=None,
                   adminId=None,
                   phone=None,
                   sipNum=None,
                   fixSipNum=None,
                   isLeader=None,
                   deptId=None,
                   roleIds=None,
                   expiredTime=None,
                   ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/admin/{}".format(adminId),
                               json={
            "phone": phone,
            "sipNum": sipNum,
            "fixSipNum": fixSipNum,
            "isLeader": isLeader,
            "deptId": deptId,
            "roleIds": roleIds,
            "expiredTime": expiredTime,
        },
            params={
            "adminId": adminId,
        }

        )
        self._printresponse(response)
        return response.json()

    def delete_admin(self,  # 刪除帳號
                     platUid=None,
                     platToken=None,
                     adminId=None,
                     ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.delete(platfrom_host+"/v1/account/admin/{}".format(adminId),
                                  json={},
                                  params={
            "adminId": adminId,
        }
        )
        self._printresponse(response)
        return response.json()

    def admin_status(self,  # 帳號狀態修改
                     platUid=None,
                     platToken=None,
                     adminId=None,
                     status=None,
                     ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/admin/{}/status".format(adminId),
                               json={},
                               params={
            "adminId": adminId,
            "status": status,  # 0停用;1啟用;2刪除
        }
        )
        self._printresponse(response)
        return response.json()

    def edit_password(self,  # 修改密碼
                      platUid=None,
                      platToken=None,
                      oldPassword=None,
                      newPassword=None,
                      ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/admin/password",
                               json={
                                   "oldPassword": oldPassword,
                                   "newPassword": newPassword,
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def reset_password(self,  # 重置密碼
                       platUid=None,
                       platToken=None,
                       adminId=None,
                       ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/admin/{}/resetPassword".format(adminId),
                               json={},
                               params={
            "adminId": adminId,
        }
        )
        self._printresponse(response)
        return response.json()


class AccountAuthority(PLAT_API):

    def authority_list(self,  # 權限總列表
                       platUid=None, platToken=None,
                       ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/authority/list",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def authority_menu(self,  # 選單樹列表
                       platUid=None, platToken=None,
                       ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/authority/menu",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def authority_permission(self,  # 權限列表
                             platUid=None, platToken=None,
                             ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/authority/permission",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()


class AccountDept(PLAT_API):

    def dept_list(self,  # 結點列表
                  platUid=None, platToken=None,
                  roleId=None, departmentStatus=None
                  ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/dept/list",
                               json={},
                               params={
                                   "roleId": roleId,
                                   "departmentStatus": departmentStatus,
                               }
                               )
        self._printresponse(response)
        return response.json()

    def admim_list(self,  # 人員關係列表
                   platUid=None,
                   platToken=None,
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
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/dept/admin/list",
                               json={},
                               params=KeywordArgument.body_data()

                               )
        self._printresponse(response)
        return response.json()

    def add_dept(self,  # 新增節點
                 platUid=None, platToken=None,
                 department=None, pid=None,
                 ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/account/dept",
                                json={
                                    "department": department,
                                    "pid": pid,
                                },
                                params={},
                                )
        self._printresponse(response)
        return response.json()

    def edit_dept(self,  # 修改節點
                  platUid=None, platToken=None,
                  departmentId=None, department=None
                  ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/dept/{}".format(departmentId),
                               json={
            "department": department,
        },
            params={
            "departmentId": departmentId,
        }
        )
        self._printresponse(response)
        return response.json()

    def delete_dept(self,  # 刪除節點
                    platUid=None, platToken=None,
                    departmentId=None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.delete(platfrom_host+"/v1/account/dept/{}".format(departmentId),
                                  json={},
                                  params={
            "departmentId": departmentId,
        }
        )
        self._printresponse(response)
        return response.json()

    def dept_leader(self,  # 設置負責人
                    platUid=None, platToken=None,
                    adminId=None, isLeader=None
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/dept/leader",
                               json={
                                   "adminId": adminId,
                                   "isLeader": isLeader,
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def dept_admin(self,  # 關聯已存在帳號
                   platUid=None, platToken=None,
                   adminIdList=None, departmentId=None
                   ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/dept/admin",
                               json={
                                   "adminIdList": adminIdList,
                                   "departmentId": departmentId,
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def delete_dept_admin(self,  # 解除關聯
                          platUid=None, platToken=None,
                          adminId=None,
                          ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/dept/leader",
                               json={},
                               params={
                                   "adminId": adminId,
                               }
                               )
        self._printresponse(response)
        return response.json()


class AccountRole(PLAT_API):

    def role_list(self,  # 角色列表
                  platUid=None, platToken=None,
                  role=None, authorityId=None,
                  departmentId=None,
                  page=None, size=None,
                  ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/role/list",
                               json={},
                               params={
                                   "role": role,
                                   "authorityId": authorityId,
                                   "departmentId": departmentId,
                                   "page": page,
                                   "size": size,
                               }
                               )
        self._printresponse(response)
        return response.json()

    def add_role(self,  # 創建角色
                 platUid=None, platToken=None,
                 role=None, remark=None,
                 authorityIds=None,
                 departmentIds=None,
                 ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.post(platfrom_host+"/v1/account/role",
                                json={
                                    "role": role,
                                    "remark": remark,
                                    "authorityIds": authorityIds,
                                    "departmentIds": departmentIds,
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def edit_role(self,  # 編輯角色
                  platUid=None, platToken=None,
                  roleId=None,
                  role=None, remark=None,
                  authorityIds=None,
                  departmentIds=None,
                  ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/role/{}".format(roleId),
                               json={
            "role": role,
            "remark": remark,
            "authorityIds": authorityIds,
            "departmentIds": departmentIds,
        },
            params={}
        )
        self._printresponse(response)
        return response.json()

    def role_status(self,  # 角色狀態
                    platUid=None, platToken=None,
                    roleId=None,
                    status=None,
                    ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.put(platfrom_host+"/v1/account/role/{}/status".format(roleId),
                               json={
            "status": status,
        },
            params={}
        )
        self._printresponse(response)
        return response.json()

    def role_authorities(self,  # 顯示角色權限
                         platUid=None, platToken=None,
                         roleId=None,
                         ):
        if platToken != None:
            # self.ps.headers.update({"uid":str(platUid)})
            self.ps.headers.update({"token": str(platToken)})
        response = self.ps.get(platfrom_host+"/v1/account/role/{}/authorities".format(roleId),
                               json={},
                               params={
            "roleId": roleId,
        }
        )
        self._printresponse(response)
        return response.json()
