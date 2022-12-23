import pytest
import allure
import random
from pylib.platform.userManage import userManage
from pylib.platform.proxy import ProxyChannel, ProxyGroup, ProxyManage
from testcase.platform.conftest import getPltLoginToken
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller
from utils.generate_utils import Make

td = JsonReader()
testData = td.read_json5('test_proxy.json5')


######################
#  setup & teardown  #
######################

@pytest.fixture(scope="module", autouse=True)  # 清除代理審核列表
def clean(getPltLoginToken):
    yield
    clean = ProxyManage()
    clean.clean_proxy_approval(token=getPltLoginToken)


#############
# test_case #
#############

class Test_Proxy_Channel():
    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("新增代理渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_add_channel'))
    def test_proxy_add_channel(test, getPltLoginToken):

        if test['json']['channel'] == "不重複名稱":
            test['json']['channel'] = test['json']['channel'] + \
                str(random.randrange(99999))

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("編輯代理渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_edit_channel'))
    def test_proxy_edit_channel(test, getPltLoginToken):

        if test['json']['channel'] == "不重複名稱":
            test['json']['channel'] = test['json']['channel'] + \
                str(random.randrange(99999))

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("刪除代理渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_delete_channel'))
    def test_proxy_delete_channel(test, getPltLoginToken):

        if '存在id' in test['req_url']:
            channel_id = ProxyChannel()
            test['req_url'] = test['req_url'].replace("存在id", str(
                channel_id.get_available_channel_auto(platToken=getPltLoginToken)))

            pass
        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("獲取所有渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_get_channel_all'))
    def test_proxy_get_channel_all(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("獲取所有未綁定渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_available_channel'))
    def test_proxy_available_channel(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("獲取渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_get_channel'))
    def test_proxy_get_channel(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class Test_Proxy_Group():
    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("新增代理團隊")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_add_group'))
    def test_proxy_add_group(test, getPltLoginToken):

        if test['json']['groupName'] == "不重複名稱":
            test['json']['groupName'] = test['json']['groupName'] + \
                str(random.randrange(99999))
        if test['json']['channelIds'] == "未綁定channel":
            req = ProxyChannel()
            test['json']['channelIds'] = [
                req.get_available_channel_auto(platToken=getPltLoginToken)]

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("編輯代理團隊")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_edit_group'))
    def test_proxy_edit_group(test, getPltLoginToken):

        if test['json']['groupName'] == "不重複名稱":
            test['json']['groupName'] = test['json']['groupName'] + \
                str(random.randrange(99999))
        if test['json']['channelIds'] == "未綁定channel":
            req = ProxyChannel()
            test['json']['channelIds'] = [
                req.get_available_channel_auto(platToken=getPltLoginToken)]

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("刪除代理團隊")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_delete_group'))
    def test_proxy_delete_group(test, getPltLoginToken):
        if "存在groupId" in test['req_url']:
            groupId = ProxyGroup()
            test['req_url'] = test['req_url'].replace("存在groupId", str(
                groupId.get_exist_group_auto(platToken=getPltLoginToken)))

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("取得團隊資訊")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_get_groupsAndChannels'))
    def test_proxy_get_groupsAndChannels(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


class Test_Proxy_Commission():
    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("建立佣金模板")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_add_commission'))
    def test_proxy_add_commission(test, getPltLoginToken):

        if test['json']['name'] == "不重複名稱":
            test['json']['name'] = test['json']['name'] + \
                str(random.randrange(99999))

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("編輯佣金模板")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_edit_commission_template'))
    def test_proxy_edit_commission_template(test, getPltLoginToken):

        test['json'] = td.replace_json(test['json'], test['target'])

        if test['json']['name'] == "不重複名稱":
            test['json']['name'] = test['json']['name'] + \
                str(random.randrange(99999))

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("查詢下級代理佣金設置")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_get_commission_template_subCommissionConfig'))
    def test_proxy_get_commission_template_subCommissionConfig(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("編輯下級代理佣金設置")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_edit_commission_template_subCommissionConfig'))
    def test_proxy_edit_commission_template_subCommissionConfig(test, getPltLoginToken):

        test['json'] = td.replace_json(test['json'], test['target'])

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("查詢佣金模板")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_commission_template'))
    def test_proxy_commission_template(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("查詢佣金模板下拉選單")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_commission_list'))
    def test_proxy_commission_list(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("查詢結算分攤")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_get_commission'))
    def test_proxy_get_commission(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("編輯結算分攤")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_edit_commission'))
    def test_proxy_edit_commission(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("查詢平台費分攤")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_get_settlementShares'))
    def test_proxy_get_settlementShares(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("編輯平台費分攤")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_edit_platformFeeShares'))
    def test_proxy_edit_platformFeeShares(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("查詢設置返佣")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_get_commissionConfig'))
    def test_proxy_get_commissionConfig(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("編輯設置返佣")
    @allure.title("{test[scenario]}")
    @pytest.mark.parametrize("test", td.get_case('proxy_edit_commissionConfig'))
    def test_proxy_edit_commissionConfig(test, getPltLoginToken):

        api = API_Controller()
        resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                               test['params'], token=getPltLoginToken)
        assert resp.status_code == test['code_status'], resp.text
        assert test['keyword'] in resp.text


@allure.feature("代理列表")
@allure.story("創建代理")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_add_proxy'))
def test_proxy_add_proxy(test, getPltLoginToken):

    if test['json']['proxyAccount'] == "不重複名稱":
        test['json']['proxyAccount'] = 'proxyAccount' + \
            str(random.randrange(99999))

    if test['json']['telephone'] == "不重複手機號":
        test['json']['telephone'] = Make.mobile()

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理列表")
@allure.story("獲取代理列表")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_proxy_list'))
def test_proxy_proxy_list(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理列表")
@allure.story("代理驗證")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_proxy_validate'))
def test_proxy_proxy_validate(test, getPltLoginToken):
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理列表")
@allure.story("修改子代理上限")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_proxy_subCount'))
def test_proxy_proxy_subCount(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理列表")
@allure.story("申請佣金模式變更")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_proxy_commission'))
def test_proxy_proxy_commission(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    clean = userManage()
    clean.cleanApproval(platToken=getPltLoginToken,
                        optType="COMMISSION_CHANGE")
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理列表")
@allure.story("編輯代理渠道")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_proxy_channel'))
def test_proxy_proxy_channel(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理列表")
@allure.story("查詢代理列表編輯資訊")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_get_edit_detail'))
def test_proxy_get_edit_detail(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理列表")
@allure.story("查詢代理列表顯示資訊")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_get_edit_display'))
def test_proxy_get_edit_display(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理列表")
@allure.story("查詢三個月平均佣金")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_get_commission_avg'))
def test_proxy_get_commission_avg(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理列表")
@allure.story("查詢交易信息")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_get_tradeInfo'))
def test_proxy_get_tradeInfo(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理帳號審核")
@allure.story("代理帳號審核列表")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_get_manage_list'))
def test_proxy_get_manage_list(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理帳號審核")
@allure.story("代理帳號審批人列表")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_get_manage_approver_list'))
def test_proxy_get_manage_approver_list(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理帳號審核")
@allure.story("代理帳號審_一審")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_manage_approver_first'))
def test_proxy_manage_approver_first(test, getPltLoginToken):
    if "待審核訂單" in test['req_url']:
        orderid = ProxyManage()
        test['req_url'] = test['req_url'].replace(
            "待審核訂單", orderid.get_first_approval_id(token=getPltLoginToken))
    if "一審完成訂單" in test['req_url']:
        orderid = ProxyManage()
        test['req_url'] = test['req_url'].replace(
            "一審完成訂單", orderid.get_second_approval_id(token=getPltLoginToken))
    if "二審完成訂單" in test['req_url']:
        orderid = ProxyManage()
        test['req_url'] = test['req_url'].replace(
            "二審完成訂單", orderid.get_second_approval_success_id(token=getPltLoginToken))

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理帳號審核")
@allure.story("代理帳號審_二審")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_manage_approver_second'))
def test_proxy_manage_approver_second(test, getPltLoginToken):
    if "待審核訂單" in test['req_url']:
        orderid = ProxyManage()
        test['req_url'] = test['req_url'].replace(
            "待審核訂單", orderid.get_second_approval_id(token=getPltLoginToken))
    if "二審完成訂單" in test['req_url']:
        orderid = ProxyManage()
        test['req_url'] = test['req_url'].replace(
            "二審完成訂單", orderid.get_second_approval_success_id(token=getPltLoginToken))

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理帳號上分紀錄")
@allure.story("查詢上分紀錄")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_get_credit_detail'))
def test_proxy_get_credit_detail(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("代理帳號上分紀錄")
@allure.story("調整充值額度")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", td.get_case('proxy_edit_credit'))
def test_proxy_edit_credit(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    clean = userManage()
    clean.cleanApproval(platToken=getPltLoginToken, optType="CREDIT_CHANGE")
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text
