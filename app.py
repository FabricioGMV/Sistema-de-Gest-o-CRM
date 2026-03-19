from flask import Flask
from model.clientes_model import db
from controller.clientes_controller import cliente_blueprint

app = Flask(__name__)
app.secret_key = "chave_mestra"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Teste%40123@localhost/crm_faculdade'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(cliente_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)