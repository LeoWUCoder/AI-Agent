# for i in range(1, 10):# 外层循环控制行数，从1到9
#     # range(start（起始，默认0）, end（结束，必须指定）, step（步长，默认1）)
#     for j in range(1, i + 1):
#         print(f"{j}*{i}={i * j}", end="\t")
#     print("\n")# print()函数用于输出内容，默认情况下会在输出内容后添加一个换行符

#打印1到9之间的奇数,练习continue
#方法一
for i in range(1, 10, 2):
    print(i)

#方法二
for i in range(1, 10):
    if i % 2 == 1:
        print(i)

# 求0-9每个数自己幂自己的加和，如果大于10000000则循环终止。练习break
total = 0
for i in range(10):
    total += i ** i# i ** i表示i的i次幂，即0的0次幂为1，1的1次幂为1，2的2次幂为4，3的3次幂为27，4的4次幂为256，5的5次幂为3125，6的6次幂为46656，7的7次幂为823543，8的8次幂为16777216，9的9次幂为387420489。
    if total > 10000000:
        break
print(f"总和为: {total}")

