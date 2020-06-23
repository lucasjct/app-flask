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
   
   
def page_other(app: Flask):
    
    @app.route('/lista')
    def tabela():
        return """<ul><li>Teste1</li>
                     <li>Teste2</li>
                     <li>Teste3</li></ul>"""