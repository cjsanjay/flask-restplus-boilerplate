from flask_restplus import fields
from service_api.api.restplus import api

sample_request = api.model('Add order', {
    'orderName': fields.String(required=False,
                                description='Order Name')
})

sample_del_request = api.model('delete order', {
    'orderId': fields.Integer(required=False,
                              description='Order Id')
})

sample_response = api.model('response', {
    'orderId': fields.Integer(required=False,
                              description='Order ID'),
    'orderName': fields.String(required=False,
                             description='Order Name')
})
