from services import customerService
from models.schemas import customer_schema, customers_schema
from marshmallow import ValidationError
from flask import request, jsonify

def save():
    try:
        new_customer = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 404
    
    customer_save = customerService.save(new_customer)
    if customer_save is not None:
        return customer_schema.jsonify(customer_save), 201
    else:
        return jsonify({'message':'fallback triggered'}, {'body':new_customer}), 400
    
    
def find_all():
    customers = customerService.find_all()
    return customers_schema.jsonify(customers), 200
