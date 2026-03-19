from flask import Blueprint, render_template, request, redirect, url_for, flash
from model.clientes_model import db, Cliente
from sqlalchemy.exc import IntegrityError

cliente_blueprint = Blueprint('cliente', __name__)

@cliente_blueprint.route('/')
def index():
    return render_template('cadastro.html')

@cliente_blueprint.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.form
    novo_cliente = Cliente(
        nome=dados.get('nome'),
        cpf=dados.get('cpf'),
        cnpj=dados.get('cnpj'),
        telefone=dados.get('telefone'),
        email=dados.get('email'),
        cep=dados.get('cep')
    )

    try:
        db.session.add(novo_cliente)
        db.session.commit()
        flash("Cliente cadastrado com sucesso!", "success")
    except IntegrityError:
        db.session.rollback()
        flash("Erro: CPF ou CNPJ já cadastrado.", "error")
    
    return redirect(url_for('cliente.index'))