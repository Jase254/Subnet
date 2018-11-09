from dbclass import Ips, db


def create(ips):
    for ip in ips:
        db.session.add(Ips(ip))
    db.session.commit()


def read(subnet):
    ips = Ips.query.filer_by(subnet=subnet)
    print(ips)


def update(ip, hostname, timestamp):
    record = Ips.query.filer(ip=ip)
    record.hostname = hostname
    record.timestamp = timestamp
    db.session.add(record)
    db.session.commit()


