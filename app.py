from flask import Flask
from models.models import db




def create_app(config_name):
    app = Flask(__name__)


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blue_print_config(app)
    configure_rate_limit()

    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=True)