#-*- comding:utf-8   -*-
import json
#消费清单，前后台时间对比
'''

import  datetime, requests
delta = [0,0]
count = [0,0]

#前台代码1
start = datetime.datetime.now()
for _ in range(5):
    url = "https://task-pre.renderbus.com/api/rendering/task/renderingTask/findConsumptionList"
    payload = "{\"userId\":-1,\"submitDate\":\"2019-6-4\",\"completedDate\":\"2019-6-11 23:59:59\",\"projectId\":-1,\"platform\":-1,\"timeStatus\":0,\"pageNum\":1,\"pageSize\":10}"
    headers = {
        'userkey': "6029b5276a1f9a39c14459323620dcea",
        'content-type': "application/json",
        'signature': "rayvision2017",
        'platform': "2",
        'channel': "2",
        'version': "1.0.0",
        'cache-control': "no-cache",
        'postman-token': "b5667a5a-0289-9f9e-b62c-b4d3700c4df5"}
    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    # print(response.text)
    count[0] += 1
delta[0] = (datetime.datetime.now() - start).total_seconds()

#后台代码2
start = datetime.datetime.now()
for _ in range(5):
    url = "https://admin-pre.renderbus.com/api/rendering/admin/front/pay/recharge/list/getConsumeList"
    payload = "{\"pageNum\":1,\"pageSize\":50,\"userId\":\"10005363\",\"queryRelateUser\":0,\"timeStatus\":\"0\",\"consumeAmount\":\"0\",\"platform\":\"\",\"feeType\":[]}"
    headers = {
        'languageflag': "0",
        'channel': "5",
        'content-type': "application/json",
        'x-auth-token': "25cf5807-0ede-42a9-a0cb-e1c1e59230ae",
        'signature': "rayvision2017",
        'platform': "2",
        'version': "1.0.0",
        'cache-control': "no-cache",
        'postman-token': "852606c2-977e-c94e-be88-965132338751"
    }
    response1 = requests.request("POST", url, data=payload, headers=headers, verify=False)
    # print(response1.text)
    count[1] += 1
delta[1] = (datetime.datetime.now() - start).total_seconds()

print(count)
print(delta)
print(delta[0] - delta[1] )

'''

#random随机数整数,前后都包
'''
import random
# ss = random.randint(0,10)
# print(ss)
#
# for i in range(10):
#     ss = random.randint(0, 10)  #randint没有步长
#     print(ss,end=' ')
#
# for i in range(10):
#     dd = random.randrange(0,5,2) #randrange有步长
#     print(dd,end=' ')

list = list((range(10)))
random.choice(list)   #choice随机抽取列表中元素，可迭代对象  range（10）都可以

random.shuffle(list)    #->None  shuffle就地打乱列表元素

random.sample(list,2)   #从一个列表中，随机取2个元素生成一个新的列表   返回等于[5,8] 是一个新的列表
'''

#求100内的素数


#计算杨辉三角前6行

























