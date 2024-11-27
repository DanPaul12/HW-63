from flask import Flask
from models.models import db
from routes.customerBP import customer_blueprint
from routes.productBP import product_blueprint
from routes.employeeBP import employee_blueprint
from schema import ma


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)

    return app

def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(employee_blueprint, url_prefix='/employees')



if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blue_print_config(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=True)