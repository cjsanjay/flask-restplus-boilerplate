from datetime import datetime

from service_api.database import db


class OrderRecord(db.Model):
    orderId = db.Column(db.Integer, primary_key=True)
    orderName = db.Column(db.String(50))

    def __init__(self, orderName):
        self.orderName = orderName

    def __repr__(self):
        return '<Order Details Name %r ID %r>' % (str(self.orderName), self.orderId)
