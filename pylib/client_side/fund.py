# -*- coding: utf-8 -*-
import jsonpath
from ..client_side.webApiBase import WebAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader
from utils.generate_utils import Make

env = EnvReader()
web_host = env.WEB_HOST


# 充值操作
class Recharge(WebAPI):
    # 充值提交
    def submit(self, os_type=None,
               paymentId=None, merchantId=None,
               rechargeTypeId=None,
               amount=None,
               bankCode=None):
        request_body = {
            "method": "post",
            "url": "/v1/fund/recharge/submit",
            "params": {"os-type": os_type},
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 據用戶群組跟充值分類，獲取充值方式(點選金額後，篩選商戶)
    def get_payment_list(self, os_type=None,
                         amount=None,
                         paymentId=None, rechargeTypeId=None):
        request_body = {
            "method": "post",
            "url": "/v1/fund/recharge/getPaymentList",
            "params": {"os-type": os_type},
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 取得使用者充值訂單資訊
    def get_recharge_order_info(self, orderId):
        request_body = {
            "method": "get",
            "url": f"/v1/fund/recharge/{orderId}",
        }
        response = self.send_request(**request_body)
        return response.json()

    # 获取充值类型列表
    def get_recharge_type_list(self, os_type=None):
        request_body = {
            "method": "get",
            "url": "/v1/fund/getRechargeType",
            "params": {"os-type": os_type},
        }
        response = self.send_request(**request_body)
        return response.json()

    # 充值受限查詢
    def get_recharge_limit(self):
        request_body = {
            "method": "get",
            "url": "/v1/fund/getRechargeLimit",
        }
        response = self.send_request(**request_body)
        return response.json()

    # 获取所有充值方式列表
    def get_payment_channels(self, os_type=None,
                             rechargeTypeId=None):
        request_body = {
            "method": "get",
            "url": "/v1/fund/getPaymentChannel",
            "params": {"os-type": os_type},
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

# 充題操作
class Ratio(WebAPI):
    # 充值比例
    def get_ratio(self, currency=None):
        request_body = {
            "method": "get",
            "url": "/v1/fund/ratio",
            "params": {"currency": currency},
        }
        response = self.send_request(**request_body)
        return response.json()


# 提現操作
class Withdraw(WebAPI):
    # 發起提現
    def submit(self, device_id=None, os_type=None,
               amount=None, otpCode=None,
               # 提現方式 TRADITIONAL, USDT, TRANS_CENTER
               categoryCode=None, ratio=None, currency=None,
               cardId=None, addressId=None):
        request_body = {
            "method": "post",
            "url": "/v1/fund/withdraw/submit",
            "params": {"device-id": device_id, "os-type": os_type, "currency": currency},
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 提現配置
    def submit_info(self, withdrawAmount=None,
                    # 提現方式類型（TRADITIONAL、USDT、TRANS_CENTER）
                    categoryCode=None,
                    # TRADITIONAL請帶入BANKCARD、USDT時請帶入TRC、ERC其中一個、TRANS_CENTER請帶入GAOBAO
                    protocol=None, currency=None):
        request_body = {
            "method": "post",
            "url": "/v1/fund/withdraw/info",
            "params": {"currency": currency},
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 提現資格驗證
    def check(self):
        request_body = {
            "method": "post",
            "url": "/v1/fund/withdraw/check",
        }
        response = self.send_request(**request_body)
        return response.json()

    # 取消提現
    def cancel(self, orderId):
        request_body = {
            "method": "post",
            "url": f"/v1/fund/withdraw/cancel/{orderId}",
        }
        response = self.send_request(**request_body)
        return response.json()

    # 提現單詳情
    def get_order_info(self, orderId):
        request_body = {
            "method": "get",
            "url": f"/v1/fund/withdraw/{orderId}",
        }
        response = self.send_request(**request_body)
        return response.json()

    # 流水資料
    def water(self):
        request_body = {
            "method": "get",
            "url": "/v1/fund/withdraw/water",
        }
        response = self.send_request(**request_body)
        return response.json()

    # 處理中提現
    def processing(self):
        request_body = {
            "method": "get",
            "url": "/v1/fund/withdraw/processing",
        }
        response = self.send_request(**request_body)
        return response.json()

    # 提現分類入口
    def category(self):
        request_body = {
            "method": "get",
            "url": "/v1/fund/withdraw/category",
        }

        response = self.send_request(**request_body)
        return response.json()

    # 虛擬幣地址、銀行卡、交易所地址
    def address_info(self,currency='USD'):
        request_body = {
            "method": "get",
            "url": "/v1/fund/withdraw/address/info",
            "params": {"currency": currency}
        }

        response = self.send_request(**request_body)
        return response.json()
