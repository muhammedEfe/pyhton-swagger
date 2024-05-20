import sys
import os

# app dizininin mutlak yolunu hesaplayın
app_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
services_path = os.path.join(app_dir, "services")
models_path = os.path.join(app_dir, "models")
elasticsearch_path = os.path.join(app_dir, "elasticsearch")
database_path = os.path.join(app_dir, "database")
api_path = os.path.join(app_dir, "api")
sys.path.append(services_path)
sys.path.append(models_path)
sys.path.append(elasticsearch_path)
sys.path.append(database_path)
sys.path.append(api_path)

from flask import Flask
from flask_restx import Api
from api.controllers.product_controller import ns as product_ns
from scheduler.job_scheduler import scheduler

app = Flask(__name__)
api = Api(app, doc='/swagger/', version='1.0', title='Rival Analysis API',
          description='A simple API for rival analysis')

api.add_namespace(product_ns)

if __name__ == '__main__':
    app.run(debug=True)





