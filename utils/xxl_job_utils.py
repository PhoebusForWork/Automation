from .api_utils import API_Controller


class XxlJobs:
    @staticmethod
    def game_transfer_executor():
        xxl = API_Controller(platform='xxl')
        xxl.send_request(method='post', url='/xxl-job-admin/login',
                         json={}, params={"userName": "admin", "password": "123456"})
        """
        這裡因確認三方排程在實作上會經過三次確認後才判定為異常訂單,故須模擬認完3次改變訂單狀態
        """
        transfer_executor_count = 3
        for _ in range(transfer_executor_count):
            xxl.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                             json={}, params={"id": 1, "executorParam": None, "addressList": None})

    @staticmethod
    def sync_plt_basics_data():
        xxl = API_Controller(platform='xxl')
        xxl.send_request(method='post', url='/xxl-job-admin/login',
                         json={}, params={"userName": "admin", "password": "123456"})
        xxl.send_request(method='post', url='/xxl-job-admin/jobinfo/trigger',
                         json={}, params={"id": 15, "executorParam": "{\"pltCode\": \"ldpro\"}", "addressList": None})
