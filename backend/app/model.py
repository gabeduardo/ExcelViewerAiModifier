from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

if not api_key:
    raise ValueError("❌ COHERE_API_KEY no encontrada en .env")

from langchain_cohere import ChatCohere
from langchain.schema import StrOutputParser
from app.prompting import chat_prompt_template

model = ChatCohere(cohere_api_key=api_key, model="command-a-03-2025")

chain = chat_prompt_template | model | StrOutputParser()