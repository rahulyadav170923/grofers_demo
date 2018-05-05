import os
# putting configuring options here
secret_key = os.environ['secret']
try:
    port = os.environ['PORT']
except KeyError:
    port = 3000