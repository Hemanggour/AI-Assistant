import requests

apikey = '10'
BASE = "http://127.0.0.1:5000/"

def sendRequest(arg, command=None, apikey=None):
  if apikey:
    return (requests.post(BASE + "/api", {'apikey': apikey, 'message': arg})).json()
  elif command in ['news', 'play']:
    return requests.get(BASE + '/api', {'command': command, 'arg': arg}).json()