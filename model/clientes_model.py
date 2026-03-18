from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False) # RN02
    cpf = db.Column(db.String(14), unique=True, nullable=False) # RN01/RN02
    cnpj = db.Column(db.String(18), unique=True, nullable=False) # RN01/RN02
    email = db.Column(db.String(100), nullable=True)
    telefone = db.Column(db.String(20), nullable=False) # RN02
    cep = db.Column(db.String(10), nullable=True)