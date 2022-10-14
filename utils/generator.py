import random
import time
import string


class make():

    def name(namelen=8):
        name = ''.join(random.choice(string.ascii_letters + string.digits)
                       for _ in range(namelen))
        return name

    def mobile():
        mobile = "1{}{}".format(random.choice('589'), ''.join(
            random.choice(string.digits) for x in range(9)))
        return mobile

    def date(date='now'):
        if date == 'start':
            return time.strftime('%Y-%m-%d ', time.localtime()) + '00:00:00'

        elif date == 'end':
            return time.strftime('%Y-%m-%d ', time.localtime()) + '23:59:59'

        else:
            return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
