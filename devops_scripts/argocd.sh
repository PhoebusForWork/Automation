#!/bin/bash

check_health() {
  while true
  do
    DATE=$(date +'[%Y-%m-%d] %H:%M:%S')
    state=$(ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app get automation-app --show-operation --insecure --server $ARGOCD_SERVER | grep "Health Status" | awk '{print $3}')
    if [ $state != "Healthy" ]; then
      sleep 10 && echo "$DATE - Wait 10 second then continue detect"
    else
      echo "All Pod is health state !" && break
    fi
  done
}

run() {
  # Step1
  for item in $(ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app actions list $ARGOCD_APPNAME --kind $ARGOCD_KIND --insecure --server $ARGOCD_SERVER | awk '!seen[$3]++ { print $3 }' | tail -n +2); do
     ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app actions run $ARGOCD_APPNAME restart --resource-name $item --kind $ARGOCD_KIND --insecure --server $ARGOCD_SERVER && echo "Restart Pod '$item'"
  done;

  # Step2
  echo "###### Detech Pod State ######"
  check_health
}

run
