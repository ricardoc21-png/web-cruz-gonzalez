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

# Importar modelos
from models import Equipo

# Crear tablas automáticamente al iniciar
with app.app_context():
    db.create_all()
    print("✅ Tablas de base de datos creadas/verificadas")

# Ruta principal
@app.route('/')
@app.route('/catalogo')
def catalogo():
    equipos = Equipo.query.filter_by(disponible=True).all()
    return render_template('catalogo.html', equipos=equipos)

if __name__ == '__main__':
    app.run(debug=False)
# Agregar equipos de prueba si la base de datos está vacía
with app.app_context():
    if Equipo.query.count() == 0:
        equipos_prueba = [
            Equipo(marca='Lenovo', modelo='ThinkPad T480', especificaciones='Intel Core i5, 16GB RAM, 512GB SSD', precio=850000, imagen_url='https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=400', disponible=True),
            Equipo(marca='Dell', modelo='Latitude 7490', especificaciones='Intel Core i7, 16GB RAM, 256GB SSD', precio=950000, imagen_url='https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=400', disponible=True),
            Equipo(marca='HP', modelo='EliteBook 840 G5', especificaciones='Intel Core i5, 8GB RAM, 256GB SSD', precio=750000, imagen_url='https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=400', disponible=True),
        ]
        db.session.add_all(equipos_prueba)
        db.session.commit()
        print(f"✅ {len(equipos_prueba)} equipos de prueba agregados")