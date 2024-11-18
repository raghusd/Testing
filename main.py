from flask import Flask, render_template

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


if __name__ == '__main__':
        app.run(debug=True)
