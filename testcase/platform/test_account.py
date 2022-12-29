import pytest
import allure
import json
import random
from pylib.platform.userManage import userManage
from pylib.platform.platApiBase import PLAT_API
from testcase.platform.conftest import getPltLoginToken
from pylib.platform.accountAdmin import accountAdmin
from utils.data_utils import JsonReader
from utils.api_utils import API_Controller
from utils.generate_utils import Make

td = JsonReader()
testData = td.read_json5('test_account.json5')



#############
# test_case #
#############

@allure.feature("帳號登入登出模組")
@allure.story("帳號登入")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_account_login'))
def test_account_login(test, ):

    json_replace = td.replace_json(test["json"], test["target"])  # 替換完後下面參數要用json_replace去操作

    imgcode = PLAT_API()
    if json_replace['imgCode'] == "給我圖形驗證碼":
        json_replace['imgCode'] = str(
            imgcode.ImgCode(uuid=json_replace['uuid']))

    print(json_replace['uuid'])

    api = API_Controller()
    resp = api.HttpsClient(test["req_method"], test["req_url"], json_replace,
                           test["params"])

    assert resp.status_code == test["code_status"], resp.text
    assert test['keyword'] in resp.text



@allure.feature("組織結構") ###roleId參數會影響resp selected的值(true/false)
@allure.story("節點列表")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_dept_list'))
def test_dept_list(test, getPltLoginToken):
    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    if "[roleId]基本查詢" in test['scenario']:
        resp = resp.json()
        for d in resp['data']:
            if d['id'] == 2:
                assert d["selected"] is True
    else:
        assert test['keyword'] in resp.text

