#########################################################################
# File Name: influx2.py
# Author   : ATM006
# mail     : 18829897162@163.com
# Time: 2018年05月01日 星期二 10时40分17秒
#########################################################################
#!/usr/bin/python
#-*- coding:utf8 -*-
from influxdb import InfluxDBClient



json_body = [
    {
        "measurement": "stu",
        "tags": {
            "stuid": "s123"
        },
        #"time": "2017-03-12T22:00:00Z",
        "fields": {
            "score": 89
        }
    }
]




def showDBNames(client):
	result = client.query('show measurements;') 
	print("Result: {0}".format(result))



client = InfluxDBClient('localhost', 8086, 'root', '', 'IoT')
print(client.get_list_database()) 
showDBNames(client)

x = client.write_points(json_body)
print(x)
showDBNames(client)


#client.query("drop measurement students") # 删除表
#showDBNames(client)
