from .api_utils import API_Controller
# from .api_utils_V2 import API_Controller


class XxlJobs():
    @staticmethod
    def game_transfer_executor():
        xxl = API_Controller(platfrom='xxl')
        xxl.HttpsClient(reqMethod='post', reqUrl='/xxl-job-admin/login',
                        json={"userName": "admin", "password": "123456"}, params={})
        for _ in range(3):
            resp = xxl.HttpsClient(reqMethod='post', reqUrl='/xxl-job-admin/jobinfo/trigger',
                                   json={"id": 1, "executorParam": None, "addressList": None}, params={})
