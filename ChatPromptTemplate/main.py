import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate

#chaining...
def language_translate_service()->None:
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    print(f"The api key is ${GOOGLE_API_KEY}")
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",
                                    temperature=0.45,
                                    max_tokens=None,
                                    timeout=None,
                                    max_retries=2,
                                 )
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are helpful assistant who translates languages to Presidents of different nations . You should translate {input_language} to {output_language}",
            ),
            ("human","{input}"),
        ]
    )

    chain = prompt | llm

    prompt_value = chain.invoke({
        "input_language":"English",
        "output_language":"Japanese",
        "input":"I want to open a business."
    })

    print(prompt_value.content,'-',prompt_value.id)

def translator_chat_prompt_template()->None:
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    print(f"The api key is ${GOOGLE_API_KEY}")
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",
                                 temperature=0.2,
                                 max_tokens=None,
                                 timeout=None,
                                 max_retries=2,
                                 )

    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to French. Translate the user sentence.",
        ),
        ("human","I love programming"),
    ]

    baseMessage = llm.invoke(messages)

    print(baseMessage)


def main():
    language_translate_service()


if __name__ == "__main__":
    print("start")
    main()
    print("end")

