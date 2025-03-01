import gradio as gr, os, json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai = OpenAI()

openai_key = os.getenv("OPENAI_API_KEY")
model = 'gpt-4o'
