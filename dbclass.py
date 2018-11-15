import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCEHMY_TRACK-MODIFICATION'] = False

db = SQLAlchemy(app)


class Ips(db.Model):
    ip = db.Column(db.Text, primary_key=True)
    hostname = db.Column(db.Text)
    prev_hostname = db.Column(db.Text)
    timestamp = db.Column(db.Time(timezone=False))
    ucinet = db.Column(db.Text)
    building = db.Column(db.Text)
    room_num = db.Column(db.Integer, default=0)

    def __init__(self, ip, hostname, timestamp, ucinet, building, room, progress):
        self.ip = ip
        self.hostname = hostname
        self.prev_hostname = hostname
        self.timestamp = timestamp
        self.ucinet = ucinet
        self.building_num = building
        self.room_num = room
        self.progress = progress

    def __repr__(self):
        return "IP: {}".format(self.ip)


class Notes(db.Model):
    date = db.Column(db.Date, primary_key=True)
    notes = db.Column(db.Text)

    def __init__(self, date, notes):
        self.date = date
        self.notes = notes

    def __str__(self):
        return "{}: {}".format(self.date, self.notes)
