# -*- coding: utf-8 -*-
import configparser
import jsonpath
from ..client_side.webApiBase import WEB_API  # 執行RF時使用
from utils.generate_utils import Make


config = configparser.ConfigParser()
config.read('config/config.ini')
web_host = config['host']['web_host']
platfrom_host = config['host']['platform_host']


class Detail(WEB_API):  # 客戶詳細資料

    def getDetail(self):  # 獲取用戶明細資料
        response = self.ws.get(web_host+"/v1/user/detail",
                               data={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def editDetail(self, avatar=None, nickname=None, birthday=None, sex=None):  # 編輯用戶明細資料
        response = self.ws.put(web_host+"/v1/user/detail",
                               json={
                                        "avatar": avatar,
                                        "nickname": nickname,
                                        "birthday": birthday,
                                        "sex": sex
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()


class Security(WEB_API):  # 用戶安全中心

    def getSecurityInfo(self):  # 取得用戶安全中心資訊\
        response = self.ws.get(web_host+"/v1/user/security/info",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def emailBind(self, email=None, code=None):  # 綁定郵箱地址\
        response = self.ws.put(web_host+"/v1/user/security/email/binding",
                               json={
                                        "email": email,
                                        "code": code
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def emailUnbind(self, code=None):  # 解綁郵箱地址\
        response = self.ws.put(web_host+"/v1/user/security/email/unbind",
                               json={
                                        "code": code
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def editMobile(self, newMobile=None, nmCode=None, omCode=None):  # 更換手機號\
        response = self.ws.put(web_host+"/v1/user/security/mobile",
                               json={
                                        "newMobile": newMobile,
                                        "nmCode": nmCode,
                                        "omCode": omCode
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def editPwd(self, newPwd=None, oldPwd=None):  # 修改密碼
        response = self.ws.put(web_host+"/v1/user/security/pwd",
                               json={
                                        "newPwd": newPwd,
                                        "oldPwd": oldPwd,
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()


class Trade(WEB_API):  # 用戶-安全中心

    def balanceHistory(self,  # 查詢資金明細
                       webUid=None,
                       web_token=None,
                       orderType="",
                       startTime="",
                       endTime="",
                       status="-1",
                       page="",
                       size="",
                       ):
        if webUid != None:
            self.ws.headers.update({"uid": str(webUid)})
            self.ws.headers.update({"token": str(web_token)})
        response = self.ws.post(web_host+"/api/gl/balance/history/v2",
                                data={
                                    "orderType": orderType,
                                    "startTime": startTime,
                                    "endTime": endTime,
                                    "status": status,
                                    "page": page,
                                    "size": size,
                                }
                                )
        self._printresponse(response)
        return response.json()

    def historySportList(self,  # 獲取用戶體育注單列表
                         webUid=None,
                         web_token=None,
                         endTime="2022-04-01 23:59:59",
                         startTime="2022-04-01 23:59:59",
                         channelId=None,
                         gameId=None,
                         page=None,
                         size=None,
                         status=None,
                         ):
        if webUid != None:
            self.ws.headers.update({"uid": str(webUid)})
            self.ws.headers.update({"token": str(web_token)})
        response = self.ws.post(web_host+"/api/game/v2/history/sportList",
                                data={
                                    "channelId": channelId,
                                    "gameId": gameId,
                                    "startTime": startTime,
                                    "endTime": endTime,
                                    "status": status,
                                    "page": page,
                                    "size": size,
                                }
                                )
        self._printresponse(response)
        return response.json()


class Address(WEB_API):  # 用戶送貨地址

    def get_user_address(self):  # 依使用者查詢地址
        response = self.ws.get(web_host+"/v1/user/address",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def get_user_address_one(self, id=1):  # 查詢單筆地址
        response = self.ws.get(web_host+"/v1/user/address/{}".format(id),
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def add_user_address(self, recipient=None, telephone=None, cityId=None, district=None, street=None, detailAddress=None):  # 新增地址
        response = self.ws.post(web_host+"/v1/user/address",
                                json={
                                    "recipient": recipient,
                                    "telephone": telephone,
                                    "cityId": cityId,
                                    "district": district,
                                    "street": street,
                                    "detailAddress": detailAddress
                                },
                                params={}
                                )
        self._printresponse(response)
        return response.json()

    def edit_user_address(self, recipient=None, telephone=None, cityId=None, district=None, street=None, detailAddress=None, id=None):  # 更新地址
        response = self.ws.put(web_host+"/v1/user/address",
                               json={
                                   "recipient": recipient,
                                   "telephone": telephone,
                                   "cityId": cityId,
                                   "district": district,
                                   "street": street,
                                   "detailAddress": detailAddress,
                                   "id": id
                               },
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def delete_user_address(self, id=1):  # 刪除用戶地址
        response = self.ws.delete(web_host+"/v1/user/address/{}".format(id),
                                  json={},
                                  params={}
                                  )
        self._printresponse(response)
        return response.json()

    def get_provinces(self):  # 省列表
        response = self.ws.get(web_host+"/v1/user/address/provinces",
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def get_city(self, provinceId=None):  # 省下城市列表
        response = self.ws.get(web_host+"/v1/user/address/province/{}/city".format(provinceId),
                               json={},
                               params={}
                               )
        self._printresponse(response)
        return response.json()

    def clear_user_address(self, web_token=None):  # 移除非默認地址
        if web_token is not None:
            self.ws.headers.update({"token": str(web_token)})
        resp = self.get_user_address()
        ret = jsonpath.jsonpath(resp, "$.data[?(@.isDefault != 1)].id")
        if ret is not False:
            for i in ret:
                self.delete_user_address(id=i)

    def get_user_address_not_default(self, web_token=None):  # 獲取可刪除地址
        if web_token is not None:
            self.ws.headers.update({"token": str(web_token)})
        resp = self.get_user_address()
        ret = jsonpath.jsonpath(resp, "$.data[?(@.isDefault != 1)].id")
        if ret is not False:
            return ret[0]
        else:
            self.add_user_address(
                recipient="AutoTest", telephone=Make.mobile(), cityId=1, detailAddress="詳細地址")
            resp = self.get_user_address()
            ret = jsonpath.jsonpath(resp, "$.data[?(@.isDefault != 1)].id")
            return ret[0]
