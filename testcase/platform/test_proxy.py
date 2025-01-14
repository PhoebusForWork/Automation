import pytest
import allure
import random
import jsonpath
from pylib.platform.user import UserManage
from pylib.platform.account import AccountAdmin
from pylib.platform.proxy import Proxy, ProxyChannel, ProxyGroup, ProxyManage, ProxyOperation, CommissionAdjust
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller
from utils.generate_utils import Make

test_data = TestDataReader()
test_data.read_json5("test_proxy.json5")

######################
#  setup & teardown  #
######################


# @pytest.fixture(scope="module", autouse=True)  # 清除代理審核列表
# def clean(get_platform_token):
#     yield
#     clean = ProxyManage()
#     clean.clean_proxy_approval(token=get_platform_token)


#############
# test_case #
#############


class TestProxyChannel:
    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("新增代理渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_add_channel"))
    def test_proxy_add_channel(test, get_platform_token):
        if test["json"]["channel"] == "不重複名稱":
            test["json"]["channel"] = test["json"]["channel"] + str(
                random.randrange(99999)
            )

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("編輯代理渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_edit_channel"))
    def test_proxy_edit_channel(test, get_platform_token):
        if test["json"]["channel"] == "不重複名稱":
            test["json"]["channel"] = test["json"]["channel"] + str(
                random.randrange(99999)
            )

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("刪除代理渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_delete_channel"))
    def test_proxy_delete_channel(test, get_platform_token):
        if "存在id" in test["req_url"]:
            channel_id = ProxyChannel()
            test["req_url"] = test["req_url"].replace(
                "存在id",
                str(
                    channel_id.get_available_channel_auto(plat_token=get_platform_token)
                ),
            )

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("獲取所有渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_get_channel_all"))
    def test_proxy_get_channel_all(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("獲取所有未綁定渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_available_channel"))
    def test_proxy_available_channel(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("獲取渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_get_channel"))
    def test_proxy_get_channel(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)


