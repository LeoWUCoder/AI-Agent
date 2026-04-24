# 3）编写一个函数 multiply_list，它接收一个列表 numbers 作为参数，将列表中的元素相乘，并返回结果
def multiply_list(numbers):
    for i in range(len(numbers)):
        if i==0:
            result=numbers[i]
        else:
            resuilt=result*numbers[i]
    return result
# 标准答案
# def multiply_list(numbers):
#     result = 1
#     for num in numbers:
#         result *= num
#     return result

# 4）编写一个函数 is_prime，它接收一个正整数 n，并判断 n 是否为质数，如果是质数返回 True，否则返回 False。
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True



