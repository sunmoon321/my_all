from httplib import error

from flask import Flask
from flask.templating import render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<div style="font-size:60px">Hello World!</div>'

@app.route('/foo')
def foo():
    return render_template("foo.html",error=error)

if __name__ == '__main__':
    app.run(debug=True)
