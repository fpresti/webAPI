from flask import Blueprint

tools_bp = Blueprint('tools_bp', __name__, url_prefix='/tools')

@tools_bp.route("/ping")
def ping():
    return "ping"

@tools_bp.route("/getRandomKey")
def get_random_key():
    import os
    #generates a random key
    return os.urandom(24).hex()