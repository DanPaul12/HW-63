from services import productService
from models.schemas import product_schema
from marshmallow import ValidationError
from flask import request, jsonify

def save():
    try:
        product = product_schema.load(request.json)
    except ValidationError:
        pass

    product_save = productService.save(product)
    if product_save is not None:
        return jsonify(product_save), 201
    else:
        return jsonify('error')
