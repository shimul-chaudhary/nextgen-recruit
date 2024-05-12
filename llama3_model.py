from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "llama3-8b-8192"

llm = ChatGroq(temperature=0, model_name=MODEL_NAME)

def get_llm():
  return llm