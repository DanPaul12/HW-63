from models.schemas import production_schema, productions_schema
from services import productionService
from flask import request

def save():
    new_production = production_schema.load(request.json)
    save_production = productionService.save(new_production)
    return production_schema.jsonify(save_production), 201

def find_all():
    productions = productionService.find_all()
    return productions_schema.jsonify(productions), 200