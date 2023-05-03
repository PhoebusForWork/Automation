from pylib.platform.account import AccountAdmin
from pylib.platform.proxy import Proxy
from pylib.platform.game import Game
from utils.generate_utils import Make


def super_admin_initialize_and_create_admin():
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
    code = accountAdmin.imgcode()
    accountAdmin.login(username="superAdmin",
                       password="abc123456",
                       imgCode=code)

    account_list = ['account001', 'account002', 'account003', 'deltest001']
    for account_name in account_list:
        accountAdmin.add_admin(account=account_name,
                               deptId=3,
                               displayName=account_name,
                               phone=Make.mobile(),
                               password='abc1234567',
                               isLeader=1,
                               roleIds=[3])


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
