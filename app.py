from flask import *
import pyqrcode
app = Flask(__name__)
def qrcode(string):
    string=pyqrcode.create(string)
    data=string.terminal(quiet_zone=1)
    return data
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<path:string>')
def code(string):
    return qrcode(string)
if __name__=='__main__':
    app.run()
