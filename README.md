# Sistema-de-Gest-o-CRM🚀 Sistema de Gestão CRM - Projeto Acadêmico
Este é um sistema de Gestão de Relacionamento com o Cliente (CRM) desenvolvido para facilitar o controle de contatos e endereços. O projeto foi construído com foco em arquitetura MVC (Model-View-Controller) utilizando Python e SQL Server.

🛠️ Tecnologias e Ferramentas
Linguagem: Python 3.13

Framework Web: Flask

Banco de Dados: Microsoft SQL Server (Express Edition)

Persistência de Dados: Flask-SQLAlchemy (ORM)

Conectividade: PyODBC

Interface: HTML5, CSS3 (Modern UI) e FontAwesome Icons

📋 Pré-requisitos
Antes de iniciar, você precisará ter instalado em sua máquina:

Python 3.10 ou superior.

Microsoft SQL Server (Instância Express recomendada).

ODBC Driver 17 for SQL Server (Essencial para a comunicação do Python com o banco).

🔧 Guia de Instalação e Execução
1. Clonar o Repositório
Bash
git clone https://github.com/seu-usuario/Sistema-de-Gest-o-CRM.git
cd Sistema-de-Gest-o-CRM
2. Configurar o Ambiente Virtual (venv)
Bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente (Windows)
.\venv\Scripts\activate
3. Instalar Dependências
Bash
pip install -r requirements.txt
4. Configuração Automática do Banco de Dados
Para evitar configurações manuais complexas, execute o script de automação que criará o banco crm_faculdade e as tabelas necessárias:

Bash
python setup_banco.py
5. Ajuste de Conexão (Importante)
No arquivo app.py, verifique a linha da SQLALCHEMY_DATABASE_URI. Caso sua instância do SQL Server não seja a padrão, ajuste conforme necessário:

Python
# Exemplo para instância SQLEXPRESS01
app.config['SQLALCHEMY_DATABASE_URI'] = r'mssql+pyodbc://.\SQLEXPRESS01/crm_faculdade?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes&Encrypt=no&TrustServerCertificate=yes'
6. Rodar a Aplicação
Bash
python app.py
Acesse no seu navegador: http://127.0.0.1:5000

💡 Funcionalidades Implementadas
Dashboard Principal: Listagem de clientes com design responsivo.

Busca Dinâmica: Filtro por nome ou e-mail diretamente no banco de dados.

Cadastro de Clientes: Formulário intuitivo com validação de campos.

Edição de Dados: Atualização rápida de informações de contato e endereço.

⚠️ Solução de Problemas (Troubleshooting)
Se encontrar o erro pyodbc.OperationalError (Erro 08001):

Abra o SQL Server Configuration Manager.

Vá em Configuração de Rede do SQL Server > Protocolos para [SuaInstancia].

Certifique-se de que o TCP/IP está como Habilitado.

Reinicie o serviço do SQL Server e tente novamente.

📂 Estrutura de Pastas
Plaintext
/
├── controller/          # Lógica de rotas (Blueprints)
├── model/               # Modelos do Banco de Dados (SQLAlchemy)
├── templates/           # Páginas HTML (Jinja2)
├── venv/                # Ambiente virtual (desconsiderado pelo .gitignore)
├── app.py               # Arquivo principal de inicialização
├── setup_banco.py       # Script de automação do banco
└── requirements.txt     # Lista de dependências do projeto