class TestProxyGroup:
    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("新增代理團隊")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_add_group"))
    def test_proxy_add_group(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        if json_replace["groupName"] == "不重複名稱":
            json_replace["groupName"] = json_replace["groupName"] + str(
                random.randrange(99999)
            )
        if json_replace["channelIds"] == "未綁定channel":
            req = ProxyChannel()
            json_replace["channelIds"] = [
                req.get_available_channel_auto(plat_token=get_platform_token)
            ]

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("編輯代理團隊")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_edit_group"))
    def test_proxy_edit_group(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        if json_replace["groupName"] == "不重複名稱":
            json_replace["groupName"] = json_replace["groupName"] + str(
                random.randrange(99999)
            )
        if json_replace["channelIds"] == "未綁定channel":
            req = ProxyChannel()
            json_replace["channelIds"] = [
                req.get_available_channel_auto(plat_token=get_platform_token)
            ]

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("刪除代理團隊")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_delete_group"))
    def test_proxy_delete_group(test, get_platform_token):
        if "存在groupId" in test["req_url"]:
            groupId = ProxyGroup()
            test["req_url"] = test["req_url"].replace(
                "存在groupId",
                str(groupId.get_exist_group_auto(plat_token=get_platform_token)),
            )

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("渠道及團隊")
    @allure.story("取得團隊資訊")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_get_groupsAndChannels"))
    def test_proxy_get_groupsAndChannels(test, get_platform_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            params_replace,
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)


class TestProxyCommission:
    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("建立佣金模板")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_add_commission"))
    def test_proxy_add_commission(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        if json_replace["name"] == "不重複名稱":
            json_replace["name"] = json_replace["name"] + str(random.randrange(99999))

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("編輯佣金模板")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test", test_data.get_case("proxy_edit_commission_template")
    )
    def test_proxy_edit_commission_template(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])

        if json_replace["name"] == "不重複名稱":
            json_replace["name"] = json_replace["name"] + str(random.randrange(99999))

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("查詢下級代理佣金設置")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test",
        test_data.get_case("proxy_get_commission_template_sub_commission_conditions"),
    )
    def test_proxy_get_commission_template_subCommissionConditions(
        test, get_platform_token
    ):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("編輯下級代理佣金設置")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test",
        test_data.get_case("proxy_edit_commission_template_sub_commission_conditions"),
    )
    def test_proxy_edit_commission_template_subCommissionConditions(
        test, get_platform_token
    ):
        json_replace = test_data.replace_json(test["json"], test["target"])

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("查詢佣金模板")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_commission_template"))
    def test_proxy_commission_template(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("查詢佣金模板下拉選單")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_commission_list"))
    def test_proxy_commission_list(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("查詢結算分攤")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_get_settlement_shares"))
    def test_proxy_get_settlement_shares(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("編輯結算分攤")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_edit_settlement_shares"))
    def test_proxy_edit_settlement_shares(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("查詢平台費分攤")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test", test_data.get_case("proxy_get_platform_fee_shares")
    )
    def test_proxy_get_platform_fee_shares(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("編輯平台費分攤")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test", test_data.get_case("proxy_edit_platform_fee_shares")
    )
    def test_proxy_edit_platform_fee_shares(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("查詢設置返佣")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test", test_data.get_case("proxy_get_commission_conditions")
    )
    def test_proxy_get_commission_conditions(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金模式管理")
    @allure.story("編輯設置返佣")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "test", test_data.get_case("proxy_edit_commission_conditions")
    )
    def test_proxy_edit_commission_conditions(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)


class TestProxy:
    @staticmethod
    @allure.feature("代理列表")
    @allure.story("創建代理")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_add_proxy"))
    def test_proxy_add_proxy(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        if json_replace["proxyAccount"] == "不重複名稱":
            json_replace["proxyAccount"] = "proxyAccount" + str(random.randrange(99999))

        if json_replace["telephone"] == "不重複手機號":
            json_replace["telephone"] = Make.mobile()

        if json_replace["email"] == "不重複Email":
            json_replace["email"] = "proxyEmail" + str(random.randrange(99999)) + "@testgmail.com"

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("獲取代理列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_proxy_list"))
    def test_proxy_proxy_list(test, get_platform_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            params_replace,
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("校驗代理帳號")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_proxy_validate"))
    def test_proxy_proxy_validate(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("修改子代理上限")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_proxy_subCount"))
    def test_proxy_proxy_subCount(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("申請佣金模式變更")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_proxy_commission"))
    def test_proxy_proxy_commission(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        clean = UserManage()
        clean.clean_approval(plat_token=get_platform_token, optType="COMMISSION_CHANGE")
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("編輯代理渠道")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_proxy_channel"))
    def test_proxy_proxy_channel(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        clean = UserManage()
        clean.clean_approval(plat_token=get_platform_token, optType="CHANNEL_CHANGE")
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("查詢交易信息")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_get_tradeInfo"))
    def test_proxy_get_tradeInfo(test, get_platform_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            params_replace,
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("搜尋代理域名")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_proxy_domain_query"))
    def test_get_proxy_domain_query(test, get_platform_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller()
        resp = api.send_request(test["req_method"],
                                test["req_url"],
                                test["json"],
                                params_replace,
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("更新代理備註")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_proxy_remark"))
    def test_proxy_proxy_remark(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("搜尋代理銀行卡")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_get_bank_cards"))
    def test_get_proxy_bank_cards(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)
        # 先用sql塞資料，等小網自動化完成之後可以移除sql

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("申請刪除代理提款銀行卡")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_bankcard_unbind"))
    def test_proxy_unbind_bankcard(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        if "銀行卡" in test["json"]['cardId']:
            proxy = Proxy()
            ret = proxy.get_bankcards(plat_token=get_platform_token, proxyId=2)
            card_id = jsonpath.jsonpath(ret, "$.data[0].cardId")
            test["json"]['cardId'] = card_id[0]

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("風險分析重複IP")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_get_risk_same_ip"))
    def test_get_proxy_risk_same_ip(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            params_replace,
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("代理登入日誌")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_get_login_info"))
    def test_get_proxy_login_info(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        print(test["params"])
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            params_replace,
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理列表")
    @allure.story("查詢代理列表顯示資訊")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_get_detail_display"))
    def test_get_proxy_detail_display(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

class TestProxyOperation:
    @staticmethod
    @allure.feature("操作記錄")
    @allure.story("代理用戶操作記錄")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_get_operation_log"))
    def test_get_operation_log(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            params_replace,
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

class TestProxyManage:
    @staticmethod
    @allure.feature("代理帳號審核")
    @allure.story("代理帳號審核列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_get_manage_list"))
    def test_proxy_get_manage_list(test, get_platform_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            params_replace,
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理帳號審核")
    @allure.story("代理帳號審批人列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_get_manage_approver_list"))
    def test_proxy_get_manage_approver_list(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            test["json"],
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理帳號審核")
    @allure.story("代理帳號審_一審")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_manage_approver_first"))
    def test_proxy_manage_approver_first(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        if "待審核訂單" in test["req_url"]:
            orderid = ProxyManage()
            test["req_url"] = test["req_url"].replace(
                "待審核訂單", orderid.get_first_approval_id(token=get_platform_token)
            )
        if "一審完成訂單" in test["req_url"]:
            orderid = ProxyManage()
            test["req_url"] = test["req_url"].replace(
                "一審完成訂單", orderid.get_second_approval_id(token=get_platform_token)
            )
        if "二審完成訂單" in test["req_url"]:
            orderid = ProxyManage()
            test["req_url"] = test["req_url"].replace(
                "二審完成訂單", orderid.get_second_approval_success_id(token=get_platform_token)
            )

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("代理帳號審核")
    @allure.story("代理帳號審_二審")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_manage_approver_second"))
    def test_proxy_manage_approver_second(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        if "待審核訂單" in test["req_url"]:
            orderid = ProxyManage()
            test["req_url"] = test["req_url"].replace(
                "待審核訂單", orderid.get_second_approval_id(token=get_platform_token)
            )
        if "二審完成訂單" in test["req_url"]:
            orderid = ProxyManage()
            test["req_url"] = test["req_url"].replace(
                "二審完成訂單", orderid.get_second_approval_success_id(token=get_platform_token)
            )

        api = API_Controller()
        resp = api.send_request(
            test["req_method"],
            test["req_url"],
            json_replace,
            test["params"],
            token=get_platform_token,
        )
        ResponseVerification.basic_assert(resp, test)


# class TestProxyCredit:
#     @staticmethod
#     @allure.feature("代理帳號上分紀錄")
#     @allure.story("查詢上分紀錄")
#     @allure.title("{test[scenario]}")
#     @pytest.mark.regression
#     @pytest.mark.parametrize("test", test_data.get_case("proxy_get_credit_detail"))
#     def test_proxy_get_credit_detail(test, get_platform_token):
#         params_replace = test_data.replace_json(test["params"], test["target"])
#         api = API_Controller()
#         resp = api.send_request(
#             test["req_method"],
#             test["req_url"],
#             test["json"],
#             params_replace,
#             token=get_platform_token,
#         )
#         ResponseVerification.basic_assert(resp, test)

#     @staticmethod
#     @allure.feature("代理帳號上分紀錄")
#     @allure.story("調整充值額度")
#     @allure.title("{test[scenario]}")
#     @pytest.mark.regression
#     @pytest.mark.parametrize("test", test_data.get_case("proxy_edit_credit"))
#     def test_proxy_edit_credit(test, get_platform_token):
#         json_replace = test_data.replace_json(test["json"], test["target"])
#         if "存在id" == test["json"]['userId']:
#             proxy = Proxy()
#             ret = proxy.get_proxy(queryType=0,input='proxy001')
#             user_id = jsonpath.jsonpath(ret, "$.data.[0].userId")
#             test["json"]['userId'] = user_id[0]
#         api = API_Controller()
#         resp = api.send_request(
#             test["req_method"],
#             test["req_url"],
#             json_replace,
#             test["params"],
#             token=get_platform_token,
#         )
#         clean = UserManage()
#         clean.clean_approval(plat_token=get_platform_token, optType="CREDIT_CHANGE")
#         ResponseVerification.basic_assert(resp, test)


class TestProxyDomain:
    # 編輯域名
    @staticmethod
    @allure.feature("代理訊息")
    @allure.story("編輯域名")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("edit_proxy_domain"))
    def test_edit_proxy_domain(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        api = API_Controller()
        resp = api.send_request(test["req_method"],
                                test["req_url"],
                                json_replace,
                                test["params"],
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 取得推廣域名
    @staticmethod
    @allure.feature("代理訊息")
    @allure.story("取得推廣域名")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_proxy_domain_promotion_link"))
    def test_get_proxy_domain_promotion_link(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test["req_method"],
                                test["req_url"],
                                test["json"],
                                test["params"],
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

class TestCommissionAdjust:
    @staticmethod
    @allure.feature("佣金調整審核")
    @allure.story("查詢列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_commission_adjust_list"))
    def test_get_commission_adjust_list(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金調整審核")
    @allure.story("審核狀態")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_proxy_manage_status"))
    def test_get_proxy_manage_status(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金調整審核")
    @allure.story("佣金結算審批人列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_approver_list"))
    def test_get_approver_list(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金調整審核")
    @allure.story("佣金調整申請")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("commission_adjust"))
    def test_commission_adjust(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金調整審核")
    @allure.story("佣金調整一審")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("commission_adjust_first_approve"))
    def test_commission_adjust_first_approve(test, get_platform_token):
        
        adjust = CommissionAdjust()
        adjust.post_commission_adjust(plat_token=get_platform_token, detailId=1, reason='test', amount=1)
        adjust.post_commission_adjust(plat_token=get_platform_token, detailId=2, reason='test', amount=1)

        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("佣金調整審核")
    @allure.story("佣金調整二審")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("commission_adjust_second_approve"))
    def test_commission_adjust_second_approve(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])

        if "isPass[false]" in test["scenario"]:
            adjust = CommissionAdjust()
            adjust.post_commission_adjust(plat_token=get_platform_token, detailId=2, reason='test', amount=1)
            ret = adjust.get_proxy_commission_adjust(plat_token=get_platform_token, From='2023-07-22T16:00:00+08:00', to='2033-07-22T16:00:00+08:00', status=0)
            
            records = ret.get("data", {}).get("records", [])
            adjust.edit_commission_adjust_first_approve(plat_token=get_platform_token, id=records[0].get("id"), remark="test1", isPass=True)

            test["req_url"] = test["req_url"].replace("待審ID", str(records[0].get("id")))

        accountAdmin = AccountAdmin()
        accountAdmin.admin_status(plat_token=get_platform_token, adminId=3, status=1)

        code = accountAdmin.imgcode()
        token = accountAdmin.login(username="account002",
                               password="abc123456",
                               imgCode=code).json()['data']['token']

        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=token)
        accountAdmin.admin_status(plat_token=get_platform_token, adminId=3, status=0)
        ResponseVerification.basic_assert(resp, test)


class TestCommission:
    # 佣金結算查詢
    @staticmethod
    @allure.feature("佣金結算")
    @allure.story("佣金結算查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_proxy_commission"))
    def test_get_proxy_commission(test, get_platform_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller()
        resp = api.send_request(test["req_method"],
                                test["req_url"],
                                test["json"],
                                params_replace,
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 查詢公司總輸贏
    @staticmethod
    @allure.feature("佣金結算")
    @allure.story("查詢公司總輸贏")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_proxy_commission_winTotal"))
    def test_get_proxy_winTotal(test, get_platform_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller()
        resp = api.send_request(test["req_method"],
                                test["req_url"],
                                test["json"],
                                params_replace,
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 查詢下級會員佣金
    @staticmethod
    @allure.feature("佣金結算")
    @allure.story("查詢下級會員佣金")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_proxy_subUser_commission"))
    def test_get_proxy_subUser_commission(test, get_platform_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller()
        resp = api.send_request(test["req_method"],
                                test["req_url"],
                                test["json"],
                                params_replace,
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 查詢下級代理佣金
    @staticmethod
    @allure.feature("佣金結算")
    @allure.story("查詢下級代理佣金")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_proxy_subProxy_commission"))
    def test_get_proxy_subProxy_commission(test, get_platform_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller()
        resp = api.send_request(test["req_method"],
                                test["req_url"],
                                test["json"],
                                params_replace,
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 佣金結算歷史查詢
    @staticmethod
    @allure.feature("佣金結算")
    @allure.story("佣金結算歷史查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_proxy_commission_history"))
    def test_get_proxy_commission_history(test, get_platform_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller()
        resp = api.send_request(test["req_method"],
                                test["req_url"],
                                test["json"],
                                params_replace,
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 結算狀態列表
    @staticmethod
    @allure.feature("佣金結算")
    @allure.story("結算狀態列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_proxy_commission_grant_status"))
    def test_get_proxy_commission_grant_status(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test["req_method"],
                                test["req_url"],
                                test["json"],
                                test["params"],
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 查詢成本分攤
    @staticmethod
    @allure.feature("佣金結算")
    @allure.story("查詢成本分攤")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("get_proxy_commission_cost_share"))
    def test_get_proxy_commission_cost_share(test, get_platform_token):
        params_replace = test_data.replace_json(test["params"], test["target"])
        api = API_Controller()
        resp = api.send_request(test["req_method"],
                                test["req_url"],
                                test["json"],
                                params_replace,
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 佣金發放一審
    @staticmethod
    @allure.feature("佣金結算")
    @allure.story("佣金發放一審")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_commission_firstApprove"))
    def test_put_proxy_commission_firstApprove(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])
        api = API_Controller()
        resp = api.send_request(test["req_method"],
                                test["req_url"],
                                json_replace,
                                test["params"],
                                token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 佣金發放二審
    @staticmethod
    @allure.feature("佣金結算")
    @allure.story("佣金發放二審")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case("proxy_commission_secondApprove"))
    def test_put_proxy_commission_secondApprove(test, get_platform_token):
        json_replace = test_data.replace_json(test["json"], test["target"])

        accountAdmin = AccountAdmin()
        accountAdmin.admin_status(plat_token=get_platform_token, adminId=3, status=1)

        code = accountAdmin.imgcode()
        token = accountAdmin.login(username="account002",
                               password="abc123456",
                               imgCode=code).json()['data']['token']

        api = API_Controller()
        resp = api.send_request(test["req_method"],
                                test["req_url"],
                                json_replace,
                                test["params"],
                                token=token)
        accountAdmin.admin_status(plat_token=get_platform_token, adminId=3, status=0)
        ResponseVerification.basic_assert(resp, test)