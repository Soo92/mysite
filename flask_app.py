
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template

app = Flask(__name__,static_url_path='/templates/')

@app.route('/t2')
def t2():
    return render_template('3tAcr.html',title='견적미리보기')

if __name__ == '__main__':
    app.run()
