from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")


MODEL_NAME = "llama3-8b-8192"



llm = ChatGroq(temperature=0,  groq_api_key = groq_key , model_name=MODEL_NAME)

def get_llm():
  return llm