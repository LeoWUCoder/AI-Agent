# # 正态分布可视化
# import math
# import time
# import numpy as np
# import torch
# from d2l import torch as d2l
# def normal(x, mu, sigma):
#     p = 1 / math.sqrt(2 * math.pi * sigma**2)# 计算正态分布的概率密度函数值，**2表示平方，math.sqrt表示开平方，math.pi表示圆周率
#     return p * np.exp(-0.5 / sigma**2 * (x - mu)**2)
# # 可视化
# # 再次使用numpy进行可视化
# x = np.arange(-7, 7, 0.01)

# # 均值和标准差对
# params = [(0, 1), (0, 2), (3, 1)]
# d2l.plot(x, [normal(x, mu, sigma) for mu, sigma in params], xlabel='x',
#          ylabel='p(x)', figsize=(4.5, 2.5),
#          legend=[f'mean {mu}, std {sigma}' for mu, sigma in params]) 
# import matplotlib.pyplot as plt
# plt.show()

# 只使用张量和自动求导。 来实现线性回归
####
#生成数据
####
import random# 导入random库，random是Python内置的一个模块，用于生成随机数和进行随机操作。
import torch# 导入torch库，torch是一个流行的深度学习框架，用于构建和训练神经网络模型。
from d2l import torch as d2l# from...import...表示从d2l库中导入torch模块，并将其命名为d2l，以便在后续代码中使用d2l来调用torch模块的功能。

def synthetic_data(w, b, num_examples):  #@save
    """生成y=Xw+b+噪声"""
    X = torch.normal(0, 1, (num_examples, len(w)))# 生成μ=0，σ=1的正态分布随机数，size是num_examples行，len(w)列的二维张量，表示输入特征矩阵X。
    y = torch.matmul(X, w) + b# y=Xw+b，使用torch.matmul函数进行矩阵乘法，将输入特征矩阵X与权重向量w相乘，并加上偏置b，得到线性回归模型的输出y。
    y += torch.normal(0, 0.01, y.shape)# 在y的基础上添加噪声，生成μ=0，σ=0.01的正态分布随机数，size与y相同的张量，并将其加到y上，以模拟真实数据中的噪声。
    return X, y.reshape((-1, 1))# y.reshape((-1, 1))将y的形状调整为(num_examples, 1)，即每个样本对应一个标签，返回输入特征矩阵X和标签y。

true_w = torch.tensor([2, -3.4])# 真实的权重向量true_w是一个包含两个元素的张量，分别为2和-3.4，表示线性回归模型中每个特征的权重。
true_b = 4.2
features, labels = synthetic_data(true_w, true_b, 1000)
# 解释一下x*w这件事情，其实本质上从数学上看，是不符合矩阵乘法的维度要求，但是在PyTorch中，torch.matmul函数会自动处理维度不匹配的情况，进行广播（broadcasting）操作，使得矩阵乘法能够顺利进行。
# 具体来说，当输入特征矩阵X的形状为(num_examples, num_features)时，
# 权重向量w的形状为(num_features,)或者(num_features, 1)，torch.matmul函数会自动将权重向量w进行广播，使其与输入特征矩阵X的形状兼容，从而完成矩阵乘法的计算。
print('features:', features[0],'\nlabel:', labels[0])
# features: tensor([0.1631, 1.3261]) 
# label: tensor([0.0454])
d2l.set_figsize()
d2l.plt.scatter(features[:, (1)].detach().numpy(), labels.detach().numpy(), 1)
d2l.plt.show()# 可视化

####
#读取数据
####

# 训练模型时要对数据集进行遍历，每次抽取一小批量样本，并使用它们来更新我们的模型。
def data_iter(batch_size, features, labels):# 该函数接收批量大小、特征矩阵和标签向量作为输入
    num_examples = len(features)# 计算特征矩阵中的样本数量，即行数，存储在num_examples变量中。
    indices = list(range(num_examples))# 创建一个包含从0到num_examples-1的整数列表，表示样本的索引。
    # 这些样本是随机读取的，没有特定的顺序
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):# 从0开始，以batch_size为步长，遍历样本索引列表indices，生成批量的样本索引。
        batch_indices = torch.tensor(
            indices[i: min(i + batch_size, num_examples)])# 生成当前批量的样本索引，使用torch.tensor将其转换为张量形式，存储在batch_indices变量中。 
        #min(i + batch_size, num_examples)确保在最后一个批量时不会超过样本数量。
        yield features[batch_indices], labels[batch_indices]# 使用yield关键字将当前批量的特征和标签作为生成器的输出，供后续代码使用。
         # 【关键点】使用 yield 返回当前批次的数据
        # 函数在这里暂停，把 X_batch 和 y_batch 交给外面的循环
        # 下次循环时，从这里继续执行，i 自动增加 batch_size，直到遍历完整个数据集。

# 在我们开始用小批量随机梯度下降优化我们的模型参数之前， 我们需要先有一些参数——初始化模型参数w和b,后续要不断更新这些餐胡。
w = torch.normal(0, 0.01, size=(2,1), requires_grad=True)# 生成一个形状为(2, 1)的张量，元素服从均值为0、标准差为0.01的正态分布，并且设置requires_grad=True，表示这个张量需要计算梯度，用于后续的反向传播和参数更新。
b = torch.zeros(1, requires_grad=True)

# 定义模型
# 广播机制： 当我们用一个向量加一个标量时，标量会被加到向量的每个分量上。
def linreg(X, w, b):  #@save
    """线性回归模型"""
    return torch.matmul(X, w) + b

# 定义损失函数
def squared_loss(y_hat, y):  #@save
    """均方损失"""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

# 定义优化算法
def sgd(params, lr, batch_size):  #@save
    """小批量随机梯度下降"""
    with torch.no_grad():# 暂时关闭梯度计算
        for param in params:
            param -= lr * param.grad / batch_size# param.grad（梯度存取，存取反向传播后的梯度）是参数的梯度，lr是学习率，batch_size是批量大小。通过将梯度除以批量大小，我们可以得到每个样本的平均梯度，从而更稳定地更新参数。
            param.grad.zero_()# 更新参数后，将梯度清零，以便下一次迭代计算新的梯度。PyTorch 的机制是梯度累加（Accumulation）。如果你不清零，下一次 loss.backward() 计算出的梯度会加到现有的 param.grad 上，而不是覆盖它。

# 训练——主函数
lr = 0.03
num_epochs = 3
net = linreg
loss = squared_loss
batch_size = 10
for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y)  # X和y的小批量损失
        # 因为l形状是(batch_size,1)，而不是一个标量。l中的所有元素被加到一起，
        # 并以此计算关于[w,b]的梯度
        l.sum().backward()# 即随机梯度下降原理的求和再求偏导
        sgd([w, b], lr, batch_size)  # 使用参数的梯度更新参数
    with torch.no_grad():# with torch.no_grad()上下文管理器来禁用梯度计算，这样在评估模型性能时就不会计算梯度，从而节省内存和计算资源。
        # with的用法：with语句用于包装代码块，在代码块执行前后自动执行特定的操作。在这里，with torch.no_grad()表示在代码块内禁用梯度计算。
        # 前后自动执行的操作是指在进入代码块时禁用梯度计算，在退出代码块时恢复正常的梯度计算。（就是with底下的代码）
        train_l = loss(net(features, w, b), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')
    print(f'w的估计误差: {true_w - w.reshape(true_w.shape)}')
print(f'b的估计误差: {true_b - b}')