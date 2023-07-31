from app import create_app, db
from app.models.milk import Milk

my_app = create_app()
with my_app.app_context():
    db.session.add(Milk(id=1, timestamp="2021-11-13T22:49:06+00:00", amount='0.0', container='freezer', type='colostrum', cad='180'))
    db.session.add(Milk(id=2, timestamp="2021-12-13T22:49:06+00:00", amount='1.0', container='freezer', type='milk', cad='180'))
    db.session.add(Milk(id=3, timestamp="2021-12-15T22:49:06+00:00", amount='2.0', container='freezer', type='milk', cad='180'))
    db.session.add(Milk(id=4, timestamp="2021-12-16T23:49:06+00:00", amount='3.0', container='freezer', type='milk', cad='180'))
    db.session.add(Milk(id=5, timestamp="2021-12-17T22:30:06+00:00", amount='4.5', container='freezer', type='milk', cad='180'))
    db.session.commit()