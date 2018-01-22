from flask import Flask
from subprocess import Popen, PIPE


pipe = Popen(["cat", "/etc/hostname"], stdout=PIPE)
text = pipe.communicate()[0]

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! " + text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
