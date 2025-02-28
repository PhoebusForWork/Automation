from .database_utils import Postgresql

class UserWallet:
    @staticmethod
    def reset(balance="1000", user_id="29"):
        reset = Postgresql(database='wallet', platform="plt")
        sql = f"update wallet.ldpro_wallet set balance = {balance} ,freeze_balance=0 where user_id = {user_id} ;"
        reset.run_sql(sql=sql)

    @staticmethod
    def check_deposit(user_id="29", check_amount=100, channel="AWC"):
        check = Postgresql(database='wallet', platform='plt')
        game_transfer = f"select type,amount from wallet.ldpro_game_transfer where user_id = {user_id} order by create_time desc limit 1;"
        data = check.select_sql(game_transfer)
        type, amount = data[0][0], data[0][1]
        game_wallet = f"select channel_code,balance,freeze_balance from wallet.ldpro_game_wallet where user_id = {user_id} and channel_code = '{channel}';"
        data = check.select_sql(game_wallet)
        channel_code, balance, freeze_balance = data[0][0], data[0][1], data[0][2]
        try:
            assert type == "DEPOSIT"
            assert amount == check_amount
            assert channel_code == "AWC"
            assert check_amount in [balance, freeze_balance]
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def check_withdraw(user_id="29", check_amount=100, channel="AWC"):
        check = Postgresql(database='wallet', platform='plt')
        game_transfer = f"select type,amount from wallet.ldpro_game_transfer where user_id = {user_id} order by create_time desc limit 1;"
        data = check.select_sql(game_transfer)
        Type, amount = data[0][0], data[0][1]
        game_wallet = f"select balance,freeze_balance from wallet.ldpro_wallet where user_id = {user_id};"
        data = check.select_sql(game_wallet)
        balance, freeze_balance = data[0][0], data[0][1]
        try:
            assert Type == "WITHDRAW"
            assert amount == check_amount
            assert check_amount in [balance, freeze_balance]
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    print(UserWallet.check_deposit())
