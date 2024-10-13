import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# tweet_prompt = PromptTemplate.from_template("You are a content creator. Write me a tweet about {topic}")
# tweet_chain = LLMChain(llm=llm,prompt=tweet_prompt,verbose=True)

def ChatModel()->None:
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    print(f"google-api-key ${GOOGLE_API_KEY}")
    llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=GOOGLE_API_KEY,temperature=0.8)
    response = llm.invoke('Write a short paragraph about black holes.')
    print(response)

if __name__=="__main__":
    # topic="how will be the future of game development & AI"
    # resp=tweet_chain.run(topic=topic)
    # print(resp)
    ChatModel()

