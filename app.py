import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Cargar variables de entorno con ruta absoluta
load_dotenv('/home/RichiCruz21/catalogo_seguro/.env')

app = Flask(__name__)

# Configuración
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar base de datos
db = SQLAlchemy(app)

# Importar modelos
from models import Equipo

# Ruta principal - Catálogo público
@app.route('/')
@app.route('/catalogo')
def catalogo():
    equipos = Equipo.query.filter_by(disponible=True).all()
    return render_template('catalogo.html', equipos=equipos)

if __name__ == '__main__':
    app.run(debug=False)
