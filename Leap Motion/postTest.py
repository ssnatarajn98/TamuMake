import requests
import json
url = "http://125b72cf.ngrok.io/giveme"
postParams = {
    "img" : "hello"
}

headers = {'content-type' : 'application/json'}

post = requests.post(url = url, data = json.dumps(postParams), headers = headers)
print(post.status_code)
print(post)
