from cgi import test
from webbrowser import get
import pytest
import allure
import json
import random
from pylib.platform.accountAdmin import accountAdmin
from pylib.platform.proxy import proxyChannel
from utils.dataUtils import Utils
from utils.APIControler import API_Conttoler

td = Utils()
# testData = td.read_json('test_proxy_channel.json')
testData = td.read_json('test_proxy.json')

# 置入彈性
# @allure.feature("代理渠道測試")
# @pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord",td.get_test_case(testData,'proxy_test'))
# def test_proxy_channel(test_case, req_method, req_url, scenario, json, params, code_status, keyWord,getPltLoginToken):
#     try:
#         if json['channel'] == "不重複名稱":
#             json['channel'] = json['channel']+str(random.randrange(99999))
#     except :
#         pass
#     api = API_Conttoler()
#     resp = api.HttpsClient(req_method,req_url,json,params,token=getPltLoginToken)
#     assert resp.status_code == code_status ,resp.text
#     assert keyWord in resp.text

@allure.feature("代理團隊測試")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord",td.get_test_case(testData,'proxy_test'))
def test_proxy_group(test_case, req_method, req_url, scenario, json, params, code_status, keyWord,getPltLoginToken):
    try:
        if json['groupName'] == "不重複名稱":
            json['groupName'] = json['groupName']+str(random.randrange(99999))
    except :
        pass
    api = API_Conttoler()
    resp = api.HttpsClient(req_method,req_url,json,params,token=getPltLoginToken)
    assert resp.status_code == code_status ,resp.text
    assert keyWord in resp.text


