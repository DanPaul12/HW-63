from services import orderService
from models.schemas import order_schema, orders_schema
from flask import request, jsonify

def save():
    new_order= order_schema.load(request.json)
    save_order = orderService.save(new_order)
    return order_schema.jsonify(save_order), 201

def find_all():
    orders = orderService.find_all()
    return orders_schema.jsonify(orders), 200