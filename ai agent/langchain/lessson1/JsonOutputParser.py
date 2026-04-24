#导入 dotenv 库的 load_dotenv 函数，用于加载环境变量文件（.env）中的配置
import dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser # 导入 JsonOutputParser 类
dotenv.load_dotenv() #加载当前目录下的 .env 文件
os.environ['OPENAI_API_KEY'] = os.getenv("DASHSCOPE_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("DASHSCOPE_BASE_URL")
# 创建大模型实例
llm = ChatOpenAI(model="qwen-plus") # 默认使用 gpt-3.5-turbo
# 需要注意的一点是，这里需要指明具体的role，在这里是system和用户
prompt = ChatPromptTemplate.from_messages([
("system", "你是世界级的技术文档编写者"),
("user", "{input}") # {input}为变量
])
# 创建 JsonOutputParser 实例
output_parser = JsonOutputParser()
# 我们可以把prompt和具体llm的调用和在一起。
chain = prompt | llm | output_parser # 将 JsonOutputParser 添加到链中
message = chain.invoke({"input": "LangChain是什么? 用JSON格式回复，问题用question，回答用answer"})
print(message)
# print(type(message))