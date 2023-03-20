#!/bin/bash

check_project() {
    echo "###### Check 'automation-app' project exist ######"

    DATE=$(date +'[%Y-%m-%d] %H:%M:%S')

    state=$(ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app list --grpc-web | grep $ARGOCD_APPNAME)
    
    # $? > 0 = true otherwise false
    # echo state: $? 

    if [ $? -eq 0 ]; then
      sleep 5 && echo "$DATE - Wait 5 second then continue detect exist"
    else
      echo "###### ArgoCD check 'automation-app' project already delete done ######" && break
    fi
}


run() {
  ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app delete $ARGOCD_APPNAME -y --grpc-web

  while true
  do
    check_project
  done

  echo "###### ArgoCD delete '$ARGOCD_APPNAME' project ######"
}

run
