from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('client_message')
def receive_message(client_msg):
    emit('server_message', client_msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)