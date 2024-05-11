from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "llama3-8b-8192"

chat = ChatGroq(temperature=0, model_name=MODEL_NAME)

system = "You are a helpful assistant."
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

chain = prompt | chat
print(chain.invoke({"text": "Explain the importance of low latency LLMs."}))
