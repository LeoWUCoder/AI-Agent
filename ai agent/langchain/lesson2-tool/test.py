from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool 
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage # 1. 导入消息类型
import os

# --- 环境配置 ---
load_dotenv(encoding='utf-8')
os.environ['OPENAI_API_KEY'] = os.getenv("DASHSCOPE_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("DASHSCOPE_BASE_URL")

# --- 初始化模型与工具 ---
model = init_chat_model("qwen-plus", model_provider="openai") 

@tool
def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
    print(f"🛠️  [系统执行] 正在查询 {city} 的天气...")
    return "晴天，温度 15°C"

model_with_tools = model.bind_tools([get_weather])

# --- 模拟对话流程 ---

# 1. 用户提问
user_msg = HumanMessage(content="北京现在的天气怎么样？")
print(f"👤 用户: {user_msg.content}")

# 2. AI 思考并决定调用工具
# 这里的消息列表记录了对话历史
messages = [user_msg] 
ai_response = model_with_tools.invoke(messages)
messages.append(ai_response) # 把 AI 的“思考”加入历史

# 3. 检查并执行工具调用
if ai_response.tool_calls:
    tool_call = ai_response.tool_calls[0] # 获取第一个工具调用
    
    # 🔑 关键步骤：真正执行 Python 函数
    # 从 tool_call 中提取参数
    result = get_weather.invoke(tool_call['args']) 
    
    # 创建工具消息，把结果“喂”回给 AI
    tool_msg = ToolMessage(content=result, tool_call_id=tool_call['id'])
    messages.append(tool_msg)
    
    print(f"🤖 AI (思考中): 我查到了，结果是 {result}")

    # 4. AI 根据结果生成最终回答
    final_response = model_with_tools.invoke(messages)
    print(f"🤖 AI (最终回答): {final_response.content}")

else:
    print(f"🤖 AI: {ai_response.content}")