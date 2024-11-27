from flask import Blueprint
from controllers.customerController import save, find_all
from controllers.productController import save

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)


product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(save)
