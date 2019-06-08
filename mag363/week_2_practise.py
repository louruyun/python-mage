#-*- comding:utf-8   -*-


###第一个小练习，折半查找   22视频  50分钟
'''
a = int(input('请输入数字a:'))
b = int(input('请输入数字b:'))

def  pk (a):
    if a >= 1000:
        if a >= 10000:
            print('这是一个5位数')
        else:
            print('这是一个4位数')
    else:
        if a >= 100:
            print('这是一个3位数')
        elif a >= 10:
            print('这是一个2位数')
        else:
            print('这是一个1位数')

if  a > b :
    print(a)
    pk(a)
elif b > a :
    print(b)
    pk(b)
'''

#第二个小练习，  23视频  1分钟
## 给定一个正整数，判断该数的位数，依次打印每个位置的的数字
#
# '''
# x = input('请输入一个数字：')
# n = x.count('',1)
# print('这是一个%s位数'%n)
# w = 10 ** (n-1)
# x = int(x)
# print('从高位依次打印到个位')
# for i in range(n):
#     print(x//w)
#     x = x %  w     #去除对应位置
#     w = w // 10    #再除以10
# '''

#第三个小练习，24  正方形打印

# n = int(input(">>>"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or j==1 or i==n or j==n:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# n = int(input(">>>"))
# print('*'*n)
# a=n-2
# while a:
#     print('*'+' '*(n-2)+'*')
#     a-=1
# print('*'*n)

# n = 4
# for i in range(n):
#     if i % n == 0:
#         print('*' * n)
#     else:
#         print('*'+ ' '*  (n-2) + '*')


# n = int(input(">>>"))
# e = -(n // 2)
# for i in range(e , n + e):
#     if i == e  or i == n + e - 1:
#         print('*' * n)
#     else:
#         print('*' + ' ' * (n - 2) + '*')


#第四小练习  100内奇数和
# s = 0
# for i in range(2 ,101 , 2):
#         s += i
# print(s)

#阶乘 25
# n = 5
# s = 0
# value = 1
# for i in range(1,n+1):
#     value *= i
#     s += value
#     print(value,s)
# print(s)

# # 判断一个数是否素数
# x = 19777
# for i in range(2 ,x):
#     # print(x , i)
#     # print(x % i )
#     if x % i == 0:
#         print(x , 'is not a prime number')
#         break
# else:
#     print(x , 'is a prime mumber')

#打印九九乘法表

#打印菱形

#打印100以内的斐波那契数列

#求斐波那契数列第101项

#求10万内的所有素数

print(1
      %3)













