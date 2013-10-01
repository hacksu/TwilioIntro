from flask import Flask
from twilio import twiml
import os

app = Flask(__name__)

# routes go here :)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
