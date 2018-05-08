from app.app import socketio
from app.controllers.eventhandlers import transaction_handler

# just to do post request with websocket 

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('transaction')
def handle_transaction(json):
    transaction_handler(json)

