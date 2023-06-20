from .api_utils import API_Controller
import json


class XxlJobs(API_Controller):
    def __init__(self, token=None):
        super().__init__(platform='xxl')
        if token:
            self.request_session.headers.update({"token": token})
        self.send_request(method='post', url='/xxl-job-admin/login',
                          json={}, params={"userName": "admin", "password": "123456"})

    def game_transfer_executor(self):
        # """
        # 這裡因確認三方排程在實作上會經過三次確認後才判定為異常訂單,故須模擬認完3次改變訂單狀態
        # """
        transfer_executor_count = 3
        for _ in range(transfer_executor_count):
            self.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                              json={}, params={"id": 1, "executorParam": None, "addressList": None})

    def sync_plt_basics_data(self, pltCode='ldpro'):
        executorParam = json.dumps({"pltCode": pltCode}, ensure_ascii=False)
        self.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                          json={}, params={"id": 11, "executorParam": executorParam, "addressList": None})

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
