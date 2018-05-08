from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from config import secret_key
import json


app = Flask(__name__)

# configuring options for app object
app.config['SECRET_KEY'] = secret_key

socketio = SocketIO(app)

from app.controllers.eventhandlers import transaction_handler
from app.controllers.database import firebase


@app.route('/',methods = ['POST', 'GET'])
def main():
   if request.method == 'GET':
      return render_template('main.html', store=firebase.store)



#  below endpoints are just to check if our Firebase store is working correctly
@app.route('/money', methods = ['POST'])
def transation():
    transaction_handler(json.loads(request.data))
    return "Amount has been debited/credited"

@app.route('/contact', methods = ['POST'])
def contact():
    firebase.set('contact', json.loads(request.data))
    return "Contacts have been updated"


