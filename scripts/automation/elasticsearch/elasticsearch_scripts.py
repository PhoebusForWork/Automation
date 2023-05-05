# -*- coding: utf-8 -*-
from utils.database_utils import ElasticsearchTool
import json


def printJson(func):
    print(json.dumps(func, sort_keys=True, indent=4, separators=(',', ':')))


test = ElasticsearchTool()
abc ={"_score":1,"_class":"com.galaxy.storage.elasticsearch.po.AdminActionLogPo","trace_id":"95fdee8be806356a233d7144e2b3b5ce","account":"superAdmin","account_id":1,"department":"測試部","department_id":3,"role":"超级管理员","http_method":"GET","headers":{"x-request-id":"728655fc-c970-9739-80e3-521560be75a3","content-length":"2","x-b3-parentspanid":"233d7144e2b3b5ce","os-type":"0","x-forwarded-proto":"https","x-b3-sampled":"1","sign":"ODMwYzA4NmE5YmFjYTNhOTZiNzIzZjkyMzk2NzExYWM=","device-id":"3263782594","version":"1.0","accept":"application/json, text/plain, */*","token":"a52ce9bb-90e3-48a6-afd6-e509cb3b1544","x-envoy-attempt-count":"1","x-envoy-external-address":"35.194.237.247","x-b3-traceid":"95fdee8be806356a233d7144e2b3b5ce","x-b3-spanid":"54666a7fada6cb11","x-forwarded-client-cert":"By=spiffe://cluster.local/ns/app/sa/default;Hash=5862e73a2a816785a3bca476b421e2dbf0964f6b5305c9e9077bf52ff11f0553;Subject=\"\";URI=spiffe://cluster.local/ns/istio-system/sa/istio-ingressgateway-service-account","host":"api30-qa.prj300.xyz","content-type":"application/json","accept-encoding":"identity","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","timestamp":"1679393000"},"request_parameters":{},"response_status":200,"business_type":"SELECT","action_log_content_title":"節點列表","plt_code":"vs","gateway_controller_name":"com.galaxy.pltgateway.controller.account.v1.DepartmentController.listDepartment","ip":"35.194.237.247","log_time":"2023-03-21T10:03:20.385Z"};

t = test.add_data(index='vs_basics_admin_action_log', doc_type='_doc', json_data=abc)
printJson(t)
