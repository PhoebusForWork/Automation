from .data_base_handler import Postgresql


class User_wallet:
    @staticmethod
    def user_wallet_reset(balance="1000", user_id="29"):
        reset = Postgresql(database='wallet', platform="plt")
        sql = "update wallet.vs_wallet set balance = {} ,freeze_balance=0 where user_id = {} ;".format(
            balance, user_id)
        reset.run_sql(sql=sql)

    @staticmethod
    def user_wallet_deposit_check(user_id="29", check_amount=100, channel="AWC"):
        check = Postgresql(database='wallet', platform='plt')
        game_transfer = "select type,amount from wallet.vs_game_transfer where user_id = {} order by create_time desc limit 1;".format(
            user_id)
        data = check.select_sql(game_transfer)
        Type, amount = data[0][0], data[0][1]
        game_wallet = "select channel_code,balance,freeze_balance from wallet.vs_game_wallet where user_id = {};".format(
            user_id)
        data = check.select_sql(game_wallet)
        channel_code, balance, freeze_balance = data[0][0], data[0][1], data[0][2]
        # print(Type, amount, channel_code, balance, freeze_balance)
        try:
            assert Type == "DEPOSIT"
            assert amount == check_amount
            assert channel_code == "AWC"
            assert balance or freeze_balance == check_amount
            return True
        except:
            return False

    @staticmethod
    def user_wallet_withdraw_check(user_id="29", check_amount=100, channel="AWC"):
        check = Postgresql(database='wallet', platform='plt')
        game_transfer = "select type,amount from wallet.vs_game_transfer where user_id = {} order by create_time desc limit 1;".format(
            user_id)
        data = check.select_sql(game_transfer)
        Type, amount = data[0][0], data[0][1]
        game_wallet = "select balance,freeze_balance from wallet.vs_wallet where user_id = {};".format(
            user_id)
        data = check.select_sql(game_wallet)
        balance, freeze_balance = data[0][0], data[0][1]
        try:
            assert Type == "WITHDRAW"
            assert amount == check_amount
            assert balance or freeze_balance == check_amount
            return True
        except:
            return False


if __name__ == '__main__':
    print(User_wallet.user_wallet_deposit_check())
