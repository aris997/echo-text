from globals import *
from langchain_cohere import ChatCohere

def answer(userMessage):
    # client = OpenAI(api_key=OPENAI_API_KEY)

    # response = client.chat.completions.create(
    #     model = "gpt-3.5-turbo-0125",
    #     response_format="json_object",
    #     messages = [
    #         {"role" : "system", "content" : "Sei una cartomante che legge le mani delle persone e racconta il futuro con arguto pensiero, leggi i sogni e li comprendi e aiuti le persone a capirli."},
    #         {"role" : "user", "content" : userMessage}
    #     ],
        
    # )

    # return response.choices[0].message.content

    llm = ChatCohere(
        model="command-r-plus",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        cohere_api_key=COHERE_API_KEY
    )
    return llm.invoke("Sei un giovane italiano, molto informato su tante cose ma ricorda di usare un gergo colloquiale: " + userMessage).content