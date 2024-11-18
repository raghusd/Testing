from flask import Flask, render_template
import templates.dbconnection
from django.shortcuts import render
import requests

#Create a Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')


# Home page
@app.route('/')
def home():
        return render_template('home.html')


# Connection page
@app.route('/connection')
def connection():
        return render_template('connection.html')


# DB Connection Page
@app.route('/db')
def db():
        return render_template('db.html')

if __name__ == '__main__':
        app.run(debug=True)
