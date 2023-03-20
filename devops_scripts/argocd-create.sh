#!/bin/bash

run() {
  #) Create 
  ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app create $ARGOCD_APPNAME --insecure --project $ARGOCD_PROJECTNAME --repo $ARGOCD_REPO --revision $ARGOCD_REPO_REVISION --path $ARGOCD_REPO_DATA_PATH --dest-namespace $ARGOCD_DEST_NAMESPACE --dest-name $ARGOCD_DEST_NAME --sync-option $ARGOCD_SYNC_OPTION --grpc-web && \

  # Set 'automated' policy
  ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app set $ARGOCD_APPNAME --insecure --sync-policy $ARGOCD_SYNC_POLICY_AUTOMATED --grpc-web && \

  # Set 'automatic' prune
  ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app set $ARGOCD_APPNAME --insecure --auto-prune --grpc-web && \

  # Set 'self-heal' event
  ARGOCD_AUTH_TOKEN=$ARGOCD_TOKEN argocd app set $ARGOCD_APPNAME --insecure --self-heal

  echo "###### ArgoCD create '$ARGOCD_APPNAME' project ######"
}

run
