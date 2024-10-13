import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def Prompt_Template()->None:
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    print(GOOGLE_API_KEY)
    llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=GOOGLE_API_KEY,temperature=0.45)
    prompt = PromptTemplate.from_template("You are a content creator . Write me a tweet about the {topic}")
    chain = LLMChain(llm=llm,prompt=prompt,verbose=True)
    topic="Does Game development has future with AI"
    response = chain.invoke(input=topic)
    print(response)
    print(response['topic'])
    print(response['text'])
    #topic,text are response attributes


def main():
    Prompt_Template()

if __name__=="__main__":
    main()