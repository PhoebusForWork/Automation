from pylib.platform.account import AccountAdmin, AccountDept, AccountRole
from pylib.platform.proxy import Proxy
from pylib.platform.game import Game
from pylib.platform.config import CountryCodeRelation
from utils.generate_utils import Make


def super_admin_initialize():
    accountAdmin = AccountAdmin()
    accountAdmin.first_login_password(username='superAdmin',
                                      oldPassword='abc123456',
                                      newPassword='abc1234567')
    code = accountAdmin.imgcode()
    accountAdmin.login(username="superAdmin",
                       password="abc1234567",
                       imgCode=code)
    accountAdmin.edit_password(oldPassword='abc1234567',
                               newPassword='abc123456')

def create_dept_and_role():
    accountAdmin = AccountAdmin()
    code = accountAdmin.imgcode()
    token = accountAdmin.login(username="superAdmin",
                               password="abc123456",
                               imgCode=code).json()['data']['token']

    dept = AccountDept(token=token)
    dept.add_dept(department='測試組')
    role = AccountRole(token=token)
    role.add_role(role='測試員', departmentIds=[1], authorityIds=[])


def create_account():
    accountAdmin = AccountAdmin()
    code = accountAdmin.imgcode()
    accountAdmin.login(username="superAdmin",
                       password="abc123456",
                       imgCode=code)

    account_list = ['account001', 'account002', 'account003', 'deltest001']
    for account_name in account_list:
        accountAdmin.add_admin(account=account_name,
                               deptId=1,
                               displayName=account_name,
                               password='abc1234567',
                               isLeader=True,
                               roleIds=[2])

def login_account():
    login_account = AccountAdmin()
    login_account.first_login_password(username='account001',
                                       oldPassword='abc1234567',
                                       newPassword='abc123456')
    code = login_account.imgcode()
    login_account.login(username="account001",
                        password="abc123456",
                        imgCode=code)


def turn_on_the_game_to_test():
    '''
    用來開啟欲測試的遊戲讓他同步至前台cs_game
    '''
    trun_on_the_game = Game()
    code = trun_on_the_game.imgcode()
    trun_on_the_game.login(username="superAdmin",
                           password="abc123456",
                           imgCode=code)
    #  目前僅有AI體育可測試
    trun_on_the_game.edit_game_status(game_code='AI_SPORT_AI',
                                      status=True,
                                      currency='CNY')
    trun_on_the_game.edit_game_status(game_code='AI_SPORT_AI',
                                      status=True,
                                      currency='USD')
    trun_on_the_game.game_sync(game_code='AI_SPORT_AI')

def create_initialize_proxy_account():
    create_proxy = Proxy()
    code = create_proxy.imgcode()
    create_proxy.login(username="superAdmin",
                       password="abc123456",
                       imgCode=code)
    create_proxy.add_proxy(proxyAccount="", proxyName="",
                           password="", proxyChannelId="",
                           commissionId=None)

def sync_relation_manage():
    sync_relation = CountryCodeRelation()
    code = sync_relation.imgcode()
    sync_relation.login(username="superAdmin",
                        password="abc123456",
                        imgCode=code)
    sync_relation.edit_manage(thirdPartyId=1, countryCodeId=5)
