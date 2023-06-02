#!/bin/bash

SECONDS=0

check_health() {
  while true
  do
    
    DATE=$(date +'[%Y-%m-%d] %H:%M:%S')
    state=$(ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app get $ARGOCD_APPNAME --show-operation --insecure --server $ARGOCD_SERVER --grpc-web | grep "Health Status" | awk '{print $3}')

    # first if
    if [ $state != "Healthy" ]; then
      sleep 10 && echo "$DATE - Wait 10 second then continue detect, SECONDS: $SECONDS"

      # second if
      if [ $SECONDS -gt "300" ]; then
        echo "SECONDS >= 300 force restart service"
        for item in $(ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app get $ARGOCD_APPNAME --insecure --show-operation --grpc-web --server $ARGOCD_SERVER | grep "Progressing" | awk '{print $4}'); do
          ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app actions run $ARGOCD_APPNAME restart --resource-name $item --kind $ARGOCD_KIND --insecure --server $ARGOCD_SERVER --grpc-web && echo "Restart Pod '$item'"
        done;
        SECONDS=0
      fi

    else
      echo "All Pod is health state !" && break
    fi
  done
}

run() {
  echo "###### Detech Pod State ######"
  check_health
}

run
