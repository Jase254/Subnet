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
    ucinet = db.column(db.Text)
    building_num = db.column(db.Integer, default=0)
    room_num = db.column(db.Integer, default=0)

    def __init__(self, ip, hostname, timestamp, ucinet, building, room):
        self.ip = ip
        self.hostname = hostname
        self.timestamp = timestamp
        self.ucinet = ucinet
        self.building_num = building
        self.room_num = room

    def __repr__(self):
        return "IP: {}".format(self.ip)


class Notes(db.Model):
    date = db.column(db.Date, primary_key=True)
    notes = db.column(db.Text)

    def __init__(self, date, notes):
        self.date = date
        self.notes = notes

    def __str__(self):
        return "{}: {}".format(self.date, self.notes)
