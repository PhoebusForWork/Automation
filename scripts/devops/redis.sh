#!/bin/bash

run() {
  FIND_MASTER=$(redis-cli -h $1 -p $REDIS_SENTINEL_PORT -a $2 --no-auth-warning sentinel masters | awk 'NR == 4')
  
  echo "Find redis master: $FIND_MASTER"
  echo "All keys" $(redis-cli -h $FIND_MASTER -p $REDIS_CLIENT_PORT -a $2 --no-auth-warning KEYS "*") && echo "It's running done"
  echo "Clear keys" && redis-cli -h $FIND_MASTER -p $REDIS_CLIENT_PORT -a $2 --no-auth-warning FLUSHALL && echo "It's running done"
  echo "Check keys" && $(redis-cli -h $FIND_MASTER -p $REDIS_CLIENT_PORT -a $2 --no-auth-warning KEYS "*") && echo "It's running done"
}

run $1 $2
