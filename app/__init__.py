from flask import Flask
import secrets

def load_routes():
    from . import routes
    

app = Flask(__name__)
app.secret_key = "ee651a2b053f2d7387efe6361d0d05df5195b89d6bd0e526239d0dbe1f80aade6"


load_routes()