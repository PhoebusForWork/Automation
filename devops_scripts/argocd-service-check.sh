#!/bin/bash

record_time=0

check_health() {
  while true
  do
    
    DATE=$(date +'[%Y-%m-%d] %H:%M:%S')
    state=$(ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app get $ARGOCD_APPNAME --show-operation --insecure --server $ARGOCD_SERVER | grep "Health Status" | awk '{print $3}')
    item=$()

    if [ $state != "Healthy" ]; then
      sleep 10 && echo "$DATE - Wait 10 second then continue detect, record_time: $record_time"
    elif [ $record_time == "300" ]; then
      record_time=0
      echo "record_time = 300 force restart service"
      for item in $(ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app get $ARGOCD_APPNAME --show-operation --grpc-web | grep "Progressing" | awk '{print $4}'); do
        ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app actions run $ARGOCD_APPNAME restart --resource-name $item --kind $ARGOCD_KIND --insecure --server $ARGOCD_SERVER && echo "Restart Pod '$item'"
      done;
    else
      echo "All Pod is health state !" && break
    fi

    ((record_time=record_time+1))

  done
}

run() {
  echo "###### Detech Pod State ######"
  check_health

}

run
