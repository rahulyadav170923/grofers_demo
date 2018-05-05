import os
# putting configuring options here
secret_key = os.environ['secret']
port = int(os.environ.get('PORT', 5000))