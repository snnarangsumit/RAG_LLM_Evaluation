import os
import pytest
from langchain_community.document_loaders import DirectoryLoader, UnstructuredWordDocumentLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from ragas.testset import TestsetGenerator
import nltk
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set API keys from .env (never hardcode these)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["RAGAS_APP_TOKEN"] = os.getenv("RAGAS_APP_TOKEN")

nltk.data.path.append(os.getenv("NLTK_DATA_PATH", "./nltk_data"))

llm = ChatOpenAI(model="gpt-4", temperature=0)
langchain_llm = LangchainLLMWrapper(llm)
embed = OpenAIEmbeddings()

loader = DirectoryLoader(
    path=os.getenv("DOCS_PATH", "./docs"),
    glob="**/*.docx",
    loader_cls=UnstructuredWordDocumentLoader
)

docs = loader.load()
generate_embeddings = LangchainEmbeddingsWrapper(embed)
generator = TestsetGenerator(llm=langchain_llm, embedding_model=generate_embeddings)
dataset = generator.generate_with_langchain_docs(docs, testset_size=20)
print(dataset.to_list())
dataset.upload()