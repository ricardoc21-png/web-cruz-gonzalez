import os
import json
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv('/home/RichiCruz21/catalogo_seguro/.env')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

# Función para cargar datos desde JSON
def cargar_json(archivo):
    ruta = os.path.join(os.path.dirname(__file__), archivo)
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

# RUTAS
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/equipos')
@app.route('/catalogo')
def equipos():
    datos = cargar_json('equipos.json')
    disponibles = [e for e in datos if e.get('disponible', True)]
    return render_template('catalogo.html', equipos=disponibles, titulo='Equipos')

@app.route('/repuestos')
def repuestos():
    datos = cargar_json('repuestos.json')
    disponibles = [e for e in datos if e.get('disponible', True)]
    return render_template('repuestos.html', repuestos=disponibles)

@app.route('/servicios')
def servicios():
    datos = cargar_json('servicios.json')
    return render_template('servicios.html', servicios=datos)

@app.route('/software')
def software():
    datos = cargar_json('software.json')
    disponibles = [e for e in datos if e.get('disponible', True)]
    return render_template('software.html', software=disponibles)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
