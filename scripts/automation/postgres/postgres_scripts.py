from utils.database_utils import Postgresql


def host_platform():
    # host_platform SQL
    host_platform = Postgresql(database='host_platform')
    host_platform.run_sql('''
        UPDATE host_platform.platform SET secret = '30BDCDFC4EC1A3164ADF6860741DA40C95A35D574AEEE9673A218ADA7738EAEC' WHERE id = 1;
        ''')


def plt_account():
    # plt_account SQL
    plt_account = Postgresql(database='plt_account')
    plt_account.run_sql('''
        UPDATE plt_account.ldpro_admin SET last_login_time = '2023-03-06 04:01:21.203101 +00:00', last_login_device_id = '3263782594', last_login_ip = '61.220.72.61', last_modified_admin_id = 1, last_modified_admin = 'superAdmin' WHERE id = 2;
        INSERT INTO plt_account.ldpro_department (department, pid, status, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('測試用部門', 0, 1, 1, 'admin', DEFAULT, null, null, DEFAULT);
        INSERT INTO plt_account.ldpro_department (department, pid, status, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('刪除用部門', 0, 1, 1, 'admin', DEFAULT, null, null, DEFAULT);
        INSERT INTO plt_account.ldpro_role (role, status, num_of_total_admin, remark, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('測試用權限', 1, 0, null, 1, '超级管理员', DEFAULT, null, null, DEFAULT);
        INSERT INTO plt_account.ldpro_role (role, status, num_of_total_admin, remark, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('編輯用角色', 1, 0, null, 1, '超级管理员', DEFAULT, null, null, DEFAULT);
        INSERT INTO plt_account.ldpro_dept_role (dept_id, role_id, create_time, last_modified_time) VALUES (3, 2, DEFAULT, DEFAULT);
        INSERT INTO plt_account.ldpro_dept_role (dept_id, role_id, create_time, last_modified_time) VALUES (4, 2, DEFAULT, DEFAULT);
        ''')

# 這邊先用語法處理 之後換成api新增
def plt_dept():
    # plt_dept SQL
    plt_dept = Postgresql(database='plt_account')
    plt_dept.run_sql('''
        INSERT INTO plt_account.ldpro_department (department, pid, status, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('資訊部門', 0, 1, 1, 'admin', '2022-07-14 09:56:56.862311 +00:00', 1, 'superAdmin', '2022-07-28 06:12:56.176618 +00:00');
        INSERT INTO plt_account.ldpro_department (department, pid, status, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('行銷部', 0, 1, 1, 'admin', '2022-07-14 09:56:56.862311 +00:00', null, null, '2022-07-14 09:56:56.862311 +00:00');
        INSERT INTO plt_account.ldpro_department (department, pid, status, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('測試部', 0, 1, 1, 'admin', '2022-07-14 09:56:56.862311 +00:00', null, null, '2022-07-14 09:56:56.862311 +00:00');
        INSERT INTO plt_account.ldpro_department (department, pid, status, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('風控部', 0, 1, 1, 'admin', '2022-07-14 09:56:56.862311 +00:00', null, null, '2022-07-14 09:56:56.862311 +00:00');
        INSERT INTO plt_account.ldpro_department (department, pid, status, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('客服部', 0, 1, 1, 'admin', '2022-07-14 09:56:56.862311 +00:00', 24, 'kkoma666', '2023-05-16 02:32:19.649329 +00:00');
        INSERT INTO plt_account.ldpro_role (role, status, num_of_total_admin, remark, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('行销员', 1, 1343, null, 1, '超级管理员', '2022-07-14 09:56:56.862311 +00:00', 6, 'elliot666', '2023-06-01 05:47:45.595784 +00:00');
        INSERT INTO plt_account.ldpro_role (role, status, num_of_total_admin, remark, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('测试员', 1, 77, null, 1, '超级管理员', '2022-07-14 09:56:56.862311 +00:00', 1526, 'hardy666', '2023-06-01 05:47:44.872405 +00:00');
        INSERT INTO plt_account.ldpro_role (role, status, num_of_total_admin, remark, creator_id, creator, create_time, last_modified_admin_id, last_modified_admin, last_modified_time) VALUES ('风控人员', 0, 0, null, 1, '超级管理员', '2022-07-14 09:56:56.862311 +00:00', 1671, 'kkoma', '2023-05-19 02:09:04.964657 +00:00');
        ''')


def plt_game():
    plt_game = Postgresql(database='plt_game')
    plt_game.run_sql('''
        UPDATE plt_game.ldpro_game SET status = true::boolean
        ''')


def wallet():
    wallet = Postgresql(database='wallet')
    wallet.run_sql('''
        UPDATE wallet.ldpro_wallet SET balance = 100.0000::numeric(21,4) WHERE user_id in (1,2,3,4,5,6)
        ''')

def edit_the_default_platform():
    edit_the_default_platform = Postgresql(database='plt_basics')
    edit_the_default_platform.run_sql('''
        UPDATE plt_basics.platform SET domains = 'api30-auto.prj300.xyz,admin-auto.prj300.xyz'::varchar(128) WHERE id = 1::integer;
        UPDATE plt_basics.platform_currency SET status = 'ENABLE'::varchar(16);
        ''')
