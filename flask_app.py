
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/home')
def home():
    return render_template('index.html',title='자동견적')

@app.route('/t2')
def t2():
    return render_template('3tAcr.html',title='3t 아크릴')
