from flask import Flask
from collections import Counter
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World -Anuja'


@app.route('/authors')
def authors():
    url1 = "https://jsonplaceholder.typicode.com/users"
    url2 = "https://jsonplaceholder.typicode.com/posts"
    try:
        author = requests.get(url1)
        count = requests.get(url2)
    except requests.ConnectionError:
        return "Connection Error"

    authorNames = json.loads(author.text)
    postCount = json.loads(count.text)

    text=""
    for i in range(len(authorNames)):
        c=0
        for j in range(len(postCount)):
            if postCount[j]['userId']==authorNames[i]['id']:
                c+=1
        text=text+authorNames[i]['name']+" "+str(c)+"<br>"
    return text

if __name__ == "__main__":
    app.run(debug=True)
