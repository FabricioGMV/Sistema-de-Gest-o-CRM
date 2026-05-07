from datetime import date
from model.clientes_model import db


class TipoServico(db.Model):
    __tablename__ = 'tipos_servico'

    id         = db.Column(db.Integer, primary_key=True)
    nome       = db.Column(db.String(100), nullable=False)
    prazo_dias = db.Column(db.Integer, nullable=False)   # RN06 - base para cálculo do vencimento
    descricao  = db.Column(db.String(300), nullable=True)

    servicos = db.relationship('ServicoCliente', backref='tipo', lazy=True)


class ServicoCliente(db.Model):
    __tablename__ = 'servicos_cliente'

    id              = db.Column(db.Integer, primary_key=True)
    cliente_id      = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    tipo_servico_id = db.Column(db.Integer, db.ForeignKey('tipos_servico.id'), nullable=False)
    data_execucao   = db.Column(db.Date, nullable=False)
    data_vencimento = db.Column(db.Date, nullable=False)  # Calculado pelo back-end (RN06)
    status          = db.Column(db.String(20), default='Ativo')  # Ativo / Renovado / Concluido

    cliente = db.relationship('Cliente', backref='servicos', lazy=True)

    @property
    def dias_para_vencer(self):
        return (self.data_vencimento - date.today()).days

    @property
    def situacao(self):
        d = self.dias_para_vencer
        if d < 0:       return 'vencido'
        if d <= 7:      return 'critico'
        if d <= 30:     return 'a_vencer'   # RN08
        return 'ok'
