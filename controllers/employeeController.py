from models.schemas import employee_schema
from models.models import Employee
from services import employeeService
from flask import request, jsonify

def save():
    new_employee = employee_schema.load(request.json)
    save_employee = employeeService.save(new_employee)
    return employee_schema.jsonify(save_employee), 201

#best way to do error handling here and why

def find_all():
    employees = employeeService.find_all()
    return employee_schema.jsonify(employees), 200



#why useful to distinguish controllers from services?