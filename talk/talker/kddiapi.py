#!/usr/bin/python
#coding:UTF-8
import requests, json
from datetime import datetime,timedelta
import csv

def weather():
    now=datetime.now()
    before=now+timedelta(hours=-1)
    url = "http://logger.m2m-cloud-std.kddi.ne.jp/v1.0/data/regular"
    method = "POST"
    obj = {
        "terminals" :
           [ {
        "terminal_id" : "410",
        "no" : [2,3,4,5,6,7,8,9,14]
            }],
       "from" : "{0:%Y%m%d%H%M%S}".format(before),
        "to" : "{0:%Y%m%d%H%M%S}".format(now)
    }
    json_data = json.dumps(obj).encode("utf-8")
    headers = {"Host":"logger.m2m-cloud-std.kddi.ne.jp",
              "Authorization":"Bearer W2DEAhjNvxlvwVlM-sIYmsyHYsfrCHgPi" ,
    "Content-Type" : "application/json",
    "Accept":"text/csv"}

    r = requests.post(url=url, data=json_data, headers=headers)
    print(r)
    data=[]
    kddi=[]
    data=r.text
    w=data.splitlines()
    for i in range(len(w)):
        kddi.append(str(w[i]).split(','))
    del kddi[0]
    print(kddi)
    for i in range(len(kddi)):
        del kddi[i][0:2]
        print(["日時"+","+"湿度"+","+"温度"+","+"明るさ"+","+"紫外線"+","+"気圧"+","+"音量"+","+"不快指数"+","+"熱中症危険度"+","+"CO2濃度"])
        print(kddi[i])
    
    
    
