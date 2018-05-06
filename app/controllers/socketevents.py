from app.app import socketio
from app.controllers.eventhandlers import transaction_handler

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('transaction')
def handle_transaction(json):
    transaction_handler(json)