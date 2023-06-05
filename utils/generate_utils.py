import random
import time
import string
import base64
import hashlib
import datetime
from dateutil.relativedelta import relativedelta

class Make:

    @staticmethod
    def name(namelen=8):
        if namelen < 2:
            raise ValueError("字串長度必須大於或等於2")
        # 選擇一個隨機英文字母作為開頭
        first_letter = random.choice(string.ascii_letters)
        # 在剩餘的字元中隨機選擇數字和英文字母
        remaining_chars = [random.choice(string.ascii_letters + string.digits) for _ in range(namelen - 1)]
        # 確保至少有一個數字存在
        if not any(char.isdigit() for char in remaining_chars):
            index_to_replace = random.randrange(len(remaining_chars))
            remaining_chars[index_to_replace] = random.choice(string.digits)
        # 生成最終字串
        result_string = first_letter + ''.join(remaining_chars)
        return result_string

    @staticmethod
    def mobile():
        return "1{}{}".format(
            random.choice('589'),
            ''.join(random.choice(string.digits) for x in range(9)))

    @staticmethod
    def date(status):
        if status == 'start':
            return time.strftime('%Y-%m-%d', time.localtime()) + 'T00:00:00Z'

        elif status == 'end':
            return time.strftime('%Y-%m-%dT', time.localtime()) + '23:59:59Z'

        else:
            return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    @staticmethod
    def generate_custom_date(months=0, weeks=0, days=0):
        # 獲取當前日期時間
        now = datetime.datetime.now()
        # 進行日期計算
        target_date = now + relativedelta(months=months, weeks=weeks, days=days)
        # 將小時、分鐘和秒設定為 00:00:00
        target_date = target_date.replace(hour=0, minute=0, second=0)
        # 格式化日期為指定格式
        formatted_date = target_date.strftime('%Y-%m-%dT%H:%M:%SZ')
        return formatted_date

    @staticmethod
    def sign(os_type, SECRET, device_id=3263782594) -> dict:
        timestamp = str(int(datetime.datetime.now().timestamp()))
        pre_sign = f'device-id={device_id}&os-type={os_type}&timestamp={timestamp}{SECRET}'
        md5_sign = hashlib.md5(pre_sign.encode()).digest()
        after_sign = base64.b64encode(md5_sign).decode()
        return {"timestamp": timestamp, "sign": after_sign}
