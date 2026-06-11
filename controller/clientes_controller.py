from flask import Blueprint, render_template, request, redirect, url_for, flash
from model.clientes_model import db, Cliente
from sqlalchemy.exc import IntegrityError

cliente_blueprint = Blueprint('cliente', __name__)

@cliente_blueprint.route('/')
def listar_clientes():
    # Pega o termo de busca que vem da URL (ex: /?search=Analice)
    termo_busca = request.args.get('search', '')

    if termo_busca:
        # Busca clientes onde o nome OU o email contenham o termo digitado
        # O .like() com os '%' funciona como o "contém" do SQL
        clientes = Cliente.query.filter(
            (Cliente.nome.like(f'%{termo_busca}%')) | 
            (Cliente.telefone.like(f'%{termo_busca}%'))
        ).all()
    else:
        # Se não houver busca, traz todo mundo
        clientes = Cliente.query.all()

    return render_template('index.html', clientes=clientes, busca=termo_busca)

'''@cliente_blueprint.route('/')
def index():
    # Retorna a View (HTML)
    return render_template('cadastro.html')'''

@cliente_blueprint.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_cliente():
    # Coleta dados da View
    
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
        except IntegrityError:
            db.session.rollback()
            flash("Erro: CPF ou CNPJ já cadastrado (RN01).", "error")
        
        return redirect(url_for('cliente.listar_clientes'))
    
    return render_template('cadastro.html')

@cliente_blueprint.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    # 1. Busca o cliente pelo ID no banco
    cliente = db.session.get(Cliente, id) 

    if request.method == 'POST':
        # 2. Pega os dados vindos do formulário
        cliente.nome = request.form['nome']
        cliente.email = request.form['email']
        cliente.telefone = request.form['telefone']
        cliente.cep = request.form['cep'] # Se tiver esse campo no seu Model

        # 3. Salva as alterações
        db.session.commit()
        return redirect(url_for('cliente.listar_clientes')) # Redireciona para a lista

    # Se for GET, exibe a página de edição com os dados atuais
    return render_template('editar_cliente.html', cliente=cliente)