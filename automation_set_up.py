# -*- coding: utf-8 -*-
import time
from scripts.automation.elasticsearch import elasticsearch_scripts
from scripts.automation.postgres import postgres_scripts
from scripts.automation.mongo import mongo_scripts
from scripts.automation.setup_api import platform, client_side
from utils.xxl_job_utils import XxlJobs


xxl = XxlJobs()
# ####################
#  postgres-總控模擬  #
# ####################
# setting預設的站點資料
postgres_scripts.edit_the_default_platform()
# 這邊要進行plt-basic的sync
xxl.sync_plt_basics_data()
wait_for_sync = 5
time.sleep(wait_for_sync)
xxl.sync_plt_basics_data(pltCode='mx')
time.sleep(wait_for_sync)
xxl.sync_plt_basics_data(pltCode='vt999')

# #############
#  API 預處理  #
# #############

platform.super_admin_initialize()
platform.create_dept_and_role()
platform.create_account()
platform.login_account()
platform.create_proxy_channel_Group()
platform.create_initialize_proxy_account()
platform.turn_on_the_game_to_test()
client_side.create_initial_user()
client_side.binding_mobile()

# #############
#   postgres  #
# #############

postgres_scripts.host_platform()
postgres_scripts.plt_account()
postgres_scripts.plt_game()
postgres_scripts.plt_proxy()
postgres_scripts.plt_fund()
postgres_scripts.cs_game()
postgres_scripts.wallet()
platform.sync_relation_manage()
xxl.get_game_orders()
xxl.sync_activity_category()
postgres_scripts.plt_user()
postgres_scripts.cs_user()

# #############
#    mongo    #
# #############

mongo_scripts.setup_lock_status_user()

# #############
#  elasticsearch  #
# #############
# elasticsearch_scripts.plt_action_log()
