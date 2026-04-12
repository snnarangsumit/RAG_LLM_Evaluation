#Pytest -
import os
import pytest
import requests
from langchain_openai import ChatOpenAI
from ragas import SingleTurnSample
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import LLMContextPrecisionWithoutReference
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.asyncio
async def test_context_precision():
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    langchain_llm = LangchainLLMWrapper(llm)
    context_precision = LLMContextPrecisionWithoutReference(llm=langchain_llm)
    question = "How many articles are there in the Selenium webdriver python course?"
    responseDict = requests.post("https://rahulshettyacademy.com/rag-llm/ask",
                                 json={
                                     "question": question,
                                     "chat_history": []
                                 }).json()
    print(responseDict)
    sample = SingleTurnSample(
        user_input=question,
        response=responseDict["answer"],
        retrieved_contexts=[responseDict["retrieved_docs"][0]["page_content"],
                            responseDict["retrieved_docs"][1]["page_content"],
                            responseDict["retrieved_docs"][2]["page_content"]]
    )
    score = await context_precision.single_turn_ascore(sample)
    print(score)
    assert score > 0.8