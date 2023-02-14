#!/bin/bash

run() {
  echo "All index" && curl -u $ES_USER:$ES_PASSWORD -X GET $ES_FQDN:$ES_PORT/_cat/indices?pretty && echo "It's running done"

  echo "Delete incldue '$1' index" && curl -u $ES_USER:$ES_PASSWORD -X DELETE "$ES_FQDN:$ES_PORT/$1?pretty" && echo "It's running done"

  echo "Check index" && curl -u $ES_USER:$ES_PASSWORD -X GET $ES_FQDN:$ES_PORT/_cat/indices?pretty && echo "It's running done"
}

run $1
