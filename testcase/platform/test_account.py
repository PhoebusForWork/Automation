import pytest
import allure
import time
from pylib.platform.platApiBase import PlatformAPI
from pylib.platform.account import AccountAdmin, AccountDept, AccountRole
from utils.data_utils import TestDataReader, ResponseVerification
from utils.api_utils import API_Controller
from utils.generate_utils import Make

test_data = TestDataReader()
test_data.read_json5('test_account.json5')

######################
#  setup & teardown  #
######################


@pytest.fixture(scope="module")  # 將密碼重置為可登入狀態
def re_password_default(get_platform_token):
    api = PlatformAPI()
    code = api.imgcode()
    resp = api.login(username='charlieadmin100', password='abc12345', imgCode=code)
    admin_token = resp.json()['data']['token']
    reapi = AccountAdmin()
    reapi.edit_password(plat_token=admin_token, oldPassword='abc12345', newPassword='abc123456')

#############
# test_case #
#############


@allure.feature("帳號登入登出模組")
@allure.story("帳號登入")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_account_login'))
def test_account_login(test, ):

    json_replace = test_data.replace_json(test["json"], test["target"])  # 替換完後下面參數要用json_replace去操作
    img_code = PlatformAPI()
    if json_replace['imgCode'] == "給我圖形驗證碼":
        json_replace['imgCode'] = str(
            img_code.imgcode(uuid=json_replace['uuid']))
    api = API_Controller()
    resp = api.send_request(test["req_method"], test["req_url"], json_replace,
                            test["params"])
    ResponseVerification.basic_assert(resp, test)


@allure.feature("組織結構")  # roleId參數會影響resp selected的值(true/false)
@allure.story("節點列表")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_dept_list'))
def test_dept_list(test, get_platform_token):
    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    assert resp.status_code == test['code_status'], resp.text

    if "[roleId]基本查詢" == test['scenario']:
        resp = resp.json()
        for d in resp['data']:
            if d['id'] == test['params']['roleId']:
                assert d["selected"] is True
    else:
        ResponseVerification.basic_assert(resp, test)


