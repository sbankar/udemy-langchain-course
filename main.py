import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from dotenv import load_dotenv

load_dotenv()
def main():
    print("Hello from udemy-langchain-course!")
    person = 'Narendra Modi'

    summary_template = """
    Give me summary about {person}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["person"], template=summary_template
    )

    llm = ChatOllama(temperature=0, model="gemma3:270m")
    #llm = ChatOpenAI(temperature=0, model="gpt-5")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"person": person})
    print(response.content)


if __name__ == "__main__":
    main()
