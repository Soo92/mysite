
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template
import pandas as pd
import templates.static.f_key as ff
import sys

for p in sys.path:
    print( p )

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

@app.route('/admin')
def admin():
    html_all = pd.read_csv("templates/static/keyw.csv", engine='python').to_html(table_id = "csv_table",classes="display compact")
    html_add = pd.read_csv("templates/static/my.csv", engine='python').to_html(table_id = "add_table",classes="display compact")
    html_del = pd.read_csv("templates/static/del.csv", engine='python').to_html(table_id = "del_table",classes="display compact")
    return render_template('ad_1.html',data_key=html_all,data_add=html_add,data_del=html_del)

@app.route('/reload')
def reload():
    ff.reload()
    return "hello"

if __name__ == '__main__':
    app.run()
