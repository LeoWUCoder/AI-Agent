import os
# 导入 Python 内置的 os 模块，用于访问操作系统功能（读环境变量、文件路径等）。
from dotenv import load_dotenv
# 从 python-dotenv 包中导入 load_dotenv 函数，用于加载 .env 文件里的变量。
import dashscope
# 导入阿里百炼 dashscope 包，这是一个用于调用各种语言模型（如 Qwen、qwen-plus 等）的库，提供了统一的接口来进行文本生成等任务。
from dashscope import Generation
#从 dashscope 中导入 Generation 模型接口，用来调用如 Qwen、qwen-plus 等模型的文本生成能力。

# 1) 加载 .env 文件（需与本脚本在同一目录）
load_dotenv()

# 2) 从环境变量读取（读取——用了os）并设置给 dashscope
api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    raise RuntimeError("未在 .env 中找到 DASHSCOPE_API_KEY，请在 .env 写入：DASHSCOPE_API_KEY=你的APIKey")

dashscope.api_key = api_key

# 3) 你的消息体
messages = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    # 系统提示词·system prompt，告诉模型它的角色和行为准则。
    {'role': 'user', 'content': '你是谁？'}
    # 用户消息·user message，用户输入的内容，模型将基于这些内容生成回复。
]

# 4) 发起调用
response = Generation.call(
    model="qwen-plus",
    messages=messages,
    result_format='message'
)
# Generation.call() 是 dashscope 中的一个方法，用于调用指定模型进行文本生成。
# 参数说明：
# model="qwen-plus"：指定使用的模型，这里是 "qwen-plus"。
# messages=messages：传入之前定义的消息列表，包含系统提示和用户消息。
# result_format='message'：指定返回结果的格式，这里是 'message'，表示返回一个包含生成文本的消息对象。           

# 5) 友好打印
# Generation(message) 返回对象通常含有 .output_text 或 .output.choices
print(getattr(response, "output_text", response))
# 使用 getattr 来尝试获取 response 的 output_text 属性，如果没有则直接打印 response 对象。