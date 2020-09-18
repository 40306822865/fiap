from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Hola FIAP!</h1>\n MBA! o/ <br>  Guilherme V2"

if __name__ == '__main__':
    application.run()
