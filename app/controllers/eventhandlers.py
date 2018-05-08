from app.app import socketio
from app.controllers.database import firebase

# just to handle update changes to the store. (Can be done from REST api as well)

def transaction_handler(json):
    amount= int(json['amount'])
    data = firebase.get('money')
    if 'error' not in data.keys():
        data['balance'] = data['balance'] + amount
        data['transactions'].append(amount)
        firebase.set('money', data)