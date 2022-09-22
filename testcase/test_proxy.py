import pytest
import allure
import random
from pylib.platform.userManage import userManage
from pylib.platform.proxy import proxyChannel, proxyGroup, proxyManage
from testcase.conftest import getPltLoginToken
from utils.dataUtils import Utils
from utils.APIControler import API_Conttoler

td = Utils()
testData = td.read_json5('test_proxy.json5')


######################
#  setup & teardown  #
######################

@pytest.fixture(scope="session", autouse=True)  # 清除代理審核列表
def clean(getPltLoginToken):
    yield
    clean = proxyManage()
    clean.cleanProxyApproval(token=getPltLoginToken)


#############
# test_case #
#############

@allure.feature("渠道及團隊")
@allure.story("新增代理渠道")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_add_channel'))
def test_proxy_add_channel(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):
    try:
        if json['channel'] == "不重複名稱":
            json['channel'] = json['channel']+str(random.randrange(99999))
    except:
        pass
    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("渠道及團隊")
@allure.story("編輯代理渠道")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_edit_channel'))
def test_proxy_edit_channel(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("渠道及團隊")
@allure.story("刪除代理渠道")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_delete_channel'))
def test_proxy_delete_channel(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("渠道及團隊")
@allure.story("獲取所有渠道")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_channel_all'))
def test_proxy_get_channel_all(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("渠道及團隊")
@allure.story("獲取所有未綁定渠道")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_available_channel'))
def test_proxy_available_channel(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("渠道及團隊")
@allure.story("獲取渠道")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_channel'))
def test_proxy_get_channel(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("渠道及團隊")
@allure.story("新增代理團隊")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_add_group'))
def test_proxy_add_group(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):
    try:
        if json['groupName'] == "不重複名稱":
            json['groupName'] = json['groupName']+str(random.randrange(99999))
        if json['channelIds'] == "未綁定channel":
            req = proxyChannel()
            json['channelIds'] = [
                req.getAvailableChannel_auto(platToken=getPltLoginToken)]

    except:
        pass
    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("渠道及團隊")
@allure.story("編輯代理團隊")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_edit_group'))
def test_proxy_edit_group(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):
    try:
        if json['groupName'] == "不重複名稱":
            json['groupName'] = json['groupName']+str(random.randrange(99999))
        if json['channelIds'] == "未綁定channel":
            req = proxyChannel()
            json['channelIds'] = [
                req.getAvailableChannel_auto(platToken=getPltLoginToken)]

    except:
        pass
    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("渠道及團隊")
@allure.story("刪除代理團隊")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_delete_group'))
def test_proxy_delete_group(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):
    if "存在groupId" in req_url:
        groupId = proxyGroup()
        req_url = req_url.replace("存在groupId", str(
            groupId.getExistGroup_auto(platToken=getPltLoginToken)))

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("渠道及團隊")
@allure.story("取得團隊資訊")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_groupsAndChannels'))
def test_proxy_get_groupsAndChannels(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("佣金模式管理")
@allure.story("建立佣金模板")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_add_commission'))
def test_proxy_add_commission(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):
    try:
        if json['name'] == "不重複名稱":
            json['name'] = json['name']+str(random.randrange(99999))
    except:
        pass
    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("佣金模式管理")
@allure.story("查詢佣金模板")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_commission_template'))
def test_proxy_commission_template(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("佣金模式管理")
@allure.story("查詢佣金模板下拉選單")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_commission_list'))
def test_proxy_commission_list(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("佣金模式管理")
@allure.story("查詢結算分攤")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_commission'))
def test_proxy_get_commission(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("佣金模式管理")
@allure.story("編輯結算分攤")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_edit_commission'))
def test_proxy_edit_commission(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("佣金模式管理")
@allure.story("查詢平台費分攤")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_settlementShares'))
def test_proxy_get_settlementShares(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("佣金模式管理")
@allure.story("編輯平台費分攤")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_edit_platformFeeShares'))
def test_proxy_edit_platformFeeShares(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("佣金模式管理")
@allure.story("查詢設置返佣")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_commissionConfig'))
def test_proxy_get_commissionConfig(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("佣金模式管理")
@allure.story("編輯設置返佣")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_edit_commissionConfig'))
def test_proxy_edit_commissionConfig(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理列表")
@allure.story("創建代理")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_add_proxy'))
def test_proxy_add_proxy(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):
    try:
        if json['proxyAccount'] == "不重複名稱":
            json['proxyAccount'] = json['proxyAccount'] + \
                str(random.randrange(99999))
    except:
        pass
    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理列表")
@allure.story("獲取代理列表")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_proxy_list'))
def test_proxy_proxy_list(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理列表")
@allure.story("代理驗證")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_proxy_validate'))
def test_proxy_proxy_validate(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):
    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理列表")
@allure.story("修改子代理上限")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_proxy_subCount'))
def test_proxy_proxy_subCount(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理列表")
@allure.story("申請佣金模式變更")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_proxy_commission'))
def test_proxy_proxy_commission(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    clean = userManage()
    clean.cleanApproval(platToken=getPltLoginToken,
                        optType="COMMISSION_CHANGE")
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理列表")
@allure.story("編輯代理渠道")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_proxy_channel'))
def test_proxy_proxy_channel(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理列表")
@allure.story("查詢代理列表編輯資訊")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_edit_detail'))
def test_proxy_get_edit_detail(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理列表")
@allure.story("查詢代理列表顯示資訊")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_edit_display'))
def test_proxy_get_edit_display(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理列表")
@allure.story("查詢三個月平均佣金")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_commission_avg'))
def test_proxy_get_commission_avg(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理列表")
@allure.story("查詢交易信息")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_tradeInfo'))
def test_proxy_get_tradeInfo(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理帳號審核")
@allure.story("代理帳號審核列表")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_manage_list'))
def test_proxy_get_manage_list(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理帳號審核")
@allure.story("代理帳號審批人列表")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_manage_approver_list'))
def test_proxy_get_manage_approver_list(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理帳號審核")
@allure.story("代理帳號審_一審")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_manage_approver_first'))
def test_proxy_manage_approver_first(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):
    if "待審核訂單" in req_url:
        orderid = proxyManage()
        req_url = req_url.replace(
            "待審核訂單", orderid.getFirstApprovalId(token=getPltLoginToken))
    if "一審完成訂單" in req_url:
        orderid = proxyManage()
        req_url = req_url.replace(
            "一審完成訂單", orderid.getSecondApprovalId(token=getPltLoginToken))
    if "二審完成訂單" in req_url:
        orderid = proxyManage()
        req_url = req_url.replace(
            "二審完成訂單", orderid.getSecondApprovalSuccessId(token=getPltLoginToken))

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理帳號審核")
@allure.story("代理帳號審_二審")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_manage_approver_second'))
def test_proxy_manage_approver_second(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):
    if "待審核訂單" in req_url:
        orderid = proxyManage()
        req_url = req_url.replace(
            "待審核訂單", orderid.getSecondApprovalId(token=getPltLoginToken))
    if "二審完成訂單" in req_url:
        orderid = proxyManage()
        req_url = req_url.replace(
            "二審完成訂單", orderid.getSecondApprovalSuccessId(token=getPltLoginToken))

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理帳號上分紀錄")
@allure.story("查詢上分紀錄")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_get_credit_detail'))
def test_proxy_get_credit_detail(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text


@allure.feature("代理帳號上分紀錄")
@allure.story("調整充值額度")
@allure.title("{scenario}")
@pytest.mark.parametrize("test_case, req_method, req_url, scenario, json, params, code_status, keyWord", td.get_test_case(testData, 'proxy_edit_credit'))
def test_proxy_edit_credit(test_case, req_method, req_url, scenario, json, params, code_status, keyWord, getPltLoginToken):

    api = API_Conttoler()
    resp = api.HttpsClient(req_method, req_url, json,
                           params, token=getPltLoginToken)
    clean = userManage()
    clean.cleanApproval(platToken=getPltLoginToken, optType="CREDIT_CHANGE")
    assert resp.status_code == code_status, resp.text
    assert keyWord in resp.text
