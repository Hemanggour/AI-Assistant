import google.generativeai as ai
import datetime

ai.configure(api_key="API-KEY")
model = ai.GenerativeModel("gemini-1.5-flash")

def GenerateContent(query):
    chat = model.start_chat(history=[])
    try:
        res = chat.send_message(query)
        res.resolve()
        message =  chat.history
        userStr = f"{message[0].role}: {message[0].parts[0].text}"
        AIStr = f"{message[1].role}: {message[1].parts[0].text}"
        AIStr = AIStr.replace("*", "")
        message.clear()
        with open("ChatHistory.txt", "a", encoding="utf-8") as file:
            file.write(f"{datetime.datetime.now()}\n{userStr}\n{AIStr}\n\n")
        return (res.text).replace("*", "")
    except Exception as err:
        print(err)

if __name__ == "__main__":
    chat = model.start_chat(history=[])
    while(True):
        query = input("Enter Query: ")
        print(GenerateContent(query))