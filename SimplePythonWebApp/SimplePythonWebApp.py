from flask import Flask
from random import randint
import socket

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return '<h3>Hello from ' + name + '</h3><br>Your number of the day is: ' + '<h1>' +str(randint(1, 101)) + '</h1><br>The hostname is: ' + socket.gethostname()

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)