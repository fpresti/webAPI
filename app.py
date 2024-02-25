from flask import Flask
from api.user.user_controller import user_bp
from api.tools.tools_controller import tools_bp
from api.ia.ia_controller import ia_bp
app = Flask(__name__)

app.secret_key = '84a563b7b53c97a9f996dd843330f522809497e5bb8801ca'

# Registrar el blueprint del controlador de inicio de sesión
app.register_blueprint(user_bp)
app.register_blueprint(tools_bp)
app.register_blueprint(ia_bp)

@app.route('/')
def index():
    return 'Welcome to PrestiCoding webAPI!'

if __name__ == '__main__':
    app.run(debug=True)