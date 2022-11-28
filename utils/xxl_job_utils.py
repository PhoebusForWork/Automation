from .api_utils import API_Controller
# from .api_utils_V2 import API_Controller


class XxlJobs():
    @staticmethod
    def game_transfer_executor():
        xxl = API_Controller(platfrom='xxl')
        xxl.HttpsClient(reqMethod='post', reqUrl='/xxl-job-admin/login',
                        json={"userName": "admin", "password": "123456"}, params={})
        """
        這裡因確認三方排程在實作上會經過三次確認後才判定為異常訂單,故須模擬認完3次改變訂單狀態
        """
        transfer_executor_count = 3
        for _ in range(transfer_executor_count):
            resp = xxl.HttpsClient(reqMethod='post', reqUrl='/xxl-job-admin/jobinfo/trigger',
                                   json={"id": 1, "executorParam": None, "addressList": None}, params={})
