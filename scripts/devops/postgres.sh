#!/bin/bash

CS=("cs_basics cs_fund cs_game cs_message cs_proxy cs_user cs_activity")
PLT=("plt_activity plt_account plt_basics plt_fund plt_game plt_message plt_proxy plt_user plt_risk plt_user wallet pay xxl_job")

# syntax(){
#   RECEIVE_ADDRESS=$1
#   RECEIVE_PASSWORD=$2
#   RECEIVRE_ITEM=$3

# echo "###### $RECEIVRE_ITEM ######" && echo "## Rebuild ##"
# # PGPASSWORD=$PG_MANAGE_PASSWORD psql -h $RECEIVE_ADDRESS -p $POSTGRES_PORT -U $PG_MANAGE_USER -d $RECEIVRE_ITEM  <<EOFSQL
# PGPASSWORD=$RECEIVE_PASSWORD psql -h $RECEIVE_ADDRESS -p $POSTGRES_PORT -U $PG_RD_USER -d $RECEIVRE_ITEM  <<EOFSQL
#     DROP SCHEMA $RECEIVRE_ITEM cascade;
#     CREATE SCHEMA $RECEIVRE_ITEM;
#     GRANT USAGE  ON SCHEMA $RECEIVRE_ITEM TO sit_sr;
#     GRANT CREATE ON SCHEMA $RECEIVRE_ITEM TO sit_sr;
#     GRANT USAGE ON SCHEMA $RECEIVRE_ITEM TO sit_app;
# EOFSQL

# echo "## Grant privilege ##"
# PGPASSWORD=$RECEIVE_PASSWORD psql -h $RECEIVE_ADDRESS -p $POSTGRES_PORT -U $PG_RD_USER -d $RECEIVRE_ITEM  <<EOFSQL
#     ALTER DEFAULT PRIVILEGES IN SCHEMA $RECEIVRE_ITEM GRANT SELECT, INSERT, UPDATE, DELETE  ON TABLES TO app_svc;
#     ALTER DEFAULT PRIVILEGES IN SCHEMA $RECEIVRE_ITEM GRANT SELECT, INSERT, UPDATE, DELETE  ON TABLES TO app_jr;
# EOFSQL
# }

plt_syntax(){
  RECEIVE_ADDRESS=$1
  RECEIVE_PASSWORD=$2
  RECEIVRE_ITEM=$3
  RECEIVE_JAVA_APP_PASSWORD=$4

echo "###### $RECEIVRE_ITEM ######" && echo "## Rebuild ##"
# PGPASSWORD=$PG_MANAGE_PASSWORD psql -h $RECEIVE_ADDRESS -p $POSTGRES_PORT -U $PG_MANAGE_USER -d $RECEIVRE_ITEM  <<EOFSQL
PGPASSWORD=$RECEIVE_PASSWORD psql -h $RECEIVE_ADDRESS -p $POSTGRES_PORT -U $PG_MANAGE_USER -d $RECEIVRE_ITEM  <<EOFSQL
    DROP SCHEMA $RECEIVRE_ITEM cascade;
    CREATE SCHEMA $RECEIVRE_ITEM;
    REVOKE CREATE ON SCHEMA public FROM PUBLIC;
    REVOKE ALL ON DATABASE $RECEIVRE_ITEM FROM PUBLIC;

    GRANT CONNECT ON DATABASE $RECEIVRE_ITEM TO plt_rd_role;
    GRANT USAGE ON SCHEMA $RECEIVRE_ITEM TO plt_rd_role;

    GRANT CONNECT ON DATABASE $RECEIVRE_ITEM TO plt_qa_role;
    GRANT USAGE ON SCHEMA $RECEIVRE_ITEM TO plt_qa_role;

    GRANT CONNECT ON DATABASE $RECEIVRE_ITEM TO plt_java_app_role;
    GRANT USAGE ON SCHEMA $RECEIVRE_ITEM TO plt_java_app_role;
    GRANT CREATE ON SCHEMA $RECEIVRE_ITEM TO plt_java_app_role;
EOFSQL

echo "## Grant privilege ##"

PGPASSWORD=$RECEIVE_JAVA_APP_PASSWORD psql -h $RECEIVE_ADDRESS -p $POSTGRES_PORT -U $PG_PLT_JAVA_APP_USER -d $RECEIVRE_ITEM  <<EOFSQL
    ALTER DEFAULT PRIVILEGES IN SCHEMA $RECEIVRE_ITEM GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO plt_java_app_role;
    ALTER DEFAULT PRIVILEGES IN SCHEMA $RECEIVRE_ITEM GRANT SELECT ON TABLES TO plt_rd_role;

    ALTER DEFAULT PRIVILEGES IN SCHEMA $RECEIVRE_ITEM GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO plt_qa_role;
EOFSQL
}

