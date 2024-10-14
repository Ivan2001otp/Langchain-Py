import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.chains import Runnabl
from langchain.prompts import PromptTemplate

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")



llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.45,max_retries=2,timeout=None) 
prompt_template = PromptTemplate(
    input_variables=["user_input"],
    template="You are Level 5 software Engineer in google and you are supposed to answer brief.Respond to the following : {user_input}"
)

chat_chain = prompt_template | llm 



def fetch_response_from_llm(user_input):
    response = chat_chain.invoke(user_input)
    # print(response)
    return response.content

def main()->None:
    print("You are chatting with a chatbot")
    while True:
        human = input("You : ")
        if human.lower()=="exit":
            break
        response = fetch_response_from_llm(human)
        print(f"Bot:{response}")

if __name__=="__main__":
    main()