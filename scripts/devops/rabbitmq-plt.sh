#!/bin/bash

run() {
  echo "Connect: " $1

  ################
  # QUEUES
  ################
  echo " ###### All queues ######" && curl -X GET -u "$RABBITMQ_PLT_USER:$RABBITMQ_PLT_PASSWORD" --url http://$1:$RABBITMQ_PORT/api/queues/%2f/ | jq '.[].name' && echo "It's running done"
  echo "Delete queues"
  for i in $(curl -X GET -u $RABBITMQ_PLT_USER:$RABBITMQ_PLT_PASSWORD --url http://$1:$RABBITMQ_PORT/api/queues/%2f/ | jq -r '.[].name');
  do
    curl -X DELETE -u $RABBITMQ_PLT_USER:$RABBITMQ_PLT_PASSWORD --url http://$1:$RABBITMQ_PORT/api/queues/%2f/$i >/dev/null 2>&1
  done;
  echo "It's running done"
  echo "Check queues" && curl -X GET -u $RABBITMQ_PLT_USER:$RABBITMQ_PLT_PASSWORD --url http://$1:$RABBITMQ_PORT/api/queues/%2f/ | jq '.[].name' && echo "It's running done"

  # ################
  # # EXCHANGE
  # ################
  echo "###### All exchanges ######" && curl -X GET -u $RABBITMQ_PLT_USER:$RABBITMQ_PLT_PASSWORD --url http://$1:$RABBITMQ_PORT/api/exchanges/%2f/ | jq '.[].name' && echo "It's running done"

  echo "Delete exchanges"
  for i in $(curl -X GET -u $RABBITMQ_PLT_USER:$RABBITMQ_PLT_PASSWORD --url http://$1:$RABBITMQ_PORT/api/exchanges/%2f/ | jq -r '.[].name');
  do
    curl -X DELETE -u $RABBITMQ_PLT_USER:$RABBITMQ_PLT_PASSWORD --url http://$1:$RABBITMQ_PORT/api/exchanges/%2f/$i >/dev/null 2>&1
  done;
  echo "It's running done"
  echo "Check exchanges" && curl -X GET -u $RABBITMQ_PLT_USER:$RABBITMQ_PLT_PASSWORD --url http://$1:$RABBITMQ_PORT/api/exchanges/%2f/ | jq '.[].name' && echo "It's running done"
}

run $1
