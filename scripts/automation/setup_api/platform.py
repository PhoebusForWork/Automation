from pylib.platform.account import AccountAdmin, AccountDept, AccountRole
from pylib.platform.proxy import Proxy, ProxyChannel, ProxyGroup, ProxyCommissionTemplate, ProxyManage
from pylib.platform.game import Game
from pylib.platform.config import CountryCodeRelation
from utils.generate_utils import Make
import random


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
    role.add_role(role='測試員', departmentIds=[1], authorityIds=[619, 625])


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
    accountAdmin = AccountAdmin()
    code = accountAdmin.imgcode()
    token = accountAdmin.login(username="superAdmin",
                               password="abc123456",
                               imgCode=code).json()['data']['token']
    
    create_proxy = Proxy(token=token)
    apprival = ProxyManage(token)
    account_list = ['proxy01', 'proxy02', 'proxy03']
    telephone_list = ['13645609354', '13645604382', '13645604399']
    i=1
    for account_name in account_list:
        create_proxy.add_proxy(proxyAccount=account_name,
                               pwd="abc123456",
                               email=account_name + "@gmailtest.com",
                               countryCode='86',
                               telephone=telephone_list[i-1],
                               proxyChannelId=1,
                               commissionId=1)
        
        apprival.approval_first(id=i, isApprove=True, remark="test")
        apprival.approval_second(id=i, isApprove=True, remark="test")
        i = i + 1

def create_proxy_channel_Group():
    accountAdmin = AccountAdmin()
    code = accountAdmin.imgcode()
    token = accountAdmin.login(username="superAdmin",
                               password="abc123456",
                               imgCode=code).json()['data']['token']

    proxyChannel = ProxyChannel(token=token)
    proxyChannel.add_channel(channel="代理渠道")
    proxyGroup = ProxyGroup(token=token)
    proxyGroup.add_group(groupName="代理團隊", channelIds=[1])


def create_proxy_commissionTemplate():
    template = ProxyCommissionTemplate()
    code = template.imgcode()
    template.login(username="superAdmin",password="abc123456",imgCode=code)
    template.add_template(name="佣金模板", isEnabled=True, isNeedToVerify=False, platformFeeShare=100)

    #設定下級代理佣金配置
    subConditions=[{"commissionLimit": 0,"commission": 100,"proxyCount": 1}]
    subSubConditions=[{"commissionLimit": 0,"commission": 100,"proxyCount": 1}]
    json={subConditions, subSubConditions}
    template.edit_commission_conditions(id=1, json=json)

    #設定反佣 
    condiction=[{ "profit": 1, "commissionLimit": 0, "commission": 100, "validUserCount": 1}]
    template.edit_commission_conditions(id=1, json=condiction)
    

def sync_relation_manage():
    sync_relation = CountryCodeRelation()
    code = sync_relation.imgcode()
    sync_relation.login(username="superAdmin",
                        password="abc123456",
                        imgCode=code)
    sync_relation.edit_manage(item=[{"thirdPartyId":8,"countryCodeId":5}])
