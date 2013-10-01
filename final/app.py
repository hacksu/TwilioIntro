from flask import Flask
from twilio import twiml
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World, my webserver is working! :)</h1>'

@app.route('/sms', methods=['POST'])
def sms():
    r = twiml.Response()
    r.sms("hello :)")
    return str(r)

@app.route('/talk', methods=['POST'])
def talk():
    r = twiml.Response()
    r.say('Hello Brian, you are the man!')
    return str(r)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
