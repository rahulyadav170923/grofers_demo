from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from config import secret_key
from app.controllers.database import data
import json


app = Flask(__name__)

# configuring options for app object
app.config['SECRET_KEY'] = secret_key

socketio = SocketIO(app)
from app.controllers.eventhandlers import transaction_handler


@app.route('/',methods = ['POST', 'GET'])
def main():
   if request.method == 'GET':
      return render_template('main.html', data=data)

@app.route('/transaction', methods = ['POST'])
def transation():
    transaction_handler(json.loads(request.data))
    return "Amount has been debited/credited"

