#!/bin/bash

CS=("cs_basics cs_fund cs_game cs_message cs_proxy cs_user")
PLT=("host_platform plt_account plt_basics plt_fund plt_game plt_message plt_proxy plt_user plt-risk wallet")

syntax(){
  RECEIVE_ADDRESS=$1
  RECEIVE_PASSWORD=$2
  RECEIVRE_ITEM=$3

echo "###### $RECEIVRE_ITEM ######" && echo "## Rebuild ##"
# PGPASSWORD=$PG_MANAGE_PASSWORD psql -h $RECEIVE_ADDRESS -p $POSTGRES_PORT -U $PG_MANAGE_USER -d $RECEIVRE_ITEM  <<EOFSQL
PGPASSWORD=$RECEIVE_PASSWORD psql -h $RECEIVE_ADDRESS -p $POSTGRES_PORT -U $PG_RD_USER -d $RECEIVRE_ITEM  <<EOFSQL
    DROP SCHEMA $RECEIVRE_ITEM cascade;
    CREATE SCHEMA $RECEIVRE_ITEM;
    GRANT USAGE  ON SCHEMA $RECEIVRE_ITEM TO sit_sr;
    GRANT CREATE ON SCHEMA $RECEIVRE_ITEM TO sit_sr;
    GRANT USAGE ON SCHEMA $RECEIVRE_ITEM TO sit_app;
EOFSQL

echo "## Grant privilege ##"
PGPASSWORD=$RECEIVE_PASSWORD psql -h $RECEIVE_ADDRESS -p $POSTGRES_PORT -U $PG_RD_USER -d $RECEIVRE_ITEM  <<EOFSQL
    ALTER DEFAULT PRIVILEGES IN SCHEMA $RECEIVRE_ITEM GRANT SELECT, INSERT, UPDATE, DELETE  ON TABLES TO app_svc;
    ALTER DEFAULT PRIVILEGES IN SCHEMA $RECEIVRE_ITEM GRANT SELECT, INSERT, UPDATE, DELETE  ON TABLES TO app_jr;
EOFSQL
}

run() {
  ARRAY=()

  TEXT=$1
  PASS_ADDRESS=$2
  PASS_PASSWORD=$3

  echo "ADDRESS: $PASS_ADDRESS"

  if [ "$TEXT" == "CS" ]; then
    ARRAY="${CS[@]}";
  elif [ "$TEXT" == "PLT" ]; then
    ARRAY="${PLT[@]}";
  else
    echo "ERROR ... exit" && exit 1
  fi

  for item in ${ARRAY[@]}; do
    syntax $PASS_ADDRESS $PASS_PASSWORD $item
  done
}

run $1 $2 $3
