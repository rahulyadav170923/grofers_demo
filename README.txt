Installation Steps : 

    cd grofers_demo
    Install [Virtualenv](https://virtualenv.pypa.io/en/stable/)
    virtualenv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

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

