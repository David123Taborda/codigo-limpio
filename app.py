from flask import Flask, render_template
from src.routes.calculadora_routes import calculadora_bp
from src.routes.database_routes import database_bp
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev_secret_key_change_in_production')

# Registrar Blueprints
app.register_blueprint(calculadora_bp)
app.register_blueprint(database_bp)

@app.route('/')
def index():
    """Página de inicio con menú principal"""
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
