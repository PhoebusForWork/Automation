from utils.database_utils import Postgresql


def host_platform():
    # host_platform SQL
    host_platform = Postgresql(database='host_platform')
    host_platform.run_sql('''
        UPDATE host_platform.platform SET secret = '7E79731B19717750E618A4E0EFF248DA6AE334BB0706A31BC36A690A51F1A8E1' WHERE id = 1;
    ''')


def plt_account():
    # plt_account SQL
    plt_account = Postgresql(database='plt_account')
    plt_account.run_sql('''
        UPDATE plt_account.vs_admin SET last_login_time = '2023-03-06 04:01:21.203101 +00:00', last_login_device_id = '3263782594', last_login_ip = '61.220.72.61', last_modified_admin_id = 1, last_modified_admin = 'superAdmin' WHERE id = 2;
        INSERT INTO plt_account.vs_department (department, pid, status, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('測試用部門', 0, 1, 1, 'admin', DEFAULT, null, null, DEFAULT);
        INSERT INTO plt_account.vs_department (department, pid, status, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('刪除用部門', 0, 1, 1, 'admin', DEFAULT, null, null, DEFAULT);
        INSERT INTO plt_account.vs_role (role, status, num_of_total_admin, remark, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('測試用權限', 1, 0, null, 1, '超级管理员', DEFAULT, null, null, DEFAULT);
        INSERT INTO plt_account.vs_role (role, status, num_of_total_admin, remark, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('編輯用角色', 1, 0, null, 1, '超级管理员', DEFAULT, null, null, DEFAULT);
        INSERT INTO plt_account.vs_dept_role (dept_id, role_id, create_time, last_modified_time) VALUES (6, 6, DEFAULT, DEFAULT);
        INSERT INTO plt_account.vs_dept_role (dept_id, role_id, create_time, last_modified_time) VALUES (3, 6, DEFAULT, DEFAULT);
        ''')


def plt_game():
    plt_game = Postgresql(database='plt_game')
    plt_game.run_sql('''
    UPDATE plt_game.vs_game SET status = true::boolean
    ''')


def wallet():
    wallet = Postgresql(database='wallet')
    wallet.run_sql('''
    UPDATE wallet.vs_wallet SET balance = 100.0000::numeric(21,4) WHERE user_id in (1,2,3,4,5,6)
    ''')
