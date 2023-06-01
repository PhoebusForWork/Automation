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
        INSERT INTO plt_account.ldpro_dept_role (dept_id, role_id, create_time, last_modified_time) VALUES (6, 6, DEFAULT, DEFAULT);
        INSERT INTO plt_account.ldpro_dept_role (dept_id, role_id, create_time, last_modified_time) VALUES (3, 6, DEFAULT, DEFAULT);
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
        UPDATE plt_basics.platform SET domains = 'api30-auto.prj300.xyz'::varchar(128) WHERE id = 1::integer;
        UPDATE plt_basics.platform_currency SET status = 'ENABLE'::varchar(16);
        ''')


def cs_message():
    cs_message = Postgresql(database='cs_message', platform='cs')
    cs_message.run_sql('''
        insert into cs_message.ldpro_third_party_manage (id, name, type, weighting, ext, is_enabled, created_time, last_modified_id, last_modified_name, last_modified_time, language)
        values
        (3, 'AliCloud', 'EMAIL', 100, '{"alias": "乐动体育", "endpoint": "dm.ap-southeast-1.aliyuncs.com", "accessKeyId": "LTAI4GH9TbcyRjXhT4U8QnR8", "accountName": "support@mail.ld65.pro", "accessKeySecret": "zA9VIxRvLAlnM7Tx3T62nIR1dMBAVg"}', true, '2022-07-19 08:11:41.620049 +00:00', null, null, null, 'NONE'),
        (5, 'MaiXunTongInternational', 'SMS', 100, '{"url": "http://43.153.82.227:9511/api/send-sms-single", "spId": "495347", "password": "1d1b7213"}', true, '2022-07-19 08:11:41.524691 +00:00', 1, 'superAdmin', '2023-03-27 09:35:34.922353 +00:00', 'NONE'),
        (4, 'YunPian', 'VOICE', 2, '{"apiKey": "69d0501dc1f92c7d5d639588f088b2c4", "yp.version": "v2", "yp.sms.host": "https://kp.prj300.xyz/sms.yunpian.com", "yp.tpl.host": "https://kp.prj300.xyz/sms.yunpian.com", "http.charset": "utf-8", "yp.call.host": "https://kp.prj300.xyz/call.yunpian.com", "yp.flow.host": "https://kp.prj300.xyz/flow.yunpian.com", "yp.sign.host": "https://kp.prj300.xyz/sms.yunpian.com", "yp.user.host": "https://kp.prj300.xyz/sms.yunpian.com", "yp.voice.host": "https://kp.prj300.xyz/voice.yunpian.com", "http.so.timeout": "30000", "http.conn.timeout": "10000", "yp.short_url.host": "https://kp.prj300.xyz/sms.yunpian.com", "http.conn.maxtotal": "200", "http.conn.maxperroute": "50"}', true, '2022-07-19 08:11:41.659012 +00:00', 3, 'alan', '2023-05-12 02:52:44.895051 +00:00', 'NONE'),
        (1, 'MaiXunTong', 'SMS', 101, '{"pwd": "Mxt8a0t1x6M1A1", "url": "https://www.weiwebs.cn/msg/HttpSendSM", "account": "MXT801611"}', true, '2022-07-19 08:11:41.524691 +00:00', 1, 'superAdmin', '2023-05-12 06:11:06.889468 +00:00', 'NONE'),
        (12, '阿里云-联卓-天津市巴鑫商贸', 'BANK', 1, '{"url": "https://jmbank.market.alicloudapi.com/bankcard/validate", "password": "bf9498bb597d4f1e9facb4834e4afbc2", "username": "2fyoiNoeqLlLNfS25lxUiMb9l6tIz5oY"}', true, '2023-05-16 05:57:18.094000 +00:00', 1, 'superAdmin', '2023-05-16 06:08:09.702705 +00:00', 'ZH'),
        (17, 'Livechat-ZH', 'CUSTOMER', 22, '{"url": "https://secure.livechatinc.com/licence/14077215/v2/open_chat.cgi"}', false, '2023-05-18 07:36:48.946151 +00:00', 25, 'ping666', '2023-05-18 08:42:21.235554 +00:00', 'ZH'),
        (21, 'SmartCustomerSystem-ZH', 'CUSTOMER', 33, '{"h5Url": "https://icstest.aicspro.com/h5sdk/#/loading", "appKey": "b6ChSz7G", "priKey": "MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBANPMumNKiSXn2LvkHJxn6Ud4iTEPxqpCjD2BUjLjg6f1b9WgvA7LFUuch2i5Woegw/jq9UblFixuoIAmHJenlAE/clEAgjlBVFXT0Pxl0bGIl2tK0Kidm5KFMREwg7NuPBljbw2a2VpunrGQv2GcPyRfRjvkLc80DbVKE3BJwg+jAgMBAAECgYEAv6p2RaJO6IGd7bJpfdS/E5FtvXtEUhF07bfY1fpzywvdz5nsdQqs08br9wY9eZ0vm1Os8SIg5caa8j0LBOZ+lNjr0H2dPx2/tTFkXh9xHKEdwjQt9dN5AubRPKYQWpUOgtpMOyflRS0QLISa07hX1h4tlJZCxD0epsEjBGBa2iECQQDu528FNKBjJyj4jWg/cGyGH3n/e4f59TWjQmMHpJDuR+taHvkoPxo9MI/RyRnO0ZwybMkZTr2I1w3qDPKTdAuTAkEA4vTCzTMQjDyW+2pTbuEXEn1iYhNZFaVGAFvhyue9NxT21mdEKpELFeFx+Uoql4DinoWisHUAU1Reify84gEVsQJAdE/C0nL7vypanSAjZ/dxLp92gvb+jahfc9unYRoy4X+sStUXkwud17qj2owg/3s3o6kpAyQ9zLh+8rtZAocV9wJBAJgc/nd0E1I6xeMKd5MoUEN3QDqFxz6HwGw7KRHK0noZlftLyVdSUYC/0pkICZXzr3AaF1l3gdlYAekwORStL3ECQHKeVUL8mZ4klVMezmzbSsyEAoKuaHms6QWzPjFD+etgr4UolKIg/skErtU82WKaIm6gZn/33AKWsI1Dhz31UiM=", "webUrl": "https://icstest.aicspro.com/sdk/#/loading", "appSecret": "1444447d809cda3ec4ffe46af4a8285301d00862", "getUserTokenApiUrl": "https://icstest.aicspro.com/apis/api/user/v1/login", "getAccessTokenApiUrl": "https://icstest.aicspro.com/apis/api/auth/v1/getAccessToken"}', false, '2023-05-18 08:15:38.234100 +00:00', 25, 'ping666', '2023-05-18 08:42:24.573015 +00:00', 'ZH'),
        (2, 'IshuMei', 'CAPTCHA', 1, '{"apiUrl": "http://captcha-s.fengkongcloud.com/ca/v1/sverify", "accessKey": "by5AZitj1wc1H2anRHXU"}', true, '2022-07-19 08:11:41.574779 +00:00', 1, 'superAdmin', '2023-05-18 08:50:45.769018 +00:00', 'ZH'),
        (19, 'Livechat-EN', 'CUSTOMER', 22, '{"url": "https://secure.livechatinc.com/licence/14077215/v2/open_chat.cgi"}', true, '2023-05-18 07:37:36.479127 +00:00', 25, 'ping666', '2023-05-19 07:57:03.335012 +00:00', 'EN'),
        (11, '阿里云-聚美-queenp', 'BANK', 1, '{"url": "https://jmbank.market.alicloudapi.com/bankcard/validate", "password": "bf9498bb597d4f1e9facb4834e4afbc2", "username": "2fyoiNoeqLlLNfS25lxUiMb9l6tIz5oY"}', false, '2023-05-16 05:57:18.094000 +00:00', 25, 'ping666', '2023-05-18 06:57:02.091009 +00:00', 'ZH'),
        (20, 'SmartCustomerSystem-EN', 'CUSTOMER', 234, '{"h5Url": "https://icstest.aicspro.com/h5sdk/#/loading", "appKey": "b6ChSz7G", "priKey": "MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBANPMumNKiSXn2LvkHJxn6Ud4iTEPxqpCjD2BUjLjg6f1b9WgvA7LFUuch2i5Woegw/jq9UblFixuoIAmHJenlAE/clEAgjlBVFXT0Pxl0bGIl2tK0Kidm5KFMREwg7NuPBljbw2a2VpunrGQv2GcPyRfRjvkLc80DbVKE3BJwg+jAgMBAAECgYEAv6p2RaJO6IGd7bJpfdS/E5FtvXtEUhF07bfY1fpzywvdz5nsdQqs08br9wY9eZ0vm1Os8SIg5caa8j0LBOZ+lNjr0H2dPx2/tTFkXh9xHKEdwjQt9dN5AubRPKYQWpUOgtpMOyflRS0QLISa07hX1h4tlJZCxD0epsEjBGBa2iECQQDu528FNKBjJyj4jWg/cGyGH3n/e4f59TWjQmMHpJDuR+taHvkoPxo9MI/RyRnO0ZwybMkZTr2I1w3qDPKTdAuTAkEA4vTCzTMQjDyW+2pTbuEXEn1iYhNZFaVGAFvhyue9NxT21mdEKpELFeFx+Uoql4DinoWisHUAU1Reify84gEVsQJAdE/C0nL7vypanSAjZ/dxLp92gvb+jahfc9unYRoy4X+sStUXkwud17qj2owg/3s3o6kpAyQ9zLh+8rtZAocV9wJBAJgc/nd0E1I6xeMKd5MoUEN3QDqFxz6HwGw7KRHK0noZlftLyVdSUYC/0pkICZXzr3AaF1l3gdlYAekwORStL3ECQHKeVUL8mZ4klVMezmzbSsyEAoKuaHms6QWzPjFD+etgr4UolKIg/skErtU82WKaIm6gZn/33AKWsI1Dhz31UiM=", "webUrl": "https://icstest.aicspro.com/sdk/#/loading", "appSecret": "1444447d809cda3ec4ffe46af4a8285301d00862", "getUserTokenApiUrl": "https://icstest.aicspro.com/apis/api/user/v1/login", "getAccessTokenApiUrl": "https://icstest.aicspro.com/apis/api/auth/v1/getAccessToken"}', false, '2023-05-18 07:37:38.485801 +00:00', 25, 'ping666', '2023-05-19 08:02:43.378985 +00:00', 'EN');
        insert into cs_message.ldpro_message_template (id, name, type, third_party_manage_name, content, is_enabled, created_time, last_modified_id, last_modified_name, last_modified_time)
        values
        (1, 'MaiXunTong', 'SMS', 'MaiXunTong', '【乐动科技】這是測試喔: ${code}', true, '2022-07-19 08:11:45.082426 +00:00', 3, 'alan', '2022-07-19 09:03:06.824647 +00:00'),
        (2, 'YunPian', 'VOICE', 'YunPian', 'this is test ${code}', true, '2022-07-11 03:56:52.270635 +00:00', 3, 'alan', '2022-07-18 10:34:31.191348 +00:00'),
        (3, 'MaiXunTongInternational', 'SMS', 'MaiXunTongInternational', '【乐动科技】這是測試喔: ${code}', true, '2022-07-19 08:11:45.082426 +00:00', 3, 'alan', '2022-07-19 09:03:06.824647 +00:00');
        ''')