cs_syntax(){
  RECEIVE_ADDRESS=$1
  RECEIVE_PASSWORD=$2
  RECEIVRE_ITEM=$3
  RECEIVE_JAVA_APP_PASSWORD=$4

echo "###### $RECEIVRE_ITEM ######" && echo "## Rebuild ##"
# PGPASSWORD=$PG_MANAGE_PASSWORD psql -h $RECEIVE_ADDRESS -p $POSTGRES_PORT -U $PG_MANAGE_USER -d $RECEIVRE_ITEM  <<EOFSQL
PGPASSWORD=$RECEIVE_PASSWORD psql -h $RECEIVE_ADDRESS -p $POSTGRES_PORT -U $PG_MANAGE_USER -d $RECEIVRE_ITEM  <<EOFSQL
    DROP SCHEMA $RECEIVRE_ITEM cascade;
    CREATE SCHEMA $RECEIVRE_ITEM;
    REVOKE CREATE ON SCHEMA public FROM PUBLIC;
    REVOKE ALL ON DATABASE $RECEIVRE_ITEM FROM PUBLIC;

    GRANT CONNECT ON DATABASE $RECEIVRE_ITEM TO cs_rd_role;
    GRANT USAGE ON SCHEMA $RECEIVRE_ITEM TO cs_rd_role;

    GRANT CONNECT ON DATABASE $RECEIVRE_ITEM TO cs_qa_role;
    GRANT USAGE ON SCHEMA $RECEIVRE_ITEM TO cs_qa_role;

    GRANT CONNECT ON DATABASE $RECEIVRE_ITEM TO cs_java_app_role;
    GRANT USAGE ON SCHEMA $RECEIVRE_ITEM TO cs_java_app_role;
    GRANT CREATE ON SCHEMA $RECEIVRE_ITEM TO cs_java_app_role;
EOFSQL

echo "## Grant privilege ##"

PGPASSWORD=$RECEIVE_JAVA_APP_PASSWORD psql -h $RECEIVE_ADDRESS -p $POSTGRES_PORT -U $PG_CS_JAVA_APP_USER -d $RECEIVRE_ITEM  <<EOFSQL
    ALTER DEFAULT PRIVILEGES IN SCHEMA $RECEIVRE_ITEM GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO cs_java_app_role;
    ALTER DEFAULT PRIVILEGES IN SCHEMA $RECEIVRE_ITEM GRANT SELECT ON TABLES TO cs_rd_role;

    ALTER DEFAULT PRIVILEGES IN SCHEMA $RECEIVRE_ITEM GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO cs_qa_role;
EOFSQL
}

run() {
  ARRAY=()

  TEXT=$1
  PASS_ADDRESS=$2
  PASS_PASSWORD=$3
  JAVA_APP_PASSWORD=$4

  echo "ADDRESS: $PASS_ADDRESS"

  if [ "$TEXT" == "CS" ]; then
    ARRAY="${CS[@]}";

    for item in ${ARRAY[@]}; do
      cs_syntax $PASS_ADDRESS $PASS_PASSWORD $item $JAVA_APP_PASSWORD
    done

  elif [ "$TEXT" == "PLT" ]; then
    ARRAY="${PLT[@]}";

    for item in ${ARRAY[@]}; do
      plt_syntax $PASS_ADDRESS $PASS_PASSWORD $item $JAVA_APP_PASSWORD
    done

  else
    echo "ERROR ... exit" && exit 1
  fi

  # for item in ${ARRAY[@]}; do
  #   syntax $PASS_ADDRESS $PASS_PASSWORD $item
  # done
}

run $1 $2 $3 $4
