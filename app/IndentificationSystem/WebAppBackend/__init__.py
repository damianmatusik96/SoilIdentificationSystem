from flask import Flask
from WebAppBackend.controller.FileController import home_blue
from flask_cors import CORS
from app.IndentificationSystem.DataController import main_blue

app = Flask(__name__)

app.register_blueprint(home_blue)
app.register_blueprint(main_blue)

CORS(app)