@allure.feature("組織結構")
@allure.story("新增節點")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_dept'))
def test_dept(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    now = time.time()
    if json_replace['department'] == "新增主節點":
        json_replace['department'] = json_replace['department']+str(int(now))
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("組織結構")
@allure.story("設置負責人")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_dept_leader'))
def test_dept_leader(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("組織結構")
@allure.story("關聯已存在帳號")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_dept_admin'))
def test_dept_admin(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("組織結構")
@allure.story("解除關聯")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_dept_delete_admin_id'))
def test_dept_delete_admin_id(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], test['json'],
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("組織結構")
@allure.story("修改節點")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_dept_put_department_id'))
def test_dept_put_department_id(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("組織結構")
@allure.story("刪除節點")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_dept_delete_department_id'))
def test_dept_delete_department_id(test, get_platform_token):

    if test["scenario"] == "正確帶入參數":
        dep_id = AccountDept()
        test['req_url'] = test['req_url'].replace(
            "要刪除的節點", dep_id.find_dept_id(plat_token=get_platform_token))

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("組織結構")
@allure.story("人員關係列表")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_dept_admin_list'))
def test_dept_admin_list(test, get_platform_token):
    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("角色管理")
@allure.story("創建角色")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_role'))
def test_role(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    now = time.time()
    if json_replace['role'] == "auto":
        json_replace['role'] = json_replace['role']+str(int(now))
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("角色管理")
@allure.story("編輯角色")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_put_role'))
def test_put_role(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("角色管理")
@allure.story("啟用/禁用/刪除角色")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_put_role_status'))
def test_put_role_status(test, get_platform_token):

    if test["scenario"] == "軟刪":
        role_id = AccountRole()
        test['req_url'] = test['req_url'].replace(
            "更換role_id", role_id.find_role_id(plat_token=get_platform_token))

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("角色管理")
@allure.story("顯示角色權限")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_get_role_status'))
def test_get_role_status(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("角色管理")
@allure.story("角色列表/搜尋角色")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_role_list'))
def test_role_list(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號列表")
@allure.story("搜尋帳號")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_admin'))
def test_admin(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號列表")
@allure.story("編輯帳號")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_edit_admin'))
def test_edit_admin(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)

    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號列表")
@allure.story("新增帳號")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_admin_add_account'))
def test_admin_add_account(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    if test['scenario'] == "正常新增帳號":
        json_replace['phone'] = Make.mobile()
        new_name = Make.name()
        json_replace['account'] = new_name
        json_replace['displayName'] = new_name
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號列表")
@allure.story("刪除帳號")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_delete_admin'))
def test_delete_admin(test, get_platform_token):
    if test["scenario"] == "正常刪除":
        dep_id = AccountAdmin()
        test['req_url'] = test['req_url'].replace(
            "未登入帳號", dep_id.find_admin_id(plat_token=get_platform_token))
    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號列表")
@allure.story("更改帳號狀態")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_admin_status'))
def test_admin_status(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號列表")
@allure.story("重置帳號密碼")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_admin_reset_password'))
def test_admin_reset_password(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號列表")
@allure.story("修改帳號密碼")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_admin_password'))
def test_admin_password(test, get_platform_token, re_password_default):
    api = PlatformAPI()
    code = api.imgcode()
    if test['scenario'] == "正常修改密碼":
        resp = api.login(username='charlieadmin100', password='abc123456', imgCode=code)
    else:
        resp = api.login(username='charlieadmin100', password='abc12345', imgCode=code)
    admin_token = resp.json()['data']['token']
    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace, test['params'], token=admin_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號列表")
@allure.story("快捷检索员工列表")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_admin_quick_search'))
def test_admin_quick_search(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號列表")
@allure.story("搜尋帳號列表")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_get_admin'))
def test_get_admin(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號列表")
@allure.story("修改偏好語言")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_put_admin_language'))
def test_put_admin_language(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號列表")
@allure.story("修改偏好貨幣")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_put_admin_currency'))
def test_put_admin_currency(test, get_platform_token):

    json_replace = test_data.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.send_request(test['req_method'], test['req_url'], json_replace,
                            test['params'], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("頁面結構")
@allure.story("權限列表")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_authority_permission'))
def test_authority_permission(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test["req_method"], test["req_url"], test["json"],
                            test["params"], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("頁面結構")
@allure.story("權限總列表")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_authority_list'))
def test_authority_list(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test["req_method"], test["req_url"], test["json"],
                            test["params"], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("頁面結構")
@allure.story("選單樹列表")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_authority_menu'))
def test_authority_menu(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test["req_method"], test['req_url'], test["json"],
                            test["params"], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("平台模組")
@allure.story("取得平台資訊")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_platform'))
def test_platform(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test["req_method"], test["req_url"], test["json"],
                            test["params"], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號登入登出模組")
@allure.story("新帳號重設密碼")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_account_login_reset_password'))
def test_account_login_reset_password(test, get_platform_token):

    json_replace = test_data.replace_json(test["json"], test["target"])
    if json_replace["account"] == "建立新帳號":
        new_account = AccountAdmin()
        json_replace["account"] = str(new_account.add_account_auto(plat_token=get_platform_token))
    api = API_Controller()
    resp = api.send_request(test["req_method"], test["req_url"], json_replace,
                            test["params"], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號登入登出模組")
@allure.story("帳號登出")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_account_logout'))
def test_account_logout(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test["req_method"], test["req_url"], test["json"],
                            test["params"], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)


@allure.feature("帳號登入登出模組")
@allure.story("取得圖形驗證碼")
@allure.title("{test[scenario]}")
@pytest.mark.parametrize("test", test_data.get_case('test_login_img_code'))
def test_login_img_code(test, get_platform_token):

    api = API_Controller()
    resp = api.send_request(test["req_method"], test["req_url"], test["json"],
                            test["params"], token=get_platform_token)
    ResponseVerification.basic_assert(resp, test)



