from flask import Flask
from model.clientes_model import db
from controller.clientes_controller import cliente_blueprint

app = Flask(__name__)
app.secret_key = "chave_mestra"

# 1. Configuração de conexão com o SQL Server
app.config['SQLALCHEMY_DATABASE_URI'] = r'mssql+pyodbc://.\SQLEXPRESS01/crm_faculdade?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes&Encrypt=no&TrustServerCertificate=yes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

# 2. Configuração de conexão com o MySQL
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Teste%40123@localhost/crm_faculdade'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy (ORM)
db.init_app(app)

# Registra as rotas do Controller
app.register_blueprint(cliente_blueprint)

# Garante que a tabela seja criada no banco ao rodar o arquivo
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)