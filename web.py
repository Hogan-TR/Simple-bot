from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/user')
def user():
    u = {
        'username': 'Hogan',
        'nickname': '霍根',
    }
    return jsonify(u)


app.run('127.0.0.1', 8080)
