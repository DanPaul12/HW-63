from marshmallow import fields, validate
from schema import ma

class CustomerSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)

    class Meta:
        fields = ('id', 'name', 'email', 'phone' )       #what is this for

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many = True)

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    price = fields.String(required=True)

class ProductSchemaID(ma.Schema):
    id = fields.Integer(required=True)


product_schema = ProductSchema()
products_schema = ProductSchema(many = True)

class EmployeeSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    position = fields.String(required=True)

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    total_price = fields.String(required=True)

order_schema = OrderSchema()
orders_schema = OrderSchema(many = True)

class ProductionSchema(ma.Schema):
    id = fields.Integer(required=False)
    product_id = fields.Integer(required=True)
    quantity_produced = fields.Integer(required=True)
    date_produced = fields.Date(required=True)

production_schema =ProductionSchema()
productions_schema =ProductionSchema(many = True)