'''
通过Python编程完成一个银行ATM机模拟系统，具备如下功能:
(1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
(2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
(3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
(4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
(5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
'''
import  os



def register():
    '''注册用户，用户已存在提示存在，用户不存在的话新增用户，并且在用户密码数组中添加新的用户和密码'''
    global money
    global username
    username = input("请输入用户名：")
    with open("./UserInfo.txt", "r") as f:
        info_dict = eval(f.readline())
        # print(type(info_dict))
    if username in info_dict.keys():
        print("用户已存在，请重新输入！")
    else:
        phone_number = input("请输入电话号码：")
        password = input("请输入密码:")
        print("用户注册成功，赠送您5000元")
        money = 5000
        info_dict[username] = [password, money, phone_number]
        #
        print(str(info_dict), '已将新用户信息存储至data')
        with open("./UserInfo.txt", "w") as f:
            f.write(str(info_dict))

def login():
    '''登录功能,包括登录成功与登录输入账号密码超过3次退出程序'''
    global user_input_error_count
    global password_input_error_count
    global flag
    global username
    global info_dict

    while True:
        username = input('请输入您的用户名')
        with open("./UserInfo.txt", "r") as f:
            info_dict = eval(f.readline())
        if username not in info_dict.keys():
            print('用户名不存在，请检查后输入！')
            user_input_error_count = user_input_error_count + 1
            if user_input_error_count == 3:
                print('输入的用户名错误次数达到3次，退出系统')
                break
        else:
            while True:
                password = input('请输入您的密码')
                if info_dict[username][0] != password:
                    print('密码输入错误，请重新输入')
                    password_input_error_count = password_input_error_count +1
                    if password_input_error_count == 3 :
                        print('输入的密码错误次数达到3次，退出系统')
                        flag = True
                        exit()  #这里不要break退出循环，不然会继续提示输入用户名，直接用exit退出程序
                else:
                    print('登录成功！')
                    print('1:菜单界面')
                    login_choice = input("请输入对应序号选择相应的功能:")
                    if login_choice == "1":
                        menu()

                    else:
                        print('输入错误，请输入密码后重新登录')
                        break
        if flag == 'True':
            break

def menu():
    '''菜单功能，定义菜单功能，主要是用户余额与转出额的对比，余额的结余'''
    global money
    print('欢迎进入SOS银行管理系统，请输入序号对应的功能'.center(50, "*"))
    while True:
        print("1:查询余额\n" + "2:转账\n" + "3:取款\n" + "4:存款\n" + "5:退出当前菜单")
        choice = input("请输入您的选择")
        if choice == "1":
            print("用户{0}的余额为{1}元.".format(username, info_dict[username][1]))
        elif choice == "2":
            transferAmount = int(input("请输入您要转账的金额:"))
            if info_dict[username][1] < transferAmount:
                print("金额不足，请重新输入")

            else:
                money = info_dict[username][1] - transferAmount
                info_dict[username][1] = money
                print("转账成功，您的余额为{}".format(info_dict[username][1]))
        elif choice == "3":
            withdrawalAmount = int(input("请输入您要取款的金额:"))
            if info_dict[username][1] < withdrawalAmount:
                print("余额不足，请重新输入！")
            else:
                money = info_dict[username][1] - withdrawalAmount
                info_dict[username][1] = money
        elif choice == "4":
            depositAmount = int(input("请输入您要存款的金额:"))
            money = info_dict[username][1] +depositAmount
            info_dict[username][1] = money

        elif choice == "5":
            exit()

if __name__ == '__main__':

    user_input_error_count = 0  # 用户名输入错误次数
    password_input_error_count = 0  # 密码输入错误次数
    money = 0  # 余额
    print('欢迎进入SOS银行管理系统，请输入序号对应的功能'.center(50, "*"))
    print("1:登录验证\n", "2:用户注册\n", "3:退出系统")
    main_choice = input("请输入您的选择:")
    flag = "false"
    if main_choice == "1":
        login()
    elif main_choice == "2":
        register()
    elif main_choice == "3":
        os.system(exit(0))
    else:
        print("输入错误，退出系统")
        os.system(exit(1))









