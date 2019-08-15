from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Topsecretkey'

from app import main, SolarHetBasic