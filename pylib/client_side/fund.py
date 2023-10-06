# -*- coding: utf-8 -*-
import jsonpath
from ..client_side.webApiBase import WebAPI
from utils.api_utils import KeywordArgument
from utils.data_utils import EnvReader
from utils.generate_utils import Make

env = EnvReader()
web_host = env.WEB_HOST


# 提現操作
class Withdraw(WebAPI):
    # 發起提現
    def submit(self, device_id, os_type,
               amount, otpCode,
               # 提現方式 TRADITIONAL, USDT, TRANS_CENTER
               categoryCode,
               cardId, addressId):
        request_body = {
            "method": "post",
            "url": "/v1/fund/withdraw/submit",
            "params": {"device-id": device_id, "os-type": os_type},
            "json": KeywordArgument.body_data()
        }
        response = self.send_request(**request_body)
        return response.json()

    # 提現配置
    def submit_info(self, withdrawAmount,
                    # 提現方式類型（TRADITIONAL、USDT、TRANS_CENTER）
                    categoryCode,
                    # TRADITIONAL請帶入BANKCARD、USDT時請帶入TRC、ERC其中一個、TRANS_CENTER請帶入GAOBAO
                    protocol):
        request_body = {
            "method": "post",
            "url": "/v1/fund/withdraw/info",
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
    def address_info(self):
        request_body = {
            "method": "get",
            "url": "/v1/fund/withdraw/address/info",
        }

        response = self.send_request(**request_body)
        return response.json()
