from model.clientes_model import db


class HistoricoCliente(db.Model):
    __tablename__ = 'historico_clientes'

    id         = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    texto      = db.Column(db.String(500), nullable=False)
    data       = db.Column(db.Date, nullable=False)

    cliente = db.relationship('Cliente', backref='historico', lazy=True)