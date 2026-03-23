# 题目1：1）给定一个列表 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，编写一个程序，将列表中所有的偶数元素删除
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(0, len(numbers)):
#     if numbers[i]%2 == 0:
#         del numbers[i]
#     else:
#         print(numbers[i])
# range(0, len(numbers)) 在循环开始前就计算好了范围，即 0 到 9（共10次循环）。
# 当循环进行到某个位置（例如删除了第一个偶数 2）时，列表长度变短了，后面的元素会自动向前移动填补空缺。
# 但是，你的循环变量 i 依然按照原来的计划递增。
# 结果：i 的值最终会超过缩短后的列表的最大索引，从而抛出 IndexError: list index out of range

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers[:]:# 使用切片创建一个列表的副本，这样在循环中修改原列表不会影响到循环的迭代过程。
    if i%2 == 0:
        numbers.remove(i)# remove()方法用于移除列表中某个值的第一个匹配项。这里使用remove()方法来删除列表中的偶数元素。
    else:
        print(i)

# 2）创建一个空列表 fruits，然后添加 "apple", "banana", "cherry", "date" 四个元素。
# 接着在列表的开始添加 "elderberry"，在 "cherry" 之前添加 "fig"，并将列表的最后一个元素替换为 "grape"。
fruits = []
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
fruits.append("date")
fruits.insert(0, "elderberry")# insert()方法用于在指定位置插入一个元素。这里使用insert()方法在列表的开始位置（索引0）前插入 "elderberry"。
cherry_index = fruits.index("cherry")# index()方法用于返回列表中第一个匹配项的索引位置。这里使用index()方法来找到 "cherry" 在列表中的索引位置，以便在该位置之前插入 "fig"。
fruits.insert(cherry_index, "fig")
fruits[-1] = "grape"# 使用索引 -1 来访问列表的最后一个元素，并将其替换为 "grape"。
print(fruits)

# 给定一个列表 prices = [10.5, 20.0, 15.75, 8.2, 12.0]，
# 编写一个程序，将列表中的元素都乘以 1.1（表示增加 10%），并将结果存储在一个新列表 new_prices 中。
prices = [10.5, 20.0, 15.75, 8.2, 12.0]
# new_prices=[price*1.1 for price in prices]
new_prices = []
for price in prices:
    price *= 1.1
    new_prices.append(price)
print(new_prices)
# 标准答案
# prices = [10.5, 20.0, 15.75, 8.2, 12.0]
# new_prices = []
# for price in prices:
#     new_price = round(price * 1.1,2) #保留2为小数
#     new_prices.append(new_price)

# 4）有两个列表 list1 = [1, 2, 3, 4, 5] 和 list2 = [6, 7, 8, 9, 10]，将它们合并为一个新列表 combined_list，并对 combined_list 进行降序排序
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
combined_list = list1 + list2# 使用加号运算符将两个列表合并成一个新列表。
combined_list.sort(reverse=True)# sort()方法用于对列表进行排序，reverse=True参数表示降序排序。
print(combined_list)

# 5）给定一个列表 strings = ["hello", "world", "python", "is", "fun"]，编写一个程序，将列表中的元素拼接成一个字符串，元素之间用空格分隔。
strings = ["hello", "world", "python", "is", "fun"] 
result = " ".join(strings)# join()方法用于将列表中的元素连接成一个字符串，参数是一个可迭代对象，这里使用空格作为分隔符。
# 例如，" ".join(strings) 会将列表中的元素连接成一个字符串 "hello world python is fun"，其中每个元素之间用一个空格分隔。
# " ".是分隔符字符串，join()方法会将列表中的每个元素转换为字符串，并使用空格作为分隔符将它们连接起来，最终返回一个新的字符串。
# 使用空格 " " 作为分隔符：

# " ".join(strings)
# # 结果: "Hello World Python"
# # 解释: Hello + [空格] + World + [空格] + Python

# 如果使用空字符串 ""（没有空格）：

# "".join(strings)
# # 结果: "HelloWorldPython"
# # 解释: 单词直接粘在一起，中间没有任何东西

# 如果使用逗号加空格 ", " 作为分隔符：

# ", ".join(strings)
# # 结果: "Hello, World, Python"
# # 解释: 中间变成了逗号和空格

