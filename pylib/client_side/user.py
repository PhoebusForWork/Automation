# -*- coding: utf-8 -*-
import jsonpath
from ..client_side.webApiBase import WebAPI
from utils.api_utils import KeywordArgument
from utils.generate_utils import Make
from utils.data_utils import EnvReader
from utils.database_utils import Mongo
from utils.xxl_job_utils import XxlJobs
from decimal import Decimal
from bson.decimal128 import Decimal128
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json
import time

env = EnvReader()
web_host = env.WEB_HOST


# 交易通知信
class TransactionNotice(WebAPI):
    # 已讀通知信
    def read_notice(self, id=None):
        request_body = {
            "method": "put",
            "url": f"/v1/transaction/notice/read/{id}"
        }
        response = self.send_request(**request_body)
        return response.json()

    # 一鍵已讀
    def read_all_notice(self):
        request_body = {
            "method": "post",
            "url": "/v1/transaction/notice/read/all"
        }
        response = self.send_request(**request_body)
        return response.json()

    # 未讀數量
    def get_unread_count(self):
        request_body = {
            "method": "get",
            "url": "/v1/transaction/notice/unread/count"
        }
        response = self.send_request(**request_body)
        return response.json()

    # 通知信列表
    def get_notice_list(self, page=None, size=None):
        request_body = {
            "method": "get",
            "url": "/v1/transaction/notice/list",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()


# 站內信
class InternalLetter(WebAPI):
    # 未讀數量
    def get_unread_count(self, now=Make.date('end')):
        request_body = {
            "method": "get",
            "url": "/v1/user/internal/letter/unread/count",
            "params": KeywordArgument.body_data(),
        }
        response = self.send_request(**request_body)
        return response.json()

    # 一鍵已讀
    def read_all_letter(self, now=Make.date('end')):
        request_body = {
            "method": "post",
            "url": "/v1/user/internal/letter/read/all",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 新站內信
    def new_letter(self, page=None, size=None,
                   typeId=None, title=None, message=None,
                   now=None, img1=None, img2=None, img3=None):
        request_body = {
            "method": "post",
            "url": "/v1/user/internal/letter",
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 站內信回覆
    def reply_letter(self, id=None, type=None, message=None,
                     img1=None, img2=None, img3=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/internal/letter/message/reply",
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 問題類型
    def get_quiz_types(self):
        request_body = {
            "method": "get",
            "url": "/v1/user/internal/letter/quiz/types"
        }
        response = self.send_request(**request_body)
        return response.json()

    # 站內信對話
    def get_massage(self, id=None, type=None,
                    now=None, page=None, size=None):
        request_body = {
            "method": "get",
            "url": "/v1/user/internal/letter/message",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 站內信列表
    def get_letter_list(self, type=None, now=None,
                        page=None, size=None):
        request_body = {
            "method": "get",
            "url": "/v1/user/internal/letter/list",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()


# 用戶幣種
class Currency(WebAPI):
    # 選擇幣別
    def select_currency(self, currency=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/currency",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()


# VIP資訊
class Vip(WebAPI):
    # 用戶VIP點卷可兌換詳情
    def get_coupon_exchange(self, currency=None):
        request_body = {
            "method": "get",
            "url": "/v1/user/vip/coupon-exchange"
        }
        response = self.send_request(**request_body)
        return response.json()

    # 用戶兌換VIP點卷
    def edit_coupon_exchange(self, currency=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/vip/coupon-exchange",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 用戶VIP點卷詳情
    def get_coupon_records(self, type=None):
        request_body = {
            "method": "get",
            "url": "/v1/user/vip/coupon-records"
        }
        response = self.send_request(**request_body)
        target = response.json()
        if type is not None:
            target = jsonpath.jsonpath(response.json(), "$..data[?(@.type==" + str(type) + ")]")

        target = target if target else {}

        return target

    #用戶VIP未領點卷
    def get_coupons(self, source=None):
        request_body = {
            "method": "get",
            "url": "/v1/user/vip/coupons",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        target = response.json()
        if source is not None:
            target = jsonpath.jsonpath(response.json(), "$..data[?(@.source=='" + source + "')]")

        target = target if target else {}

        return target

    # 用戶VIP
    def get_vip(self):
        request_body = {
            "method": "get",
            "url": "/v1/user/vip"
        }
        response = self.send_request(**request_body)
        return response.json()

    # 各VIP階層與幣別積分比例
    def get_vip_config(self, vipName = None):
        request_body = {
            "method": "get",
            "url": "/v1/user/vip/config"
        }
        response = self.send_request(**request_body)
        target=response.json()

        if vipName is not None:
            target = jsonpath.jsonpath(response.json(), "$..data.vipLevels[?(@.name=='" + vipName + "')]")

        target = target if target else {}

        return target


    def setup_mongo_user_vip(self,username=None, vipjosn = None):
        setup = Mongo(platform='plt')
        setup.specify_db('plt_user')
        setup.specify_collection('ldpro_user')

        filter_query = {"username": username}
        update_query = {"$set": vipjosn}
        setup.update_one(filter_query, update_query)

    def getVIPMapping(self, test):
        # 取得VIP CONFIG 設定檔，並獎vipConfig 中的参数名轉为小写
        vipConfig = self.get_vip_config(test['params']['getVip'])
        vipConfig_lower = {k.lower().replace("_", ""): v for item in vipConfig for k, v in item.items()}

        for test_key, test_value in test['json'].items():
            keyname = test_key.replace("vip_info.", "").lower()
            mapingkeyname = keyname.replace("_", "").lower()
            if mapingkeyname in vipConfig_lower:
                vip_value = Decimal(vipConfig_lower[mapingkeyname])
                if keyname in test['params']:
                    vip_value += Decimal(test['params'][keyname])
                vip_value = vip_value.quantize(Decimal('0.00000000'))
                test['json'][test_key] = Decimal128(vip_value)


        # 获取当前日期和时间
        type = test['params']['type']
        current_date = datetime.now()
        target_day = [1, 15, 10, 5][type]  # {0:每月点券(m/1) ,1:新年点券(m/15),2:生日点券(m/10),3:升级点券 (m/5)}
        current_date = current_date.replace(day=target_day, hour=0, minute=15, second=0, microsecond=0)
        test['json']['vip_info.last_modified_time'] = current_date - timedelta(days=3)  # 减去 3 天
        if type == 2 :
            test['json']['register_time'] = current_date - relativedelta(months=4)
            print("test['json']['register_time']=",test['json']['register_time'])

        print("current_date=",current_date,"test['json']=",test['json'])
        return test

    def run_Vip_XXL_JOB(self,type=3):

        xxl = XxlJobs()
        # 将时间固定为 00:15:00
        current_date = datetime.now()
        target_day = [1, 15, 10, 5][type]  # {0:每月点券(m/1) ,1:新年点券(m/15),2:生日点券(m/10),3:升级点券 (m/5)}
        current_date = current_date.replace(day=target_day, hour=0, minute=15, second=0, microsecond=0)

        # 格式化日期并手动添加时区信息
        formatted_date = current_date.strftime('%Y-%m-%dT%H:%M:%S+08:00')
        xxl.sync_vip_festivalGift_date(syncVipDate=current_date) if type == 1 else None
        xxl.sync_vip(syncVipDate=formatted_date)
        print("formatted_date=",formatted_date)
        time.sleep(2)

    def get_coupon(self,type=None, user_vip_id=None, user_vip_name=None):

        available_coupons = []  # 获取用户可用的彩金清单
        user_coupons = []  # 获取用户彩金清单
        print("user_vip_id=",user_vip_id,"user_vip_name=",user_vip_name)
        if user_vip_name is not None and user_vip_id is not None and user_vip_name != "VIP0" and user_vip_name.startswith("VIP"):
            # 获取用户彩金清单
            user_coupons =  self.get_coupon_records(type=type)
            vipConfig = self.get_vip_config()
            #print("user_coupons=",user_coupons,"vipConfig==",vipConfig)
            # 遍历用户VIP等级及以下的VIP等级
            for vip_level in vipConfig["data"]["vipLevels"]:
                couponsName = ['redEnvelop', 'festivalGift', 'birthdayGift','levelGift',][type]
                if(type==3):
                    if vip_level["id"] <= user_vip_id and vip_level[couponsName] > 0:
                        available_coupons.append({"name": vip_level["name"], "point": vip_level[couponsName]})
                else:
                    if vip_level["id"] == user_vip_id and vip_level[couponsName] > 0:
                        available_coupons.append({"name": vip_level["name"], "point": vip_level[couponsName]})

        print("user_coupons ==========",user_coupons,"available_coupons=", available_coupons)
        return user_coupons, available_coupons


# 客戶詳細資料
class Detail(WebAPI):
    # 獲取用戶明細資料
    def get_detail(self):
        request_body = {
            "method": "get",
            "url": "/v1/user/detail"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 編輯用戶明細資料
    def edit_detail(self, avatar=None, nickname=None, birthday=None, sex=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/detail",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()


# 用戶安全中心
class Security(WebAPI):
    # 提款短信驗證開關
    def get_withdraw_protect(self, status=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/security/withdrawProtect",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 解綁交易所地址
    def unbind_exchange(self, addressId=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/security/unBind/exchange",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 解綁虛擬幣地址
    def unbind_address(self, addressId=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/security/unBind/address",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 修改密碼
    def edit_pwd(self, newPwd=None, oldPwd=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/security/pwd",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 是否綁定手機號碼
    def check_mobile(self):
        request_body = {
            "method": "get",
            "url": "/v1/user/security/mobile"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 更換手機號
    def edit_mobile(self, newMobileCountryCode=None, newMobile=None,
                    nmCode=None, omCode=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/security/mobile",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 綁定手機號碼
    def mobile_binding(self, countryCode=None, mobile=None,
                       code=None,  web_token=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})
        request_body = {
            "method": "put",
            "url": "/v1/user/security/mobile/binding",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 預設銀行卡設置
    def bank_card_default(self, cardId=None, cardType=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/security/bankCard/default",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 預設虛擬幣設置
    def address_default(self, addressId=None, type=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/security/address/default",
            "params": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 綁定交易所地址
    def bind_exchange(self, userId=None, userName=None,
                      withdrawAddress=None, protocol=None,
                      remark=None, isDefault=None, code=None):
        request_body = {
            "method": "post",
            "url": "/v1/user/security/bind/exchange",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 綁定銀行卡
    def bind_bank_card(self, userId=None, userName=None,
                       realName=None, bankId=None,
                       bankName=None, bankAddress=None, cardNo=None,
                       cardOwnerName=None, cardType=None,
                       default=None, first=None):
        request_body = {
            "method": "post",
            "url": "/v1/user/security/bind/bankCard",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 綁定虛擬幣地址
    def bind_address(self, userId=None, userName=None,
                     withdrawAddress=None, protocol=None,
                     remark=None, isDefault=None, code=None):
        request_body = {
            "method": "post",
            "url": "/v1/user/security/bind/address",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 取得用戶安全中心資訊
    def get_security_info(self):
        request_body = {
            "method": "get",
            "url": "/v1/user/security/info"
        }

        response = self.send_request(**request_body)
        return response.json()

    # # 綁定郵箱地址
    # def bind_email(self, email=None, code=None):
    #     request_body = {
    #         "method": "put",
    #         "url": "/v1/user/security/email/binding",
    #         "json": KeywordArgument.body_data()
    #     }

    #     response = self.send_request(**request_body)
    #     return response.json()

    # # 解綁郵箱地址
    # def unbind_email(self, code=None):
    #     request_body = {
    #         "method": "put",
    #         "url": "/v1/user/security/email/unbind",
    #         "json": KeywordArgument.body_data()
    #     }

    #     response = self.send_request(**request_body)
    #     return response.json()


# 用戶送貨地址
class Address(WebAPI):
    # 依使用者查詢地址
    def get_user_address(self):
        request_body = {
            "method": "get",
            "url": "/v1/user/address"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 查詢單筆地址
    def get_user_address_one(self, id=1):
        request_body = {
            "method": "get",
            "url": f"/v1/user/address/{id}"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 新增地址
    def add_user_address(
            self, recipient=None, telephone=None, cityId=None, district=None, street=None, detailAddress=None
    ):
        request_body = {
            "method": "post",
            "url": "/v1/user/address",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 更新地址
    def edit_user_address(
            self, recipient=None, telephone=None, cityId=None, district=None, street=None, detailAddress=None, id=None
    ):
        request_body = {
            "method": "put",
            "url": "/v1/user/address",
            "json": KeywordArgument.body_data()
        }

        response = self.send_request(**request_body)
        return response.json()

    # 刪除用戶地址
    def delete_user_address(self, id=1):
        request_body = {
            "method": "delete",
            "url": f"/v1/user/address/{id}"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 省列表
    def get_provinces(self):
        request_body = {
            "method": "get",
            "url": "/v1/user/address/provinces"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 省下城市列表
    def get_city(self, provinceId=None):
        request_body = {
            "method": "get",
            "url": f"/v1/user/address/province/{provinceId}/city"
        }

        response = self.send_request(**request_body)
        return response.json()

    # 移除非默認地址
    def clear_user_address(self, web_token=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})
        resp = self.get_user_address()
        ret = jsonpath.jsonpath(resp, "$.data[?(@.isDefault != 1)].id")
        if ret is not False:
            for i in ret:
                self.delete_user_address(id=i)

    # 獲取可刪除地址
    def get_user_address_not_default(self, web_token=None):
        if web_token is not None:
            self.request_session.headers.update({"token": str(web_token)})
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


# 用戶語系
class Language(WebAPI):
    # 選擇語系
    def select_language(self, language=None):
        request_body = {
            "method": "put",
            "url": "/v1/user/language",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()


# 用戶操作
class User(WebAPI):
    # 用戶心跳
    def hearrbeat(self):
        request_body = {
            "method": "post",
            "url": "/v1/user/heartbeat"
        }
        response = self.send_request(**request_body)
        return response.json()