@allure.feature("組織結構")
@allure.story("新增節點")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_dept'))
def test_dept(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    if json_replace['department'] == "新增主節點":
        json_replace['department'] = json_replace['department']+str(random.randrange(99999))
        print(json_replace)
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("組織結構")
@allure.story("設置負責人")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_dept_leader'))
def test_dept_leader(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    # if json_replace['department'] == "新增主節點":
    #     json_replace['department'] = json_replace['department']+str(random.randrange(99999))
    #     print(json_replace)
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("組織結構")
@allure.story("關聯已存在帳號")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_dept_admin'))
def test_dept_admin(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    # if json_replace['department'] == "新增主節點":
    #     json_replace['department'] = json_replace['department']+str(random.randrange(99999))
    #     print(json_replace)
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("組織結構")
@allure.story("解除關聯")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_dept_delete_adminId'))
def test_dept_delete_adminId(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], test['json'],
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("組織結構")
@allure.story("修改節點")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_dept_put_departmentId'))
def test_dept_put_departmentId(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    # if json_replace['department'] == "新增主節點":
    #     json_replace['department'] = json_replace['department']+str(random.randrange(99999))
    #     print(json_replace)
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("組織結構")
@allure.story("刪除節點")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_dept_delete_departmentId'))
def test_dept_delete_departmentId(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("組織結構")
@allure.story("人員關係列表")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_dept_admin_list'))
def test_dept_admin_list(test, getPltLoginToken):
    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text

@allure.feature("角色管理")
@allure.story("創建角色")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_role'))
def test_role(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    if json_replace['role'] == "浣熊":
        json_replace['role'] = json_replace['role']+str(random.randrange(99999))
        print(json_replace)
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("角色管理")
@allure.story("編輯角色")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_put_role'))
def test_put_role(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("角色管理")
@allure.story("啟用/禁用/刪除角色")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_put_role_status'))
def test_put_role_status(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("角色管理")
@allure.story("顯示角色權限")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_get_role_status'))
def test_get_role_status(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("角色管理")
@allure.story("角色列表/搜尋角色")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_role_list'))
def test_role_list(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text



@allure.feature("帳號列表")
@allure.story("搜尋帳號")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_admin'))
def test_admin(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("帳號列表")
@allure.story("編輯帳號")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_edit_admin'))
def test_edit_admin(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("帳號列表")
@allure.story("刪除帳號")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_delete_admin'))
def test_delete_admin(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("帳號列表")
@allure.story("更改帳號狀態")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_admin_status'))
def test_admin_status(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("帳號列表")
@allure.story("重置帳號密碼")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_admin_resetPassword'))
def test_admin_resetPassword(test, getPltLoginToken):

    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("帳號列表")
@allure.story("修改帳號密碼")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_admin_password'))
def test_admin_password(test, getPltLoginToken):

    api = PLAT_API()
    code = api.ImgCode()
    resp = api.Login(username='charlie3344', password='abc123456', imgCode=code)
    admin_token = resp.json()['data']['token']

    json_replace = td.replace_json(test['json'], test['target'])
    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=admin_token)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("帳號列表")
@allure.story("新增帳號")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_admin_add_account'))
def test_admin_add_account(test, getPltLoginToken ):

    json_replace = td.replace_json(test['json'], test['target'])
    if test['scenario'] == "正常新增帳號":
        json_replace['phone'] = Make.mobile()
        new_name = Make.name()
        json_replace['account'] = new_name
        json_replace['displayName'] = new_name
        print(json_replace)


    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("帳號列表")
@allure.story("快捷检索员工列表")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_admin_quick_search'))
def test_admin_quick_search(test, getPltLoginToken ):

    json_replace = td.replace_json(test['json'], test['target'])

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text


@allure.feature("帳號列表")
@allure.story("搜尋帳號列表")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_get_admin'))
def test_get_admin(test, getPltLoginToken ):

    json_replace = td.replace_json(test['json'], test['target'])

    api = API_Controller()
    resp = api.HttpsClient(test['req_method'], test['req_url'], json_replace,
                           test['params'], token=getPltLoginToken)
    assert resp.status_code == test['code_status'], resp.text
    assert test['keyword'] in resp.text



@allure.feature("頁面結構")
@allure.story("權限列表")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case( 'test_authority_permission'))
def test_authority_permission(test, getPltLoginToken):

    api = API_Controller()
    resp = api.HttpsClient(test["req_method"], test["req_url"], test["json"],
                           test["params"], token=getPltLoginToken)
    assert resp.status_code == test["code_status"], resp.text
    assert test["keyword"] in resp.text


@allure.feature("頁面結構")
@allure.story("權限總列表")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_authority_list'))
def test_authority_list(test, getPltLoginToken):


    api = API_Controller()
    resp = api.HttpsClient(test["req_method"], test["req_url"], test["json"],
                           test["params"], token=getPltLoginToken)
    assert resp.status_code == test["code_status"], resp.text
    assert test["keyword"] in resp.text


@allure.feature("頁面結構")
@allure.story("選單樹列表")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case( 'test_authority_menu'))
def test_authority_menu(test, getPltLoginToken):


    api = API_Controller()
    resp = api.HttpsClient(test["req_method"], test['req_url'], test["json"],
                           test["params"], token=getPltLoginToken)
    assert resp.status_code == test["code_status"], resp.text
    assert test["keyword"] in resp.text



@allure.feature("平台模組")
@allure.story("取得平台資訊")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_platform'))
def test_platform(test, getPltLoginToken):


    api = API_Controller()
    resp = api.HttpsClient(test["req_method"], test["req_url"], test["json"],
                           test["params"], token=getPltLoginToken)
    assert resp.status_code == test["code_status"], resp.text
    assert test["keyword"] in resp.text



@allure.feature("帳號登入登出模組")
@allure.story("新帳號重設密碼")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_account_login_resetPassword'))
def test_account_login_resetPassword(test, getPltLoginToken):

    json_replace = td.replace_json(test["json"], test["target"])

    print(json)
    print(json_replace)
    if json_replace["account"] == "建立新帳號":
        new_account = accountAdmin()
        json_replace["account"] = str(new_account.add_account_auto(platToken=getPltLoginToken))
    print(json)
    print(json_replace)

    api = API_Controller()
    resp = api.HttpsClient(test["req_method"], test["req_url"], json_replace,
                           test["params"], token=getPltLoginToken)
    assert resp.status_code == test["code_status"], resp.text
    assert test["keyword"] in resp.text


@allure.feature("帳號登入登出模組")
@allure.story("帳號登出")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_account_logout'))
def test_account_logout(test, getPltLoginToken):


    api = API_Controller()
    resp = api.HttpsClient(test["req_method"], test["req_url"], test["json"],
                           test["params"], token=getPltLoginToken)
    assert resp.status_code == test["code_status"], resp.text
    assert test["keyword"] in resp.text


@allure.feature("帳號登入登出模組")
@allure.story("取得圖形驗證碼")
@allure.title("{scenario}")
@pytest.mark.parametrize("test", td.get_case('test_login_imgCode'))
def test_login_imgCode(test, getPltLoginToken):


    api = API_Controller()
    resp = api.HttpsClient(test["req_method"], test["req_url"], test["json"],
                           test["params"], token=getPltLoginToken)
    assert resp.status_code == test["code_status"], resp.text
    assert test["keyword"] in resp.text