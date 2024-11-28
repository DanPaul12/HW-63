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

def find_all_pagination():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return orders_schema.jsonify(orderService.find_all_pagination(page=page, per_page=per_page))