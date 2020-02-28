import flask
import json

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.Response(json.dumps({'name': 'Alessio'}), mimetype = 'application/json')

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
