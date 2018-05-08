from app.app import socketio 


data={
    'money': {
        'balance': 5,
        'transactions': [
            10,
            -5,
        ]
    },
    'contact': {
        'address': 'Sheetla Enclave Gurgaon',
        'mobile': '9717389646'
    }
}

# main class to build the nosql store 

class FirbaseDict():
    def __init__(self, data = {}):
        self.store = data
    
    # to get value of keys from store
    def get(self, key):
        try:
            return self.store[key]
        except KeyError:
            socketio.send('error', 'KeyError')
    
    # to set value of key in store and emit event in the websocket
    def set(self, key, value):
        try:
            self.store[key] = value
            socketio.emit(key, value, broadcast=True)
        except KeyError:
            socketio.send('error', 'KeyError')


firebase = FirbaseDict(data)