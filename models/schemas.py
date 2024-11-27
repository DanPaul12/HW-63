from marshmallow import fields, validate
from schema import ma

class CustomerSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)

    class Meta:
        fields = ('id', 'name', 'email', 'phone' )

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many = True)

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True, validate=validate.Length(min=1))
    price = fields.String(required=True, validate=validate.Range(min=0))

class ProductSchemaID(ma.Schema):
    id = fields.Integer(required=True)


product_schema = ProductSchema()
products_schema = ProductSchema(many = True)