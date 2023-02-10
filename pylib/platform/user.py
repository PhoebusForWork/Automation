# -*- coding: utf-8 -*-
from ..platform.platApiBase import PLAT_API
from utils.data_utils import EnvReader
import jsonpath

env = EnvReader()
platform_host = env.PLATFORM_HOST


class User(PLAT_API):

    def get_user_list(self,  # 查詢客戶列表
                      plat_token=None,
                      From=None, to=None,
                      minBalance=None, maxBalance=None,
                      status=None, vipId=None, groupId=None,
                      isRegisterTime=None, searchType=None,
                      keyword=None, page=None, size=None,
                      isOnline=None, isWhiteList=None,
                      ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user",
                               json={},
                               params={
                                   "from": From, "to": to,
                                   "minBalance": minBalance, "maxBalance": maxBalance,
                                   "status": status, "vipId": vipId, "groupId": groupId,
                                   "isRegisterTime": isRegisterTime, "searchType": searchType,
                                   "keyword": keyword, "page": page, "size": size,
                                   "isOnline": isOnline, "isWhiteList": isWhiteList,
                               }
                               )
        self._printresponse(response)
        return response.json()

    def user_params(self,  # 客戶列表查詢條件
                    plat_token=None,
                    ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user/params",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def get_user_info(self,  # 查詢客戶資訊
                      plat_token=None,
                      userId=None
                      ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user/{}".format(userId),
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def get_user_amount(self,  # 查詢客戶財務資訊
                        plat_token=None,
                        userId=None
                        ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user/{}/account".format(userId),
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def user_remark(self,  # 更新客戶備註(不需審核)
                    plat_token=None,
                    userId=None, remark=None,
                    ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platform_host+"/v1/user/{}/remark".format(userId),
                               json={
            "remark": remark,
        },
            params={}
        )
        self._printresponse(response)
        return response.json()

    def user_really_name(self,  # 更新客戶真實姓名(不需審核)
                         plat_token=None,
                         userId=None, reallyName=None,
                         ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platform_host+"/v1/user/{}/reallyName".format(userId),
                               json={
            "reallyName": reallyName,
        },
            params={}
        )
        self._printresponse(response)
        return response.json()

    def set_white_list(self,  # 設置客戶撞庫白名單
                       plat_token=None,
                       userId=None, isWhiteList=None,
                       ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platform_host+"/v1/user/{}/isWhiteList".format(userId),
                               json={},
                               params={
            "isWhiteList": isWhiteList,
        }
        )
        self._printresponse(response)
        return response.json()

    def user_convert_proxy(self,  # 開通代理角色
                           plat_token=None,
                           userId=None,
                           ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platform_host+"/v1/user/convertProxy",
                               json={
                                   "userId": userId,
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def username_validate(self,  # 校驗會員帳號是否存在
                          plat_token=None,
                          usernames=None,
                          ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.post(platform_host+"/v1/user/username/validate",
                                json={
                                    "usernames": usernames
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def user_lock_status(self,  # 申請鎖定 lockStatus(鎖定類別) LOGIN：登入, RECHARGE：充值, WITHDRAW：提領, TRANSFER：轉帳
                         plat_token=None,
                         userIds=None, lockStatus=None, isLock=None,
                         remark=None,
                         ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.post(platform_host+"/v1/user/lockStatus",
                                json={
                                    "userIds": userIds,
                                    "userLockTypeList": [
                                        {
                                            "lockStatus": lockStatus,
                                            "isLock": isLock,
                                        }
                                    ],
                                    "remark": remark,
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def edit_user_vip(self,  # 修改客戶VIP層級
                      plat_token=None,
                      userId=None, vipId=None,
                      ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platform_host+"/v1/userVip/{}".format(userId),
                               json={},
                               params={
            "userId": userId,
            "vipId": vipId,
        }
        )
        self._printresponse(response)
        return response.json()

    def get_user_vip_info(self,  # 查詢客戶VIP層級
                          plat_token=None,
                          userName=None,
                          ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/userVip",
                               json={},
                               params={
                                   "userName": userName,
                               }
                               )
        self._printresponse(response)
        return response.json()


# --------------------------------------------------------------------------------------------


    def risk_analysis_same_ip(self,  # 風險套利重複ip
                              plat_token=None,
                              userId=None, page=None, size=None,
                              ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user/{}/risk/analysis/same/ip".format(userId),
                               json={},
                               params={
            "page": page,
            "size": size,
        }
        )
        self._printresponse(response)
        return response.json()

    def risk_analysis_arbitrage(self,  # 風險套利分析查詢
                                plat_token=None,
                                id=None, From=None, to=None,
                                username=None, userType=None, reallyName=None,
                                page=None, size=None,
                                ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user/{}/risk/analysis/arbitrage".format(id),
                               json={},
                               params={
            "from": From, "to": to,
            "username": username, "userType": userType, "reallyName": reallyName,
            "page": page,
            "size": size,
        }
        )
        self._printresponse(response)
        return response.json()

    def login_info(self,  # 登入日誌
                   plat_token=None,
                   id=None,
                   From='2022-01-01T00:00:00Z',
                   to='2022-12-31T23:59:59Z',
                   type=None, keyword=None, osType=None,
                   page=None, size=None,
                   ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user/{}/login/info".format(id),
                               json={},
                               params={
            "from": From, "to": to,
            "type": type, "keyword": keyword, "osType": osType,
            "page": page, "size": size,
        }
        )
        self._printresponse(response)
        return response.json()

    def login_stat(self,  # 客戶登入統計
                   plat_token=None,
                   userId=None,
                   ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user/login/stat/{}".format(userId),
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def get_client_user(self, plat_token=None):
        target = self.get_user_list(plat_token=plat_token, From='2022-01-01T00:00:00Z', status=0,
                                    to='2023-01-15T00:00:00Z', page=None, size=1000)
        client_user = jsonpath.jsonpath(
            target, "$..records[?(@.userType==0).userId]")
        return client_user[0]


class UserManage(PLAT_API):

    def get_user_manage_list(self,  # 查詢審批列表
                             plat_token=None,
                             approveTimeType=0,
                             From="2023-01-01T00:00:00Z", to="2023-12-31T23:59:59Z",
                             username=None, userType=None,
                             optType=None, creator=None,
                             firstApprover=None, secondApprover=None,
                             status=None, page=None, size=None,
                             ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user/manage",
                               json={},
                               params={
                                   "from": From, "to": to,
                                   "status": status, "page": page, "size": size,
                                   "approveTimeType": approveTimeType, "username": username,
                                   "userType": userType, "optType": optType, "creator": creator,
                                   "firstApprover": firstApprover, "secondApprover": secondApprover,
                               }
                               )
        self._printresponse(response)
        return response.json()

    def get_user_manage_query_params(self,  # 查詢審批參數
                                     plat_token=None,
                                     ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user/manage/query/params",
                               json={},
                               params={},
                               )
        self._printresponse(response)
        return response.json()

    def get_user_manage_log(self,  # 後台操作記錄
                            plat_token=None,
                            userId=None, From=None, to=None,
                            optType=None, creator=None,
                            page=None, size=None,
                            ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user/manage/log/{}".format(userId),
                               json={},
                               params={
            "from": From, "to": to,
            "optType": optType, "creator": creator,
            "page": page, "size": size,
        },
        )
        self._printresponse(response)
        return response.json()

    def first_approval(self,  # 一審 審核狀態 1:核准 / 2:駁回
                       plat_token=None,
                       id=None, status=None, remark=None,
                       ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platform_host+"/v1/user/manage/{}/first/approval".format(id),
                               json={
            "status": status,
            "remark": remark,
        },
            params={},
        )
        self._printresponse(response)
        return response.json()

    def second_approval(self,  # 二審 第二審批狀態 4:核准 / 5:駁回
                        plat_token=None,
                        id=None, status=None, remark=None,
                        ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platform_host+"/v1/user/manage/{}/second/approval".format(id),
                               json={
            "status": status,
            "remark": remark,
        },
            params={},
        )
        self._printresponse(response)
        return response.json()

    def user_manage_parent(self,  # 修改上級代理
                           plat_token=None,
                           userId=None, parentUsername=None,
                           ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platform_host+"/v1/user/manage/parent",
                               json={
                                   "userId": userId,
                                   "parentUsername": parentUsername,
                               },
                               params={},
                               )
        self._printresponse(response)
        return response.json()

    def user_manage_contact(self,  # 編輯會員聯絡資料
                            plat_token=None,
                            userId=None, telephone=None,
                            email=None, birthday=None,
                            remark=None,
                            ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platform_host+"/v1/user/manage/parent",
                               json={
                                   "userId": userId,
                                   "telephone": telephone,
                                   "email": email,
                                   "birthday": birthday,
                                   "remark": remark,
                               },
                               params={},
                               )
        self._printresponse(response)
        return response.json()

    def clean_approval(self,  #
                       plat_token=None, optType=None
                       ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        jsdata = self.get_user_manage_list(optType=optType, size=100, status=0)
        ret = jsonpath.jsonpath(jsdata, "$..id")
        jsdata2 = self.get_user_manage_list(
            optType=optType, size=100, status=3)
        ret2 = jsonpath.jsonpath(jsdata2, "$..id")
        if ret:
            for i in ret:
                self.first_approval(id=i, status=2, remark="auto_rej")
        if ret2:
            for i in ret2:
                self.second_approval(id=i, status=5, remark="auto_rej")

    def get_manage_id(self,  #
                      plat_token=None,
                      phase=1  # 一審訂單:1 二審訂單:2
                      ):
        FIRST = 0
        SECOND = 3
        phase = FIRST if phase == 1 else SECOND
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        jsdata = self.get_user_manage_list(
            plat_token=plat_token, status=phase)
        ret = jsonpath.jsonpath(jsdata, "$..id")
        print(phase)
        if ret is False:
            self.user_manage_parent(userId=12, parentUsername='proxy001')
            jsdata = self.get_user_manage_list(
                plat_token=plat_token, status=FIRST)
            ret = jsonpath.jsonpath(jsdata, "$..id")
            if phase == SECOND:
                self.first_approval(id=ret[0], status=1)
        print(ret)
        return ret[0]


class UserVip(PLAT_API):

    def add_vip(self,  # 新增VIP層級
                plat_token=None,
                name=None, regStartTime=None,
                regEndTime=None, rechargeTotal=None,
                betTotal=None, levelGift=None,
                birthdayGift=None, festivalGift=None,
                redEnvelop=None, limitBet=None,
                limitRecharge=None, isVip=None,
                remark=None,
                ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.post(platform_host+"/v1/user/vip/config",
                                json={
                                    "name": name,
                                    "regStartTime": regStartTime,
                                    "regEndTime": regEndTime,
                                    "rechargeTotal": rechargeTotal,
                                    "betTotal": betTotal,
                                    "levelGift": levelGift,
                                    "birthdayGift": birthdayGift,
                                    "festivalGift": festivalGift,
                                    "redEnvelop": redEnvelop,
                                    "limitBet": limitBet,
                                    "limitRecharge": limitRecharge,
                                    "isVip": isVip,
                                    "remark": remark,
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def edit_vip(self,  # 編輯VIP層級
                 plat_token=None,
                 vipId=None,
                 name=None, regStartTime=None,
                 regEndTime=None, rechargeTotal=None,
                 betTotal=None, levelGift=None,
                 birthdayGift=None, festivalGift=None,
                 redEnvelop=None, limitBet=None,
                 limitRecharge=None, isVip=None,
                 remark=None,
                 ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platform_host+"/v1/user/vip/config/{}".format(vipId),
                               json={
            "name": name,
            "regStartTime": regStartTime,
            "regEndTime": regEndTime,
            "rechargeTotal": rechargeTotal,
            "betTotal": betTotal,
            "levelGift": levelGift,
            "birthdayGift": birthdayGift,
            "festivalGift": festivalGift,
            "redEnvelop": redEnvelop,
            "limitBet": limitBet,
            "limitRecharge": limitRecharge,
            "isVip": isVip,
            "remark": remark,
        },
            params={
            "vipId": vipId,
        }
        )
        self._printresponse(response)
        return response.json()

    def edit_vip_only(self,  # 編輯VIP專享
                      plat_token=None,
                      vipId=None,
                      isVip=None,
                      ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.put(platform_host+"/v1/user/vip/config/{}/isVip".format(vipId),
                               json={},
                               params={
            "vipId": vipId,
            "isVip": isVip,
        }
        )
        self._printresponse(response)
        return response.json()

    def get_vip_info(self,  # 獲取VIP配置
                     plat_token=None,
                     ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user/vip/config",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def get_vip_list(self,  # 獲取VIP列表
                     plat_token=None,
                     ):
        if plat_token is not None:
            self.ps.headers.update({"token": str(plat_token)})
        response = self.ps.get(platform_host+"/v1/user/vip/config/mapList",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def get_vip_id_exist(self,  # 獲取存在vip_id
                         plat_token=None,
                         ):
        response = self.get_vip_list(plat_token=plat_token)
        target = jsonpath.jsonpath(response, '$..data[*].id')
        return target[-1]
