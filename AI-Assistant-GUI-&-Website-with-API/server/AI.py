import google.generativeai as ai
import APIs

def GenerateContent(Query):
    try:
        ai.configure(api_key=APIs.api('gemini'))
        model = ai.GenerativeModel("gemini-1.5-flash")
        res = (model.generate_content(Query))
    except Exception as err:
        print(err)
    else:
        res = (res.text).replace("*", "")
        return res

if __name__ == "__main__":
    while(True):
        query = input("Enter Query: ")
        res = GenerateContent(query)
        print(res)
        # print(res.usage_metadata)