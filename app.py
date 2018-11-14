from flask import Flask, render_template
import subprocess
from dbclass import db

app = Flask(__name__)


def search_subnet(subnet):
    output = subprocess.Popen(["nmap", "-sP", "166.200.{}.*".format(subnet)])




@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
