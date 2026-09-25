from app import db
from datetime import datetime

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    especificaciones = db.Column(db.Text, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    imagen_url = db.Column(db.String(200), nullable=True)
    disponible = db.Column(db.Boolean, default=True)
    fecha_ingreso = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Equipo {self.marca} {self.modelo}>'
