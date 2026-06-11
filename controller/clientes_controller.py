from flask import Blueprint, render_template, request, redirect, url_for, flash
from model.clientes_model import db, Cliente
from sqlalchemy.exc import IntegrityError

cliente_blueprint = Blueprint('cliente', __name__)

@cliente_blueprint.route('/')
def listar_clientes():
    termo_busca = request.args.get('search', '')

    if termo_busca:
        clientes = Cliente.query.filter(
            (Cliente.nome.like(f'%{termo_busca}%')) | 
            (Cliente.telefone.like(f'%{termo_busca}%'))
        ).all()
    else:
        clientes = Cliente.query.all()

    return render_template('index.html', clientes=clientes, busca=termo_busca)


@cliente_blueprint.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
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
            return redirect(url_for('cliente.listar_clientes'))
        except IntegrityError:
            db.session.rollback()
            flash("Erro: CPF ou CNPJ já cadastrado (RN01).", "error")
            return render_template('cadastro.html')
    
    return render_template('cadastro.html')


@cliente_blueprint.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = db.session.get(Cliente, id) 

    if request.method == 'POST':
        cliente.nome = request.form.get('nome')
        cliente.email = request.form.get('email')
        cliente.telefone = request.form.get('telefone')
        cliente.cep = request.form.get('cep') 

        db.session.commit()
        return redirect(url_for('cliente.listar_clientes')) 

    return render_template('editar_cliente.html', cliente=cliente)