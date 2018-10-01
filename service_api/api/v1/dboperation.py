from service_api.database import db
from service_api.database.models import OrderRecord

def add_order(orderName):
    orderObject = OrderRecord(orderName)
    db.session.add(orderObject)
    db.session.commit()
    return orderObject

def delete_order(orderId):
   orderObject = OrderRecord.query.filter(OrderRecord.orderId == orderId).one()
   db.session.delete(orderObject)
   db.session.commit()

def get_all_order():
   orderRecords = OrderRecord.query.all()
   return orderRecords
