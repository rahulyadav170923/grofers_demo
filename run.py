from app import app
from config import port
from app.controllers.socketevents import socketio

socketio.run(app.app, host='0.0.0.0', port = port)