from services import productService
from models.schemas import product_schema, products_schema
from marshmallow import ValidationError
from flask import request, jsonify

def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    try:
        product_save = productService.save(product_data)
        return product_schema.jsonify(product_save), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

def find_all():
    products = productService.find_all()
    return products_schema.jsonify(products), 200
