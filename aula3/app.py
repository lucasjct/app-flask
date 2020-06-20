from flask import Flask

app = Flask(__name__)

@app.route("/") #wraper de roteamento
def index():
    return "<h1>Hello, Codeshow!</h1>"


@app.route("/sobre")
def sobre():
    return "<h1>Delivery Food</h1>"