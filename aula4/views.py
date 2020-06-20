from flask import Flask, request

"""Extensão Flask"""
def init_app(app: Flask):

    @app.route('/')
    def index():
        print(request.args)
        return "Hello Codeshow"

    @app.route('/contato')
    def contato():
       return "<form><input type='text'></input></form>"