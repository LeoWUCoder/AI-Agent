# 导入和使用 WebBaseLoader
import os
os.environ["USER_AGENT"] = "Mozilla/5.0"  # 去掉警告
from langchain_community.document_loaders import WebBaseLoader
import bs4
loader = WebBaseLoader(
web_path="https://www.gov.cn/xinwen/2020-06/01/content_5516649.htm",
)
docs = loader.load()
print(docs)