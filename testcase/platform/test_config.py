import pytest
import allure
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller
from utils.generate_utils import Make
from pylib.platform.config import Avatar, Make_config_data

test_data = TestDataReader()
test_data.read_json5('test_config.json5')


######################
#  setup & teardown  #
######################


@pytest.fixture(scope="module")
def make_config_action_log_data(get_platform_token):
    Make_config_data(token=get_platform_token).make_action_log_data()


#############
# test_case #
#############
# 電信商管理
class TestCountryCodeRelationManage:
    # 電信商查詢
    @staticmethod
    @allure.feature("電信商管理")
    @allure.story("電信商查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('get_relation_manage'))
    def test_get_relation_manage(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # 修改電信商
    @staticmethod
    @allure.feature("電信商管理")
    @allure.story("修改電信商")
    @allure.title("{test[scenario]}")
    @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('edit_relation_manage'))
    def test_edit_relation_manage(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


# 幣別管理
class TestCurrency:
    @staticmethod
    @allure.feature("幣別管理")
    @allure.story("站點幣別查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_platform_currency'))
    def test_get_platform_currency(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


class TestBasicConfiguration:
    @staticmethod
    @allure.feature("基本配置")
    @allure.story("新增頭像")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('add_config_avatar'))
    def test_add_config_avatar(test, get_platform_token):

        json_replace = test_data.replace_json(test['json'], test['target'])

        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("基本配置")
    @allure.story("編輯頭像")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_config_avatar'))
    def test_edit_config_avatar(test, get_platform_token):

        json_replace = test_data.replace_json(test['json'], test['target'])

        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("基本配置")
    @allure.story("刪除頭像")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('delete_config_avatar'))
    def test_delete_config_avatar(test, get_platform_token):
        if "存在id" in test['req_url']:
            id = Avatar()
            test['req_url'] = test['req_url'].replace("存在id", str(
                id.get_delete_avatar(plat_token=get_platform_token)))
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("基本配置")
    @allure.story("依照條件進行查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_config_avatars'))
    def test_get_config_avatars(test, get_platform_token):
        json_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                json_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("基本配置")
    @allure.story("依頭像id進行查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_config_avatar_one'))
    def test_get_config_avatar_one(test, get_platform_token):
        if "存在id" in test['req_url']:
            id = Avatar()
            test['req_url'] = test['req_url'].replace("存在id", str(
                id.get_delete_avatar(plat_token=get_platform_token)))
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


class TestFileUpload:
    @staticmethod
    @allure.feature("檔案上傳")
    @allure.story("上傳圖片")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('file_image_upload'))
    def test_file_image_upload(test, get_platform_token):
        if test['files'] == 'null':
            files = None
        else:
            files = [('file', ('upload_image_charliebrown.jpeg',
                               open('resources/upload_file/upload_image_charliebrown.jpeg', 'rb'), 'image/jpeg'))]
        api = API_Controller()
        api.request_session.headers.update({"Content-Type": None})
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token, files=files)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("檔案上傳")
    @allure.story("上傳影片")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('file_video_upload'))
    def test_file_video_upload(test, get_platform_token):
        if test['files'] == 'null':
            files = None
        else:
            files = [('file', ('upload_video_realshort.mp4',
                               open('resources/upload_file/upload_video_realshort.mp4', 'rb'),
                               'application/octet-stream'))]
        api = API_Controller()
        api.request_session.headers.update({"Content-Type": None})
        resp = api.send_request(test['req_method'], test['req_url'], test['json'], test['params'],
                                token=get_platform_token, files=files)
        ResponseVerification.basic_assert(resp, test)


class TestCurrencyManagement:
    @staticmethod
    @allure.feature("幣別管理")
    @allure.story("站點幣別上下架修改")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('edit_currency'))
    def test_edit_currency(test, get_platform_token):
        parmas_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                parmas_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("幣別管理")
    @allure.story("站點幣別查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_platform_currency'))
    def test_get_platform_currency(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("幣別管理")
    @allure.story("站點幣別下拉選單(排序)")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_drop_down'))
    def test_get_drop_down(test, get_platform_token):
        parmas_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                parmas_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


class TestLanguageManagement:
    @staticmethod
    @allure.feature("語系管理")
    @allure.story("站點語系查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_platform_language'))
    def test_get_platform_language(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


class TestOperationLog:
    @staticmethod
    @allure.feature("操作日誌")
    @allure.story("查詢後台用戶操作登入日誌")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_admin_action_log'))
    def test_get_admin_action_log(test, get_platform_token, make_config_action_log_data):
        if test["params"]["to"] == "today_date_to":
            test["params"].update({"from": Make.date('start'), "to": Make.date('end')})
        params_replace = test_data.replace_json(test['params'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                params_replace, token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


class TestCountryCodeManagement:
    @staticmethod
    @allure.feature("電話區碼管理")
    @allure.story("電話區碼查詢")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('get_country_code_manage'))
    def test_get_country_code_manage(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("電話區碼管理")
    @allure.story("修改電話區碼")
    @allure.title("{test[scenario]}")
    @pytest.mark.regression
    @pytest.mark.parametrize("test", test_data.get_case('put_country_code_manage'))
    def test_put_country_code_manage(test, get_platform_token):
        json_replace = test_data.replace_json(test['json'], test['target'])
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)


class TestDomainManagement:
    # @staticmethod
    # @allure.feature("應用域名管理")
    # @allure.story("編輯應用域名")
    # @allure.title("{test[scenario]}")
    # @pytest.mark.regression
    # @pytest.mark.parametrize("test", test_data.get_case('edit_domain'))
    # def test_edit_domain(test, get_platform_token):
    #     api = API_Controller()
    #     resp = api.send_request(test['req_method'], test['req_url'], test['json'],
    #                             test['params'], token=get_platform_token)
    #     ResponseVerification.basic_assert(resp, test)
    #
    # @staticmethod
    # @allure.feature("應用域名管理")
    # @allure.story("刪除應用域名")
    # @allure.title("{test[scenario]}")
    # @pytest.mark.regression
    # @pytest.mark.parametrize("test", test_data.get_case('delete_domain'))
    # def test_delete_domain(test, get_platform_token):
    #     api = API_Controller()
    #     resp = api.send_request(test['req_method'], test['req_url'], test['json'],
    #                             test['params'], token=get_platform_token)
    #     ResponseVerification.basic_assert(resp, test)

    @staticmethod
    @allure.feature("應用域名管理")
    @allure.story("應用域名列表")
    @allure.title("{test[scenario]}")
    @pytest.mark.test
    @pytest.mark.parametrize("test", test_data.get_case('get_domain'))
    def test_get_domain(test, get_platform_token):
        api = API_Controller()
        resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                                test['params'], token=get_platform_token)
        ResponseVerification.basic_assert(resp, test)

    # @staticmethod
    # @allure.feature("應用域名管理")
    # @allure.story("新增應用域名")
    # @allure.title("{test[scenario]}")
    # @pytest.mark.regression
    # @pytest.mark.parametrize("test", test_data.get_case('add_domain'))
    # def test_add_domain(test, get_platform_token):
    #     api = API_Controller()
    #     resp = api.send_request(test['req_method'], test['req_url'], test['json'],
    #                             test['params'], token=get_platform_token)
    #     ResponseVerification.basic_assert(resp, test)

    # @staticmethod
    # @allure.feature("應用域名管理")
    # @allure.story("應用類型")
    # @allure.title("{test[scenario]}")
    # @pytest.mark.regression
    # @pytest.mark.parametrize("test", test_data.get_case('get_type'))
    # def test_get_type(test, get_platform_token):
    #     api = API_Controller()
    #     resp = api.send_request(test['req_method'], test['req_url'], test['json'],
    #                             test['params'], token=get_platform_token)
    #     ResponseVerification.basic_assert(resp, test)
