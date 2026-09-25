import os
from flask import Flask, render_template
from dotenv import load_dotenv
from extensions import db

# Cargar variables de entorno
load_dotenv('/home/RichiCruz21/catalogo_seguro/.env')

app = Flask(__name__)

# Configuración
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar base de datos
db.init_app(app)

# Importar modelos DESPUÉS de inicializar db
from models import Equipo

# Ruta principal
@app.route('/')
@app.route('/catalogo')
def catalogo():
    equipos = Equipo.query.filter_by(disponible=True).all()
    return render_template('catalogo.html', equipos=equipos)

if __name__ == '__main__':
    app.run(debug=False)

