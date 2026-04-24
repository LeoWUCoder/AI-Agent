import numpy as np
import torch
from torch.utils import data# 导入torch.utils.data模块，提供了数据加载和预处理的工具，用于构建数据集和数据加载器。
from d2l import torch as d2l
true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = d2l.synthetic_data(true_w, true_b, 1000)
# def synthetic_data(w, b, num_examples):  #@save
#     """生成y=Xw+b+噪声"""
#     X = torch.normal(0, 1, (num_examples, len(w)))# 生成μ=0，σ=1的正态分布随机数，size是num_examples行，len(w)列的二维张量，表示输入特征矩阵X。
#     y = torch.matmul(X, w) + b# y=Xw+b，使用torch.matmul函数进行矩阵乘法，将输入特征矩阵X与权重向量w相乘，并加上偏置b，得到线性回归模型的输出y。
#     y += torch.normal(0, 0.01, y.shape)# 在y的基础上添加噪声，生成μ=0，σ=0.01的正态分布随机数，size与y相同的张量，并将其加到y上，以模拟真实数据中的噪声。
#     return X, y.reshape((-1, 1))# y.reshape((-1, 1))将y的形状调整为(num_examples, 1)，即每个样本对应一个标签，返回输入特征矩阵X和标签y。

def load_array(data_arrays, batch_size, is_train=True):  #@save
    """构造一个PyTorch数据迭代器"""
    dataset = data.TensorDataset(*data_arrays)
    # *data_arrays的*是一个解包的运算，如果传入 (features, labels)，它等同于 data.TensorDataset(features, labels)。
    # 表示将data_arrays中的元素作为参数传递给TensorDataset函数，构造一个TensorDataset对象dataset。TensorDataset是PyTorch提供的一个数据集类，用于将多个张量组合成一个数据集。
    return data.DataLoader(dataset, batch_size, shuffle=is_train)

batch_size = 10
data_iter = load_array((features, labels), batch_size)# net = nn.Sequential(nn.Linear(2, 1))
# data_iter和dataset, batch_size, shuffle=is_train
# nn是神经网络的缩写
from torch import nn

net = nn.Sequential(nn.Linear(2, 1))# nn.Sequential是一个容器模块，可以将多个层组合在一起，按照顺序执行。在这里，我们使用nn.Sequential来构建一个简单的线性回归模型，其中包含一个线性层nn.Linear(2, 1)，表示输入特征的维度为2，输出特征的维度为1。

net[0].weight.data.normal_(0, 0.01)#  net[0].weight.data.normal_(0, 0.01)表示对net[0]（即第一个线性层）的权重进行初始化，使用均值为0、标准差为0.01的正态分布随机数来填充权重数据。
net[0].bias.data.fill_(0)# net[0].bias.data.fill_(0)表示对net[0]（即第一个线性层）的偏置进行初始化，将偏置数据填充为0。

loss = nn.MSELoss()# 定义损失函数，使用均方误差损失函数（Mean Squared Error Loss），用于衡量模型预测值与真实标签之间的差距。

trainer = torch.optim.SGD(net.parameters(), lr=0.03)
# 定义优化算法，使用随机梯度下降（Stochastic Gradient Descent）优化器，net.parameters()表示要优化的模型参数，lr=0.03表示学习率。
# net.parameters()返回一个生成器，包含了模型中所有需要优化的参数（权重和偏置）。通过将这些参数传递给优化器，优化器就能够在训练过程中更新这些参数以最小化损失函数。
# net = nn.Sequential(nn.Linear(2, 1))
# def sgd(params, lr, batch_size):  #@save
#     """小批量随机梯度下降"""
#     with torch.no_grad():# 暂时关闭梯度计算
#         for param in params:
#             param -= lr * param.grad / batch_size# param.grad（梯度存取，存取反向传播后的梯度）是参数的梯度，lr是学习率，batch_size是批量大小。通过将梯度除以批量大小，我们可以得到每个样本的平均梯度，从而更稳定地更新参数。
#             param.grad.zero_()# 更新参数后，将梯度清零，以便下一次迭代计算新的梯度。PyTorch 的机制是梯度累加（Accumulation）。如果你不清零，下一次 loss.backward() 计算出的梯度会加到现有的 param.grad 上，而不是覆盖它。

num_epochs = 3
for epoch in range(num_epochs):
    for X, y in data_iter:
        l = loss(net(X) ,y)
        # 计算当前批量的损失，net(X)表示模型对输入特征X的预测值，y是对应的真实标签。通过将预测值和真实标签传递给损失函数loss，计算出当前批量的损失l。
        trainer.zero_grad()
        # 在进行反向传播之前，先将优化器中的梯度清零。因为在PyTorch中，默认情况下，梯度是累积的（即每次调用backward()时，新的梯度会加到现有的梯度上）。
        # 通过调用trainer.zero_grad()，我们可以确保在每次迭代开始时，梯度被重置为零，以便正确计算当前批量的梯度。
        l.backward()# 计算当前批量的梯度，调用l.backward()会自动计算损失l关于模型参数的梯度，并将这些梯度存储在每个参数的.grad属性中。
        # .backward()方法会根据计算图自动计算梯度，利用链式法则将损失函数的梯度传播回模型的参数。
        # 梯度：在机器学习中，梯度是一个向量，表示损失函数相对于目前模型参数w和b的变化率。它指示了如何调整模型参数以最小化损失函数。
        # ——先对y求导，y是net(X)的函数，net(X)又是w和b的函数，所以通过链式法则可以求出损失函数关于w和b的梯度。

        trainer.step()# 更新模型参数，调用trainer.step()会根据计算得到的梯度和优化算法的规则来更新模型参数，以最小化损失函数。
        # trainer.step()=torch.optim.SGD(net.parameters(), lr=0.03).step()，其中net.parameters()包含了模型中所有需要优化的参数，lr=0.03是学习率。通过调用trainer.step()
        # net.parameters()中的参数会根据计算得到的梯度进行更新，使得损失函数的值尽可能小。
        # .step()方法会根据优化算法的规则（在这里是随机梯度下降）来调整模型参数，使得损失函数的值尽可能小。
    l = loss(net(features), labels)# 在每个epoch结束后，计算整个训练集上的损失，net(features)表示模型对整个训练集的预测值，labels是对应的真实标签。通过将预测值和真实标签传递给损失函数loss，计算出整个训练集上的损失l。
    print(f'epoch {epoch + 1}, loss {l:f}')

w = net[0].weight.data
print('w的估计误差：', true_w - w.reshape(true_w.shape))
b = net[0].bias.data
print('b的估计误差：', true_b - b)