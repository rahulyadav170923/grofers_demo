from app.app import socketio
from app.controllers.database import data

def transaction_handler(json):
    amount= int(json['amount'])
    data['balance'] = data['balance'] + amount
    data['transactions'].append(amount)
    socketio.emit('change', data, broadcast=True)
