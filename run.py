from flask import Flask, make_response, request, redirect, render_template
import requests
import json

app = Flask(__name__)

#
# Task 1
#
@app.route('/')
def index():
    return 'Hello World -Anuja'

#
# Task 2
#
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

#
# Task 3
#
@app.route('/setcookie')
def setcookie():
    response = make_response(redirect('/'))
    response.set_cookie('anuja', value='19')
    return response

#
# Task 4
#
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('anuja')
    return name


#
# Task 5
#

#
# Task 6
#

#
# Task 7
#
if __name__ == "__main__":
    app.run(debug=True)
