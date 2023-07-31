from app import db


class Milk(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime)
    amount = db.Column(db.Float)
    container = db.Column(db.String)
    type = db.Column(db.String)
    cad = db.Column(db.Integer)

    @classmethod 
    def dict_to_model(cls, data_dict):
        return cls(timestamp = data_dict["timestamp"],
                amount = data_dict["amount"],
                container = data_dict["container"],
                type = data_dict["type"],
                cad = data_dict["cad"])

    def make_milk_dict(self):
        return dict(
            id=self.id,
            timestamp=self.timestamp,
            amount=self.amount,
            container=self.container,
            type=self.type,
            cad=self.cad
        )