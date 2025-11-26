import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

llm = init_chat_model(
    model="gpt-5-nano",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    organization=os.getenv("OPENAI_ORGANIZATION"),
)

response = llm.invoke("Write a one-sentence bedtime story about a unicorn.")

print(response)


def main():
    print("Hello from ai-lab!")


if __name__ == "__main__":
    main()
