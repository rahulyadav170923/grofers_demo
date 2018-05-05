from app import app
from config import port
app.socketio.run(app.app, host='0.0.0.0', port = port)