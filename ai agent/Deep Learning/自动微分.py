import torch
x=torch.arange(4.0)# 创建一个包含4个元素的张量，元素值为0.0、1.0、2.0和3.0
# torch.arange(start（起始，默认0.0）, end, step（步长，默认1.0）, dtype(数据类型)=None, device（cpu/cuda）=None)
x.requires_grad_(True)# 设置张量x的requires_grad属性为True，表示需要计算梯度，理解成（开关）开启自动求导功能
y = 2 * torch.dot(x, x)
# torch.dot(input, other)计算两个一维张量的点积，结果是一个标量。这里计算的是2乘以x和x的点积，即2乘以x中每个元素的平方和
y.backward()
# 反向传播，计算y关于x的梯度。由于y是一个标量，backward()函数会自动计算y对x的梯度，y对x的四个元素点求导
print(x.grad)
# 输出x的梯度，即y对x的导数。根据y=2*x^2，y对x的导数为4*x，因此输出的梯度应该是[0.0, 4.0, 8.0, 12.0]，对应于x中每个元素的导数值。
x.grad.zero_()# 将x的梯度清零，准备进行下一次计算。因为在PyTorch中，默认情况下，梯度会累积，所以在每次反向传播之前需要手动清零梯度。  
y = x * x
# 等价于y.backward(torch.ones(len(x)))
# 2. 错误示范：直接对向量求导
# y.backward() 
# ❌ 报错！RuntimeError: grad can be implicitly created only for scalar outputs
# 因为框架不知道你是想要雅可比矩阵，还是梯度和。
y.sum().backward()# 正确示范：先对y求和得到一个标量，(先sum，再backward），再进行反向传播

x.grad.zero_()# 将x的梯度清零，准备进行下一次计算。
y = x * x
u = y.detach()# detach()函数用于从计算图中分离张量u，使其不再参与梯度计算。这样，u将成为一个新的张量，具有与y相同的数据，但不包含梯度信息。
z = u * x
z.sum().backward()# 对z求和得到一个标量，然后进行反向传播，计算z关于x的梯度。由于u是从y中分离出来的张量，不参与梯度计算，因此z关于x的梯度将只考虑x的部分，即z对x的导数为u。
