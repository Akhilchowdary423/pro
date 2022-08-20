from flask import Flask

app=Flask(__name__)
@app.route("/")

def hello_world():
    return "<h1>Hello Friends!</h1><h2>welcom to my youtube channel!</h2><p>AF&F</p><a href=https://www.youtube.com/>youtube</a>"
@app.route("/youtube")

def youtube():
    return "<a href=https://www.youtube.com/>youtube</a>"
if __name__== '__main__':
    app.run()
