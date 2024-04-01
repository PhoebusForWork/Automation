from .api_utils import API_Controller
from utils.generate_utils import Make
import time
import json


class XxlJobs(API_Controller):
    def __init__(self, token=None):
        super().__init__(platform='xxl')
        if token:
            self.request_session.headers.update({"token": token})
        self.send_request(method='post', url='/xxl-job-admin/login',
                          json={}, params={"userName": "admin", "password": "abc123456"})

    def game_transfer_executor(self):
        # """
        # 這裡因確認三方排程在實作上會經過三次確認後才判定為異常訂單,故須模擬認完3次改變訂單狀態
        # """
        transfer_executor_count = 3
        for _ in range(transfer_executor_count):
            self.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                              json={}, params={"id": 5, "executorParam": None, "addressList": None})

    # 異常轉帳請求限制開關
    def game_transfer_fail(self, pltCode='ldpro', isTesting: bool = True):
        executorParam = json.dumps({"pltCode": pltCode, "isTesting": isTesting}, ensure_ascii=False)
        self.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                          json={}, params={"id": 18, "executorParam": executorParam, "addressList": None})

    def sync_plt_basics_data(self, pltCode='ldpro'):
        executorParam = json.dumps({"pltCode": pltCode}, ensure_ascii=False)
        self.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                          json={}, params={"id": 26, "executorParam": executorParam, "addressList": None})

    # 設定風控環境
    def set_message_risk_env(self, pltCode='ldpro', is_pro: bool = False):
        executorParam = json.dumps({"pltCode": pltCode, "isPro": is_pro}, ensure_ascii=False)
        self.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                          json={}, params={"id": 13, "executorParam": executorParam, "addressList": None})

    # 設定風控環境(用戶註冊與登入)
    def set_user_risk_env(self, pltCode='ldpro', is_pro: bool = False):
        executorParam = json.dumps({"pltCode": pltCode, "isPro": is_pro}, ensure_ascii=False)
        self.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                          json={}, params={"id": 15, "executorParam": executorParam, "addressList": None})

    def get_game_orders(self, pltCode='ldpro'):
        self.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                          json={}, params={"id": 2, "executorParam": str({"pltCode": pltCode}), "addressList": None})

    def sync_activity_category(self, pltCode='ldpro'):
        executorParam = json.dumps({"pltCode": pltCode}, ensure_ascii=False)
        self.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                          json={}, params={"id": 34, "executorParam": executorParam, "addressList": None})

    # 使用者VIP 設定新年點卷發放日期
    def sync_vip_festivalGift_date(self, sync_vip_date=None):
        form_date = Make.format_date(date=sync_vip_date, format='--%m-%d')
        executorParam = '{"pltCode":"ldpro","monthDay":"' + form_date + '"}'
        self.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                          json={}, params={"id": 35, "executorParam": executorParam, "addressList": None})

    # 使用者VIP 升降級與点券派發
    def sync_vip(self, sync_vip_date=None):
        self.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                          json={}, params={"id": 33, "executorParam": sync_vip_date, "addressList": None})
