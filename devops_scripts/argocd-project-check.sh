#!/bin/bash

# In bash script "Non-Zero = Failure"

check_project() {
    DATE=$(date +'[%Y-%m-%d] %H:%M:%S')

    state=$(ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app list --grpc-web | grep $ARGOCD_APPNAME)
    
    # $? > 0 = true otherwise false
    # echo state: $? 

    if [ $? -eq 0 ]; then
      sleep 5 && echo "$DATE - Wait 5 second then continue detect"
    else
      echo "###### ArgoCD check '$ARGOCD_APPNAME' project already delete done ######" && break
    fi
}

run() {
  echo "###### Check '$ARGOCD_APPNAME' project exist ######"
  while true
  do
    check_project
  done
}

run
