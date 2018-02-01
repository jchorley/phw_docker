from flask import Flask, render_template
from subprocess import Popen, PIPE
from flask_socketio import SocketIO


pipe = Popen(["cat", "/etc/hostname"], stdout=PIPE)
hostname = pipe.communicate()[0]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gotocats'
socketio = SocketIO(app)

@app.route("/")
def hello():
    return render_template('hello.html', container = hostname)



if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
    # app.run(debug=True, host='0.0.0.0')
