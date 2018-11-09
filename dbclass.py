import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCEHMY_TRACK-MODIFICATION'] = False

db = SQLAlchemy(app)


class Ips(db.Model):
    ip = db.column(db.Text, primary_key=True)
    hostname = db.column(db.Text)
    timestamp = db.column(db.Time(timezone=False))

    def __init__(self, ip, hostname, timestamp):
        self.ip = ip
        self.hostname = hostname
        self.timestamp = timestamp

    def __repr__(self):
        return "IP: {}".format(self.ip)