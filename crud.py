from dbclass import Ips, db, Notes
import datetime

db.create_all()


def create(ips,  hostname, timestamp, ucinet, building, room):
    for ip in ips:
        db.session.add(Ips(ip, hostname, timestamp, ucinet, building, room))
    db.session.commit()


def read(subnet):
    ips = Ips.query.filer_by(subnet=subnet)
    print(ips)


def update_time(ip, timestamp):
    record = Ips.query.filer(ip=ip)
    record.timestamp = timestamp
    db.session.add(record)
    db.session.commit()


def update_hostname(ip, hostname):
    record = Ips.query.filer(ip=ip)
    record.hostname = hostname
    db.session.add(record)
    db.session.commit()


def read_notes():
    ips = Ips.query()
    print(ips)


def add_note(note):
    db.session.add(Notes(datetime.datetime.now().strftime("%y-%m-%d %H:%M"), note))
    db.session.commit()


