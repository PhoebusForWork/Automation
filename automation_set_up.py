# -*- coding: utf-8 -*-
import time
from scripts.automation.postgres import postgres_scripts
from scripts.automation.mongo import mongo_scripts
from scripts.automation.setup_api import contorl, platform, client_side


# #############
#  API 預處理  #
# #############
contorl.create_platform_and_sync()
wait_for_sync = 5
time.sleep(wait_for_sync)
platform.super_admin_initialize_and_create_admin()
platform.login_account()
platform.turn_on_the_game_to_test()
client_side.create_initial_user()

# #############
#  postgres  #
# #############

postgres_scripts.host_platform()
postgres_scripts.plt_account()
postgres_scripts.plt_game()
postgres_scripts.wallet()

# #############
#    mongo   #
# #############

mongo_scripts.setup_lock_status_user()
