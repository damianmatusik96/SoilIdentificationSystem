from flask import Flask
from WebAppBackend.controller.FileController import home_blue

app = Flask(__name__)
app.register_blueprint(home_blue)
