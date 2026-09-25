import os
import json
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv('/home/RichiCruz21/catalogo_seguro/.env')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

def cargar_equipos():
    ruta_json = os.path.join(os.path.dirname(__file__), 'equipos.json')
    with open(ruta_json, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
@app.route('/catalogo')
def catalogo():
    equipos = cargar_equipos()
    equipos_disponibles = [e for e in equipos if e.get('disponible', True)]
    return render_template('catalogo.html', equipos=equipos_disponibles)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)