# -*- coding: utf-8 -*-
import redis


class Redis:
    def __init__(self, host='127.0.0.1', platform='plt', password='8LvIV2Df8l', select=None):
        port = None
        if platform == 'plt':
            port = '6379'
            password = '8LvIV2Df8l'
        elif platform == 'cs':
            port = '6380'
            password = 'mG3G9o5jSp'
        else:
            raise "Platform Error"
        self.conn = redis.Redis(
            host=host, password=password, port=port, db=select)

    def keys(self, keyword='*'):
        target = self.conn.keys(keyword)
        return target

    def set_value(self, key, value):
        target = self.conn.set(key, value)
        return target


if __name__ == '__main__':
    set_result = Redis(platform='plt', select=3)
    set_result.conn.hset(name='MOCK::AWC', key='recheckResult', value='"UNKNOWN"'
                         )
    target = set_result.conn.hget(name='MOCK::AWC', key='recheckResult')
    print(target)
