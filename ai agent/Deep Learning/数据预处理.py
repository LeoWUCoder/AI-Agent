import os
os.makedirs(os.path.join('D:/ai agent/Deep Learning', 'data'), exist_ok=True)# 生成一个路径D:/ai agent/Deep Learning/data
# exist_ok=True 表示：如果该目录（../data）已经存在，不会报错，程序会继续正常执行。如果设为 False（默认值），当目录已存在时会抛出异常。
# 如果路径已经存在则不报错
# os.path.join('..', 'data')：
# 用于智能地拼接文件路径。
# '..' 代表上一级目录。
# 'data' 是文件夹名称。
data_file = os.path.join('D:/ai agent/Deep Learning', 'data', 'house_tiny.csv')# 这里定义了一个变量 data_file，它存储了完整的文件路径。

## 写入数据
with open(data_file, 'w') as f:
    # 使用 with 语句打开文件。'w' 模式表示写入（Write）。如果文件不存在，会自动创建；如果文件已存在，内容会被覆盖。
    # as f 将打开的文件对象赋值给变量 f。
    f.write('NumRooms,Alley,Price\n')# 写入表头
    f.write('NA,Pave,127500\n')# 写入第一行数据
    f.write('2,NA,106000\n')# 写入第二行数据
    f.write('4,NA,178100\n')# 写入第三行数据
    f.write('NA,NA,140000\n')# 写入第四行数据
### 这段代码的作用是创建一个 CSV 文件，并向其中写入一些数据。CSV（Comma-Separated Values）是一种常用的文本文件格式，用于存储表格数据。

## 读取数据
# 安装pandas库
# pip install pandas
import pandas as pd # 导入 pandas 库，并将其命名为 pd，以便在后续代码中使用。   
data = pd.read_csv(data_file) # 使用 pandas 库中的 read_csv 函数读取 CSV 文件。data_file 是之前定义的文件路径变量。这个函数会将 CSV 文件中的数据加载到一个 DataFrame 对象中，DataFrame 是 pandas 中用于存储表格数据的主要数据结构。
print(data)

## 处理缺失值
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
# 这行代码将 DataFrame 中的前两列（NumRooms 和 Alley）分配给变量 inputs，第三列（Price）分配给变量 outputs
# # iloc 是 pandas 中用于基于位置进行索引的方法，0:2 表示选择第 0 列和第 1 列（不包括第 2 列），而 2 表示选择第 2 列。
inputs = inputs.fillna(inputs.mean(numeric_only=True))# 这行代码使用 fillna 方法来处理 inputs 中的缺失值（NA）。fillna 方法会将缺失值替换为指定的值，这里使用 inputs.mean() 来计算每列的平均值，并将缺失值替换为对应列的平均值。
print(inputs)

inputs = pd.get_dummies(inputs, dummy_na=True)
# 这行代码使用 pandas 的 get_dummies 函数将 inputs 中的分类变量（Alley 列）转换为虚拟变量（dummy variables）。dummy_na=True 参数表示在转换过程中也会为缺失值（NA）创建一个新的虚拟变量列。
print(inputs)

## 转换成张量
import tensorflow as tf

X = tf.constant(inputs.to_numpy(dtype=float))
# 这行代码将 inputs DataFrame 中的数据转换为一个 NumPy 数组，并将其数据类型指定为 float。然后，使用 tf.constant 函数将这个 NumPy 数组转换为一个 TensorFlow 张量，并将其赋值给变量 X。
y = tf.constant(outputs.to_numpy(dtype=float))
# 这行代码将 outputs Series 中的数据转换为一个 NumPy 数组，并将其数据类型指定为 float。然后，使用 tf.constant 函数将这个 NumPy 数组转换为一个 TensorFlow 张量，并将其赋值给变量 y。

print(X, y)