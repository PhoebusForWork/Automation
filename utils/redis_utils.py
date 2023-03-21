# -*- coding: utf-8 -*-
import sys,os
sys.path.append(os.path.abspath('.'))
import redis
from redis.sentinel import Sentinel
from utils.data_utils import EnvReader


env = EnvReader()
plt_host = env.REDIS_PLT_HOST
cs_host = env.REDIS_CS_HOST
plt_port = env.REDIS_PLT_PORT
cs_port = env.REDIS_CS_PORT
plt_sentinel_list = env.REDIS_PLT_SENTINEL_LIST
cs_sentinel_list = env.REDIS_CS_SENTINEL_LIST
plt_password = env.REDIS_PLT_PASSWORD
cs_password = env.REDIS_CS_PASSWORD
plt_sentinel_password = env.REDIS_SENTINEL_PLT_PASSWORD
cs_sentinel_password = env.REDIS_SENTINEL_CS_PASSWORD


class Redis:
    def __init__(self, platform='plt', select=None):
        self.host = None
        self.port = None
        self.password = None
        if platform == 'plt':
            self.host = plt_host
            self.port = plt_port
            self.password = plt_password
        elif platform == 'cs':
            self.host = cs_host
            self.port = cs_port
            self.password = cs_password
        else:
            raise "Platform Error"
        self.conn = redis.Redis(
            host=self.host, password=self.password, port=self.port, db=select)

    def keys(self, keyword='*'):
        target = self.conn.keys(keyword)
        return target

    def set_value(self, key, value):
        target = self.conn.set(key, value)
        return target


class RedisSentinel:
    def __init__(self, platform='plt', name='redis-master', select=None):
        if platform == 'plt':
            self.sentinel_list = plt_sentinel_list
            self.sentinel_password = plt_sentinel_password
        elif platform == 'cs':
            self.sentinel_list = cs_sentinel_list
            self.sentinel_password = cs_sentinel_password
        else:
            raise "Platform Error"
        setting = {
            'sentinels': self.sentinel_list,
            'sentinel_kwargs': {'password': self.sentinel_password},
            "socket_timeout": 60,
            "password": self.sentinel_password,
            "db": select
        }
        self.sentinel = Sentinel(**setting)
        self.master = self.sentinel.master_for(service_name=name)

if __name__ == '__main__':
    sentinel = RedisSentinel(platform='plt', select=0)
    print(sentinel.master.keys('*'))
