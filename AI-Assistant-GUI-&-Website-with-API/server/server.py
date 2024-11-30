from flask import Flask, request, render_template, redirect
import AI
from flask_restful import Api, Resource, reqparse
from youtube import youtube_search
from news import getNews
# from authentication import Authentication as auth
# from database import Database as db
# from registration import Register as res

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

CHAT_SIZE = 10
userChats = []
modelChats = []

def callAI(message):
        if message:
            # content = {
            #     'parts': [
            #         {'text': 'Previous chats:\n' + '\n'.join(userChats)},
            #         {'text': 'Current message: ' + message}
            #     ]
            # }
            model = AI.GenerateContent(message)
            # if len(userChats) >= CHAT_SIZE:
            #     userChats.pop(0)
            #     modelChats.pop(0)
            # userChats.append(message)
            # modelChats.append(model)
            return (message, model)

class HandleUser(Resource):
    def get(self):
        data = request.args
        command = data['command']
        arg = data['arg']
        if command in ['news', 'play']:
            if command == 'news':
                return {'news': getNews(arg)}
            else:
                return {'link': youtube_search(arg)}

    def post(self):
        apikey = request.form.get('apikey')
        arg = request.form.get('message')
        # if auth.ValidateApiKey():
        response = callAI(arg)
        # db.saveMessage(apikey, message, response)
        return {'User': response[0],
                'Model': response[1]}

api.add_resource(HandleUser, "/api")

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            content = {
                'parts': [
                    {'text': 'Previous chats:\n' + '\n'.join(userChats)},
                    {'text': 'Current message: ' + message}
                ]
            }
            model = AI.GenerateContent(content)
            if len(userChats) >= 10:
                userChats.pop(0)
                modelChats.pop(0)
            userChats.append(message)
            modelChats.append(model)
            return render_template('chat.html', range=range(0, len(userChats)), modelChats=modelChats, userChats=userChats)
    return render_template('chat.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)