print(result)
# join()方法的语法是：str.join(iterable)，
# 其中str是分隔符字符串，iterable是一个可迭代对象（如列表、元组等）。
# join()方法会将iterable中的每个元素转换为字符串，并使用str作为分隔符将它们连接起来，最终返回一个新的字符串。

# 6）给定一个字符串 sentence = "Hello, World!"，编写一个程序，将字符串中的所有小写字母转换为大写字母，并输出结果。
sentence = "Hello, World!"
sentence.upper()# upper()方法用于将字符串中的所有小写字母转换为大写字母，并返回一个新的字符串。
print(sentence.upper())

# 7）给定一个字符串 text = "Python is fun and powerful."，统计字符串中字母 n 出现的次数。
text = "Python is fun and powerful."
count=text.count('n')
print(f"字母 'n' 在字符串中出现了 {count} 次")

# 8）给定一个字符串 str1 = "apple,banana,cherry,date"，
# 将该字符串按照 , 分隔，存储在一个列表中，并将列表中的元素首字母大写，最后将修改后的列表元素用 - 连接成一个新的字符串。
str1 = "apple,banana,cherry,date"
list1=str1.split(',')# split()方法用于将字符串按照指定的分隔符分割成一个列表。这里使用逗号 ',' 作为分隔符。
capitalized_list = []
for s in list1:
    capitalized_list.append(s.capitalize())# capitalize()方法用于将字符串的首字母大写，其他字母小写。这里使用capitalize()方法将列表中的每个元素的首字母大写，并将修改后的元素添加到capitalized_list列表中。
new_str = '-'.join(capitalized_list)# join()方法用于将列表中的元素连接成一个字符串，参数是一个可迭代对象，这里使用连字符 '-' 作为分隔符。
print(new_str)

# 9）给定一个元组 fruits = ("apple", "banana", "cherry", "date", "elderberry")，编写一个程序，找出元组中最长的元素。
fruits = ("apple", "banana", "cherry", "date", "elderberry")
len=[]
for fruit in fruits:
    len.append(len(fruit))# len()函数用于返回对象（字符串、列表、元组等）的长度。这里使用len()函数来计算每个元素的长度，并将结果添加到len列表中。
max_length = max(len)
longest_fruit = fruits[len.index(max_length)]
# print(f"最长的元素是: {longest_fruit}")
# fruits = ("apple", "banana", "cherry", "date", "elderberry")
# longest_fruit = fruits[0]
# for fruit in fruits:
#     if len(fruit) > len(longest_fruit):
#         longest_fruit = fruit
# print(longest_fruit)

# 10）给定两个集合 set1 = {1, 2, 3, 4, 5} 和 set2 = {4, 5, 6, 7, 8}，编写一个程序，找出两个集合的交集、并集以及差集。
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set.intersection(set1, set2)# intersection()方法用于返回两个集合的交集，即同时存在于两个集合中的元素。
union = set.union(set1, set2)# union()方法用于返回两个集合的并集，即存在于至少一个集合中的所有元素。
difference = set.difference(set1, set2)# difference()方法用于返回两个集合的差集，即存在于第一个集合但不存在于第二个集合中的元素。
print(f"交集: {intersection}")
print(f"并集: {union}")
print(f"差集: {difference}")

# 11）给定一个集合 original_set = {1, 2, 3, 4, 5}，编写一个程序，向集合中添加元素 6 和 7，并从集合中移除元素 3。
original_set = {1, 2, 3, 4, 5}
original_set.add(6)# add()方法用于向集合中添加一个元素。这里使用add()方法向original_set集合中添加元素 6。
original_set.add(7)# 同样使用add()方法向original_set集合中添加元素 7。

original_set.reomve(3)# remove()方法用于从集合中移除一个元素。这里使用remove()方法从original_set集合中移除元素 3。

# 12）给定一个字典 student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 88}，
# 编写一个程序，将每个学生的分数增加 5 分，并将结果存储在一个新的字典 updated_scores 中。
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 88}
updated_scores = {name: score + 5 for name, score in student_scores.items()}

#13）给定一个字典 fruit_prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.5, "date": 3.0}，编写一个程序，找出价格最高的水果及其价格。
fruit_prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.5, "date": 3.0}
max_price = 0
max_fruit = None
for fruit, price in fruit_prices.items():
  if price > max_price:
    max_price = price
    max_fruit = fruit
print(f"The most expensive fruit is {max_fruit} with a price of {max_price}.")