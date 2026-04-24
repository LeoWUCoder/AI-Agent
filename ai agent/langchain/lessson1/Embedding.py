# 导入和使用 WebBaseLoader
import os
os.environ["USER_AGENT"] = "Mozilla/5.0"  # 去掉警告
from langchain_community.document_loaders import WebBaseLoader
import bs4
loader = WebBaseLoader(
web_path="https://www.gov.cn/xinwen/2020-06/01/content_5516649.htm",
)
docs = loader.load()

# 1. 不再使用 OpenAI，改用 HuggingFace 的本地模型
from langchain_community.embeddings import HuggingFaceEmbeddings

# 使用一个开源的中文模型 (会自动下载，或者你可以指定本地路径)
embeddings = HuggingFaceEmbeddings(
    model_name="shibing624/text2vec-base-chinese",
    model_kwargs={'device': 'cpu'} # 如果有GPU可以改成 'cuda'
)
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
# 使用分割器分割文档
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.split_documents(docs)
print(len(documents))
# 向量存储 embeddings 会将 documents 中的每个文本片段转换为向量，并将这些向量存储在 FAISS向量数据库中
vector = FAISS.from_documents(documents, embeddings)