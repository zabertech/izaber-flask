#!/usr/bin/python

from izaber import initialize
from izaber.flask import app

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    initialize('example')
    print "Running"
    app.run()


