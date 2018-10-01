import logging
import json

from flask import request
from flask_restplus import Resource
from service_api.api.v1.serializers import (sample_request, sample_response,
      sample_del_request)
from service_api.api.restplus import api

from service_api.api.v1.dboperation import (add_order, delete_order,
      get_all_order)

log = logging.getLogger(__name__)

ns = api.namespace('orderApi',
                   description='Add or remove order')

@ns.route('/orderApi')
class OrderInventory(Resource):
   '''Shows a list of all options, and lets you operate'''

   @ns.marshal_with(sample_response)
   def get(self):
      '''Get all orders'''
      orderList = get_all_order()
      return orderList

   @ns.expect(sample_request)
   @ns.marshal_with(sample_response)
   def post(self):
      '''Add order'''
      data = request.json
      orderObject = add_order(data["orderName"])
      return orderObject, 201

   @ns.expect(sample_del_request)
   @ns.response(204, 'order successfully deleted.')
   def delete(self):
      '''Delete an order'''
      data = request.json
      delete_order(data["orderId"])
      return None, 204
