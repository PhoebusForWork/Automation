from pylib.platform.account import AccountAdmin
from utils.generate_utils import Make


def super_admin_initialize_and_create_admin():
    accountAdmin = AccountAdmin()
    accountAdmin.first_login_password(username='superAdmin',
                                      oldPassword='abc123456',
                                      newPassword='abc1234567')
    code = accountAdmin.imgcode()
    accountAdmin.login(username="superAdmin",
                       password="abc1234567",
                       imgCode=code).json()['data']['token']
    accountAdmin.edit_password(oldPassword='abc1234567',
                               newPassword='abc123456')
    code = accountAdmin.imgcode()
    accountAdmin.login(username="superAdmin",
                       password="abc123456",
                       imgCode=code).json()['data']['token']

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
                        imgCode=code).json()['data']['token']
