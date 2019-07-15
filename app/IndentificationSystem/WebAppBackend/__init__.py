from flask import Flask
from WebAppBackend.controller.FileController import home_blue
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(home_blue)
CORS(app)
