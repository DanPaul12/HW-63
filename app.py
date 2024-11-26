from flask import Flask
from models.models import db
from routes.routes import customer_blueprint
from schema import ma




def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)

def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blue_print_config(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=True)