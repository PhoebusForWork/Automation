import pytest
import allure

from pylib.platform.fund import WithdrawConfig
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller

test_data = TestDataReader()
test_data.read_json5('test_fund.json5')


class TestWithdraw:
    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("通用配置查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_config_common'))
    def test_get_config_common(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("通用配置修改")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('modify_config_common'))
    def test_modify_config_common(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("通用配置修改確認")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    def test_modified_config_common(get_platform_token):
        config_setting = WithdrawConfig(token=get_platform_token)
        config_setting.common_config_setting()
        res = config_setting.get_common_config_setting()
        daily_max_limit = res["data"]["dailyMaxLimit"]
        is_open_withdraw = res["data"]["isOpenWithdraw"]
        multiple = res["data"]["multiple"]
        assert daily_max_limit == 10000000, "後台 daily_max_limit 未被更改"
        assert is_open_withdraw == 1, "後台 is_open_withdraw 未被更改"
        assert multiple == 3, "後台 multiple 未被更改"

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("小額配置查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_config_small'))
    def test_get_config_small(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("小額配置修改")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('modify_config_small'))
    def test_modify_config_small(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("小額配置白名單查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_config_white_small'))
    def test_get_config_white_small(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("小額配置白名單新增")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('add_config_white_small'))
    def test_add_config_white_small(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("小額配置白名單刪除")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('delete_config_white_small'))
    def test_delete_config_white_small(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        if "存在id" in test['req_url']:
            white_small = WithdrawConfig(token=get_platform_token)
            test['req_url'] = test['req_url'].replace("存在id", str(
                white_small.find_small_white_list_id()))
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("大額配置查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_config_large'))
    def test_get_config_large(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("大額配置修改")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('modify_config_large'))
    def test_modify_config_large(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("大額配置白名單查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_config_white_large'))
    def test_get_config_white_large(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("大額配置白名單新增")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('add_config_white_large'))
    def test_add_config_white_large(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("大額配置白名單刪除")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('delete_config_white_large'))
    def test_delete_config_white_large(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        if "存在id" in test['req_url']:
            white_large = WithdrawConfig(token=get_platform_token)
            test['req_url'] = test['req_url'].replace("存在id", str(
                white_large.find_large_white_list_id()))
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("代理傳統提款配置查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_config_proxy'))
    def test_get_config_proxy(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("代理傳統提款配置修改")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('modify_config_proxy'))
    def test_modify_config_proxy(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("出款匯總查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_summary_list'))
    def test_get_summary_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("操作記錄查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_operation_records'))
    def test_get_operation_records(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("提現方式類型查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_category_types'))
    def test_get_category_types(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("提現方式類型設置查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_category_list'))
    def test_get_category_list(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("提現方式類型設置更新")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('modify_category'))
    def test_modify_category(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("異常策略設置查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_config_policy'))
    def test_get_config_policy(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("提現相關配置")
    @allure.story("異常策略設置更新")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('modify_config_policy'))
    def test_modify_config_policy(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("審核分配")
    @allure.story("查詢審核分配列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_distribute_list'))
    def test_get_distribute_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("審核分配")
    @allure.story("查詢審核分配列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_distribute_list'))
    def test_get_distribute_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("審核分配")
    @allure.story("審核分配派單")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('distribute_dispatch'))
    def test_distribute_dispatch(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("審核分配")
    @allure.story("審核分配派單回收")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('distribute_dispatch_recovery'))
    def test_distribute_dispatch_recovery(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("審核分配")
    @allure.story("審核分配派單批量派單")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('distribute_dispatch_batch'))
    def test_distribute_dispatch_batch(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("審核分配")
    @allure.story("審核分配派單批量回收")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('distribute_dispatch_recovery_batch'))
    def test_distribute_dispatch_recovery_batch(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款審核")
    @allure.story("查詢出款審核列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_audit_list'))
    def test_get_audit_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款審核")
    @allure.story("出款審核通過")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('audit_pass'))
    def test_audit_pass(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款審核")
    @allure.story("出款審核拒絕")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('audit_refuse'))
    def test_audit_refuse(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款分配")
    @allure.story("出款分配列表查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_approve_distribute_list'))
    def test_get_approve_distribute_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款分配")
    @allure.story("出款分配方式查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_approver_dispatch_type'))
    def test_get_approver_dispatch_type(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款分配")
    @allure.story("出款分配派單")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('approver_dispatch'))
    def test_approver_dispatch(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款分配")
    @allure.story("出款分配派單回收")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('approver_recovery'))
    def test_approver_recovery(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款分配")
    @allure.story("出款分配派單批量派單")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('approver_dispatch_batch'))
    def test_approver_dispatch_batch(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款分配")
    @allure.story("出款分配派單批量回收")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('approver_dispatch_recovery_batch'))
    def test_approver_dispatch_recovery_batch(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款操作")
    @allure.story("查詢出款操作列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_approve_list'))
    def test_get_approve_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款操作")
    @allure.story("出款操作通過")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('approve_pass'))
    def test_approve_pass(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款操作")
    @allure.story("出款操作出拒絕")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('approve_refuse'))
    def test_approve_refuse(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("出款操作")
    @allure.story("出款操作-商戶下拉")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_approve_merchants'))
    def test_get_approve_merchants(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("異常提現處理")
    @allure.story("異常提現處理列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_exception_list'))
    def test_get_exception_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("異常提現處理")
    @allure.story("異常提現處理通過")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('exception_pass'))
    def test_exception_pass(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("異常提現處理")
    @allure.story("異常提現處理拒絕")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('exception_refuse'))
    def test_exception_refuse(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("異常出款")
    @allure.story("異常出款列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_unusual_list'))
    def test_get_unusual_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("異常出款")
    @allure.story("異常出款查看")
    @allure.title("{test[scenario]}")
    @pytest.mark.xfail(reason="尚未实现该请求所需功能")
    # @pytest.mark.regression
    # 尚未實作
    @pytest.mark.parametrize("test", test_data.get_case('unusual_manual'))
    def test_unusual_manual(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("回調異常")
    @allure.story("回調異常列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_error_list'))
    def test_get_error_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("回調異常")
    @allure.story("回調異常強制回收")
    @allure.title("{test[scenario]}")
    # @pytest.mark.regression
    # 尚未實作
    @pytest.mark.xfail(reason="尚未实现该请求所需功能")
    @pytest.mark.parametrize("test", test_data.get_case('error_recovery'))
    def test_error_recovery(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


class TestRecharge:
    @staticmethod
    @allure.feature("充值列表")
    @allure.story("充值匯總列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_recharge_manage_list'))
    def test_get_recharge_manage_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值列表")
    @allure.story("充值補單列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_recharge_manage_supplement_list'))
    def test_get_recharge_manage_supplement_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值列表")
    @allure.story("充值補單列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_recharge_manage_proxy_replace_list'))
    def test_get_recharge_manage_proxy_replace_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值列表")
    @allure.story("充值匯總頁籤")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_recharge_manage_query_third_party_list'))
    def test_get_recharge_manage_query_third_party_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值列表")
    @allure.story("申請補單-充值紀錄頁籤")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_recharge_manage_request_supplement_list'))
    def test_get_recharge_manage_request_supplement_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值列表")
    @allure.story("拒絕補單-充值紀錄頁籤")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_recharge_manage_request_supplement_reject_list'))
    def test_get_recharge_manage_request_supplement_reject_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值列表")
    @allure.story("查詢補單審核人列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_recharge_manage_auditor_list'))
    def test_get_recharge_manage_auditor_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值列表")
    @allure.story("查詢補單申請人列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_recharge_manage_applicant_list'))
    def test_get_recharge_manage_applicant_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值列表")
    @allure.story("補單一審-充值補單審核頁籤")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('recharge_manage_supplement_approve_first'))
    def test_recharge_manage_supplement_approve_first(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值列表")
    @allure.story("補單二審-充值補單審核頁籤")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('recharge_manage_supplement_approve_second'))
    def test_recharge_manage_supplement_approve_second(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值受限")
    @allure.story("充值受限配置列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('risk_manage_recharge_limit_record'))
    def test_risk_manage_recharge_limit_record(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值受限")
    @allure.story("保存充值受限配置列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('risk_manage_config_save'))
    def test_risk_manage_config_save(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值受限")
    @allure.story("保存充值受限配置列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('risk_manage_config'))
    def test_risk_manage_config(test, get_platform_token):
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值方式類型")
    @allure.story("充值方式類型列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('recharge_type_list'))
    def test_recharge_type_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值方式類型")
    @allure.story("查詢模板類型")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('recharge_type_list_view_type'))
    def test_recharge_type_list_view_type(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值方式類型")
    @allure.story("查詢驗證類型")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('recharge_type_list_verify_type'))
    def test_recharge_type_list_verify_type(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值方式類型")
    @allure.story("新增充值方式類型")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('recharge_type_save'))
    def test_recharge_type_save(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值方式類型")
    @allure.story("更新充值方式類型")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('recharge_type_update'))
    def test_recharge_type_update(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值方式類型")
    @allure.story("充值方式類型順序更新")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('recharge_type_sort'))
    def test_recharge_type_sort(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值設置")
    @allure.story("區塊鏈幣值")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('blockchain_currency_list'))
    def test_blockchain_currency_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值設置")
    @allure.story("查詢充值方式")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('payment_manage_list'))
    def test_payment_manage_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值設置")
    @allure.story("查詢自動充值應用")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('payment_merchant_manage_list'))
    def test_payment_merchant_manage_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值設置")
    @allure.story("查詢商戶列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('payment_merchant_account_manage_list'))
    def test_payment_merchant_account_manage_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值設置")
    @allure.story("查詢所有自動充值應用")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('payment_merchant_all_currency_manage_list'))
    def test_payment_merchant_all_currency_manage_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值設置")
    @allure.story("查詢所有自動充值應用")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('payment_merchant_all_currency_manage_list'))
    def test_payment_merchant_all_currency_manage_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值設置")
    @allure.story("查詢所有自動充值應用")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('payment_merchant_channel_list'))
    def test_payment_merchant_channel_list(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值設置")
    @allure.story("通道分析")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('payment_manage_channel_report'))
    def test_payment_manage_channel_report(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值設置")
    @allure.story("添加第三方充值應用")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('payment_manage_add_merchant'))
    def test_payment_manage_add_merchant(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("充值設置")
    @allure.story("添加第三方充值應用")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('payment_manage_update_merchant'))
    def test_payment_manage_update_merchant(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)
