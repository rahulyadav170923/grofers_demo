from app import app
from config import port
app.socketio.run(app.app, port = port)