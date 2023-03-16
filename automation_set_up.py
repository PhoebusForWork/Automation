# -*- coding: utf-8 -*-
import time
from pylib.contorl.control import ControlAPI
from pylib.platform.account import AccountAdmin
from utils.generate_utils import Make
from utils.database_utils import Postgresql

#############
#  總控配置  #
############
contorl = ControlAPI()
contorl.add_host_platform()
contorl.host_platform_sync_data()
wait_for_sync = 5
time.sleep(wait_for_sync)
#############
#  後台配置  #
############
accountAdmin = AccountAdmin()
accountAdmin.first_login_password(username='superAdmin',
                                  oldPassword='abc123456',
                                  newPassword='abc1234567')
code = accountAdmin.imgcode()
token = accountAdmin.login(username="superAdmin",
                           password="abc1234567",
                           imgCode=code).json()['data']['token']
accountAdmin.edit_password(oldPassword='abc1234567', newPassword='abc123456')
code = accountAdmin.imgcode()
token = accountAdmin.login(username="superAdmin",
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

login_account = AccountAdmin()
login_account.login

#plt_account SQL
plt_account = Postgresql(database='plt_account')
plt_account.run_sql('''
    UPDATE host_platform.platform SET secret = '7E79731B19717750E618A4E0EFF248DA6AE334BB0706A31BC36A690A51F1A8E1' WHERE id = 1;
    UPDATE plt_account.vs_admin SET last_login_time = '2023-03-06 04:01:21.203101 +00:00', last_login_device_id = '3263782594', last_login_ip = '61.220.72.61', last_modified_admin_id = 1, last_modified_admin = 'superAdmin' WHERE id = 2;
    INSERT INTO plt_account.vs_department (department, pid, status, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('測試用部門', 0, 1, 1, 'admin', DEFAULT, null, null, DEFAULT);
    INSERT INTO plt_account.vs_department (department, pid, status, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('刪除用部門', 0, 1, 1, 'admin', DEFAULT, null, null, DEFAULT);
    INSERT INTO plt_account.vs_role (role, status, num_of_total_admin, remark, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('測試用權限', 1, 0, null, 1, '超级管理员', DEFAULT, null, null, DEFAULT);
    INSERT INTO plt_account.vs_role (role, status, num_of_total_admin, remark, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('編輯用角色', 1, 0, null, 1, '超级管理员', DEFAULT, null, null, DEFAULT);
    INSERT INTO plt_account.vs_dept_role (dept_id, role_id, create_time, last_modified_time) VALUES (6, 6, DEFAULT, DEFAULT);
    INSERT INTO plt_account.vs_dept_role (dept_id, role_id, create_time, last_modified_time) VALUES (3, 6, DEFAULT, DEFAULT);
    ''')
