from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from config import secret_key
from app.controllers.database import data

app = Flask(__name__)

# configuring options for app object
app.config['SECRET_KEY'] = secret_key

socketio = SocketIO(app)

@app.route('/',methods = ['POST', 'GET'])
def main():
   if request.method == 'GET':
      return render_template('main.html', data=data)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('transaction')
def handle_transaction(json):
    amount= int(json['amount'])
    data['balance'] = data['balance'] + amount
    data['transactions'].append(amount)
    emit('change', data, broadcast=True)
