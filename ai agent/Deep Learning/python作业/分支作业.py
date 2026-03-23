# 1）接收控制台输入的薪水值，如果高于15000，就投递简历
# 获取老板提供的薪水
salary = int(input("请输入您提供的薪水"))
# input()函数用于从控制台获取用户输入，返回一个字符串。这里使用int()函数将输入的字符串转换为整数，以便进行数值比较。
#input()语法：input(prompt)
if salary >= 15000 :
    print("薪水不错,考虑进一步沟通")
print("程序执行结束")

# 4）从键盘上获取输入的数字，判断奇偶性，分别输出
num=int(input("请输入数字："))
if num%2==0:
    print("偶数")
else:
    print("奇数")

# 5）模拟用户登录验证，获取键盘上的输入，如果用户名admin,密码是123，提示登录成功，否则提示登录失败
usename=input("请输入用户名：")
userpassword=input("请输入密码：")
if usename=="admin" and userpassword=="123":
    print("登录成功")

# # 8）从键盘上输入一个时间，输出它的下一秒时间
# # 获取用户在键盘上输入的时间
# hour = int(input("请输入小时(0~23)"))
# minute = int(input("请输入分钟(0~59)"))
# second = int(input("请输入秒(0~59)"))
# print("当前时间为:%d:%d:%d" %(hour,minute,second))

# #计算下一秒
# second += 1
# # 修正时间
# if second == 60 :
#     # 如果是60秒了,秒置为0,分钟+1
#     second = 0
#     minute += 1
#     # 如果分钟加1后变为60,分钟置0,小时+1
#     if minute == 60 :
#         minute = 0
#         hour += 1
#         # 如果小时加1后变为24了,小时置0
#         if hour == 24 : 
#             hour = 0

# print("当前时间的下一秒为:%d:%d:%d" %(hour,minute,second))

# 9）遍历出1~100之间所有的数,将能被3整除的数打印出来,每行打印5个
array=[]
for num in range(1,101):
    array[num-1]=num
    print(array[num-1])
i=0
while array[i]%3==0:
    print(array[i])
    i+=1

