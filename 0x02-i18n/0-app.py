#!/usr/bin/env python3

"""Import Modules"""

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    """create a python app"""
    return render_template('index.html')

if __name__ == '__main__':
    """main"""
    app.run(debug=True)
