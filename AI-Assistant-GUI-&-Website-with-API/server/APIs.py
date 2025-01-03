import json
import getPath

def api(apiName):
    api = ''
    with open(getPath.getPath("APIs.json")) as file:
        api = json.load(file)[apiName]
    return api