Installation Steps : 

    cd grofers_demo
    Install [Virtualenv](https://virtualenv.pypa.io/en/stable/)
    virtualenv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

Setting environment variables (Add this in your ~/.bashrc):
    export secret = "" #enter your secret key for app
    export PORT = ""   #Choose port for your app
    source ~/.bashrc
    
Run the app server:
    (using python version 3.6.4)
    python run.py

Documantation :-
Database: It is a volatile server local key-value store.
        Keys: 
        name: 'balance' type: Integer
        name: 'transactions' type: Array 


Events: 
    'transaction' : This is a custom event triggered when client send transaction infomation to server.
    The imformation contains the amount credited/debited . The data is used change balance and append transaction
    and return new values of stores keys.

    'messages' : Inbuilt event to recieve and send messages through websockets.

    'json' :  Inbuilt event to recieve and send data in json format through websockets.

Endpoints: 
    '/': This endpoint serves html response where we can interact with the webpage. 
    
    # These endpoints are just to test our nosql store

    '/money': 
        request type = POST
        data format = Json
        ex: {
                'amount' : '10',
            }
    '/transaction': 
        request type = POST
        data format = Json
        ex: {
                'address' : 'gurgaon',
                'mobile' : '93048302984'
            }


Firebase : (Nosql store)
    store : Contains all the data in the store.
    get() : Method to get data for a specific key from staore.
    set() : Method to update data for a specific key in the store and communicate changes to the clients. 