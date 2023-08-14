from app import create_app, db
from app.models.milk import Milk

my_app = create_app()
with my_app.app_context():
    db.session.add(Milk(id=2, timestamp="Wed, 09 Aug 2023 19:29:38 GMT", amount='1.0', container='Freezer', type='milk', cad='180'))
    db.session.add(Milk(id=3, timestamp="Sun, 30 Jul 2023 02:47:21 GMT", amount='1.0', container='Freezer', type='milk', cad='3'))
    db.session.add(Milk(id=4, timestamp="Mon, 26 Dec 2022 15:54:10 GMT", amount='1.0', container='Freezer', type='milk', cad='180'))
    db.session.add(Milk(id=5, timestamp="Thu, 27 Apr 2023 08:10:44 GMT", amount='1.0', container='Freezer', type='milk', cad='1'))
    db.session.add(Milk(id=6, timestamp="Sun, 11 Jun 2023 11:01:32 GMT", amount='1.0', container='Freezer', type='milk', cad='1'))
    db.session.add(Milk(id=7, timestamp="Wed, 07 Jun 2023 22:33:05 GMT", amount='1.0', container='Freezer', type='milk', cad='3'))
    db.session.add(Milk(id=8, timestamp="Wed, 09 Aug 2023 19:29:38 GMT", amount='1.0', container='Freezer', type='milk', cad='180'))
    db.session.add(Milk(id=9, timestamp="Sun, 30 Jul 2023 02:47:21 GMT", amount='1.0', container='Freezer', type='milk', cad='180'))
    db.session.add(Milk(id=10, timestamp="Mon, 26 Dec 2022 15:54:10 GMT", amount='1.0', container='Freezer', type='milk', cad='180'))
    db.session.add(Milk(id=11, timestamp="Thu, 27 Apr 2023 08:10:44 GMT", amount='1.0', container='Freezer', type='milk', cad='180'))
    db.session.add(Milk(id=12, timestamp="Sun, 11 Jun 2023 11:01:32 GMT", amount='1.0', container='Freezer', type='milk', cad='180'))
    db.session.add(Milk(id=13, timestamp="Wed, 07 Jun 2023 22:33:05 GMT", amount='1.0', container='Freezer', type='milk', cad='180'))
    db.session.commit()