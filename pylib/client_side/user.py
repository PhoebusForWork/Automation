# -*- coding: utf-8 -*-
import jsonpath
from ..client_side.webApiBase import WebAPI
from utils.api_utils import KeywordArgument
from utils.generate_utils import Make
from utils.data_utils import EnvReader
from utils.xxl_job_utils import XxlJobs
from decimal import Decimal
from bson.decimal128 import Decimal128
from pylib.client_side.wallet import FrontUser
from scripts.automation.mongo import mongo_scripts
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
    def get_coupon_records(self):
        request_body = {
            "method": "get",
            "url": "/v1/user/vip/coupon-records"
        }
        response = self.send_request(**request_body)
        target = response.json()

        return target

    # 用戶VIP未領點卷
    def get_coupons(self, source=None):
        request_body = {
            "method": "get",
            "url": "/v1/user/vip/coupons",
            "params": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        target = response.json()

        if source is not None:
            target = jsonpath.jsonpath(response.json(), "$..data[?(@.source==" + str(source) + ")]")

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
    def get_vip_config(self, vip_name=None, currency=None):
        request_body = {
            "method": "get",
            "url": "/v1/user/vip/config"
        }
        response = self.send_request(**request_body)
        target = response.json()

        if vip_name is not None:
            target = jsonpath.jsonpath(response.json(), "$..data.vipLevels[?(@.name=='" + vip_name + "')]")

        if currency is not None:
            target = jsonpath.jsonpath(response.json(), "$..data.vipPointRatios[?(@.currency=='" + currency + "')]")
            if target:
                target = target[0]

        target = target if target else {}

        return target

    def set_job_date(self, token=None, test=None, type_id=None):

        job_date = Make.generate_custom_date(minutes=15, operation="replace", is_format=False)
        if "過期" in test['scenario']:
            job_date = Make.generate_custom_date(date=job_date, months=-1, is_format=False)

        target_day = 0
        if len(type_id) == 1:  # {0:每月点券(m/1) ,1:新年点券(m/15),2:生日点券(m/10),3:升级点券 (m/5)}
            target_day = [1, 15, 10, 5][type_id[0]]
        if 0 in type_id:  # 每月點卷發放日為1號
            target_day = 1
        if 2 in type_id:  # 設定使用者生日
            user_detail = Detail(token).get_detail()
            if user_detail['data']['birthdayDate'] is None:  # 若無資料才可修改
                birthday_date = Make.generate_custom_date(
                    years=1993, days=target_day, operation='replace', format='%Y-%m-%d')
                Detail(token).edit_detail(birthdayDate=birthday_date)

        if target_day > 0:
            job_date = Make.generate_custom_date(date=job_date, days=target_day, operation="replace", is_format=False)

        return job_date

    def run_vip_xxl_job(self, job_date=None, type_id=3):

        xxl = XxlJobs()
        xxl.sync_vip_festivalGift_date(sync_vip_date=job_date) if 1 in type_id else None  # 設定新年彩金發放日
        xxl.sync_vip(sync_vip_date=job_date)
        time.sleep(2)

    def run_vip_process(self, token=None, test=None, user_name=None ):

        job_date = self.getVIPMapping(token=token, test=test)
        mongo_scripts.setup_mongo(username=user_name, vip_json=test['json'])  # Mongo update
        self.run_vip_xxl_job(job_date=job_date, type_id=test['params']['type'])  # 打XXL-JOB VIP

    def getVIPMapping(self, token=None, test=None):

        # 取得後台設定的金額，設定MONGO的JSON
        vip_config = self.get_vip_config(vip_name=test['params']['getVip'])
        mapping_name = {"vip_info.bet_total": "betTotal", "vip_info.recharge_total": "rechargeTotal",
                        "vip_info.limit_bet_total": "limitBet", "vip_info.limit_recharge_total": "limitRecharge"}
        for test_key, test_value in test['json'].items():
            mapped_key = mapping_name.get(test_key)
            if mapped_key is not None:
                test['json'][test_key] = Decimal128(Decimal(test['params'][mapped_key])
                                                    + Decimal(vip_config[0][mapped_key]))

        test['params']['type'] = [int(value.strip()) for value in str(test['params']['type']).split(',')]
        type_id = test['params']['type']

        # 計算JOB時間與各彩金類型需調整的時間
        job_date = self.set_job_date(token=token, test=test, type_id=type_id)
        test['json']['vip_info.last_modified_time'] = Make.generate_custom_date(date=job_date, days=-3, is_format=False)
        if 2 in type_id:  # 生日點卷需註冊大於3個月
            print("run_vip_process=1.6", job_date)
            test['json']['register_time'] = Make.generate_custom_date(date=job_date, months=-6, is_format=False)
        if "降級" in test['scenario']:  # 降級stat_date需剛好等於30天
            test['json']['vip_info.stat_date'] = Make.generate_custom_date(date=job_date, days=-30, is_format=False)
        job_date = Make.generate_custom_date(date=job_date, minutes=15, format='%Y-%m-%dT%H:%M:%S+08:00')
        return job_date

    def get_coupon_data(self, test=None, type_id=None, org_user_vip=None, user_vip_id=None, user_vip_name=None):

        available_coupons = []  # 获取用户可用的彩金清单
        user_coupons = []  # 获取用户彩金清单

        if user_vip_name and user_vip_id and user_vip_name != "VIP0" and user_vip_name.startswith("VIP"):
            # 获取用户彩金清单
            user_coupons = self.get_coupons()['data']
            vip_config = self.get_vip_config()
            # 遍历用户VIP等级及以下的VIP等级
            if not any(scenario in test['scenario'] for scenario in ["降級", "降後升級", "過期"]):
                for vip_level in vip_config["data"]["vipLevels"]:
                    for type_value in type_id:
                        coupons_name = ['redEnvelop', 'festivalGift', 'birthdayGift', 'levelGift'][type_value]
                        if type_value == 3:  # 升級可升多等VIP3->VIP5
                            if org_user_vip < vip_level["id"] <= user_vip_id and vip_level[coupons_name] > 0:
                                available_coupons.append({"name": vip_level["name"], "point": vip_level[coupons_name]})
                        else:  # 其它點卷依當時的VIP等級派發
                            if vip_level["id"] == user_vip_id and vip_level[coupons_name] > 0:
                                available_coupons.append({"name": vip_level["name"], "point": vip_level[coupons_name]})

        return user_coupons, available_coupons

    def get_coupon_exchange_bonus(self, token=None, test=None, available_coupons=None):

        user_balances = FrontUser(token).get_balance()
        be_user_currency = ""
        be_user_balance = 0.0
        for account in user_balances["data"]:
            if account["isPreferCurrency"]:
                be_user_currency = account["currency"]
                be_user_balance = float(account["balance"])  # 将余额转换为浮点数

        user_currency = "CNY"
        if test['params'].get('currency') is not None:
            user_currency = test['params']['currency']

        if be_user_currency != user_currency:
            FrontUser(token).edit_user_currency(currency=user_currency)
            user_balances = FrontUser(token).get_balance()
            for account in user_balances["data"]:
                if account["isPreferCurrency"]:
                    be_user_balance = float(account["balance"])  # 将余额转换为浮点数

        # be_user_balance + (推算的彩金)/轉換比率
        estimate_balance = be_user_balance
        if available_coupons is not None:
            # 換算幣別與轉換比率
            vip_config = self.get_vip_config(currency=user_currency)
            exchange_ratio = vip_config['showPoint'] / vip_config['showAmount']
            total_points = sum(coupon["point"] for coupon in available_coupons)
            estimate_balance += total_points / exchange_ratio
            estimate_balance = round(estimate_balance, 4)

        # 兌換彩金
        self.edit_coupon_exchange(currency=user_currency)

        user_balances = FrontUser(token).get_balance()
        actual_balance = next(
            (float(account["balance"]) for account in user_balances["data"] if account["isPreferCurrency"]), None)
        actual_balance = round(actual_balance, 4)

        return actual_balance, estimate_balance


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
    def edit_detail(self, avatar=None, nickname=None, birthday=None, sex=None, birthdayDate=None):
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
