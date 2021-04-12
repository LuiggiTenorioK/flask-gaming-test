from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.login_controller import api as login_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Gaming project',
          version='1.0',
          description='gaming test web service'
          )

api.add_namespace(user_ns, path='/api/users')
api.add_namespace(login_ns, path='/api/login')