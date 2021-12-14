from flask import Flask
from flask import json
from flask import jsonify
from flask import request
from flask import render_template
from flask import render_template_string
app=Flask(__name__)
@app.route('/')
def home ():
    return render_template('home.html')
@app.route('/about')
def about ():
    return render_template('about.html')
if __name__== '__main__':
  app.run(debug=True)