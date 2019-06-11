#-*- comding:utf-8   -*-

# 通过Python编程完成一个银行ATM机模拟系统，具备如下功能:
# (1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
# (2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
# (3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
# (4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
# (5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
# ps:实现方式不限
# name = input('')
# pswd = input('')
# user = open('')
#
# if  name in user :
#
#     while True:
#         if  name == 1 and pswd ==2 :
#             print('1.查看自己的账户余额')
#             print('2.转账')
#             a = input('请输入需要的操作')
#
#         else:
#             break
# else:
#     print('用户不存，请注册','yes','no')
#     ss = input('')
#     if ss == 'yes':
#
#         pass
#     else:
#         pass



import requests

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
    'postman-token': "ca9f7fe8-27fb-b54b-8943-e585a020a4d7"
    }
response = requests.request("POST", url, data=payload, headers=headers, verify=False)
# response = requests.post(url=url, data=payload, headers=headers, verify=False)

print(response.text)