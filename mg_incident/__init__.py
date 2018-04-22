from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# # from flask_security import (
# #     Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
# # )

from flask_admin import Admin


db = SQLAlchemy()
admin = Admin(name='MG Incidents', url='/')
migrate = Migrate()


def create_app(config_name='development'):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.default')
    app.config.from_pyfile('config.py')
    config_obj_name = "config.{}".format(config_name)
    # TODO: ImportError
    app.config.from_object(config_obj_name)

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    from mg_incident.account.core import bp as bp_account
    app.register_blueprint(bp_account, url_prefix='/account')

    return app
