import flask
import json

app = flask.Flask(__name__)

class User:
    def __init__(self, name):
        self.name = name

@app.route('/')
def index():
    return flask.Response(json.dumps(User('Alessio').__dict__),
                          mimetype = 'application/json')

@app.route('/hello/<name>')
def hello(name):
    return f'Ciao {name}'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)
