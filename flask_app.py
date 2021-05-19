
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template

app = Flask(__name__,static_url_path='/templates/')

@app.route('/t1')
def t1():
    return render_template('3tAcr.html',title='a')
@app.route('/t2')
def t2():
    return render_template('3tAcr.html',title='b')
@app.route('/t3')
def t3():
    return render_template('3tAcr.html',title='c')
@app.route('/t4')
def t4():
    return render_template('3tAcr.html',title='d')
@app.route('/t5')
def t5():
    return render_template('3tAcr.html',title='e')

if __name__ == '__main__':
    app.run()
