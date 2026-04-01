import pyodbc

# Lista de instâncias comuns para tentar conexão
instancias = [r'.\SQLEXPRESS', r'.\SQLEXPRESS01', r'localhost', r'(local)']
sucesso = False

for instancia in instancias:
    conn_str = (
        f'Driver={{ODBC Driver 17 for SQL Server}};'
        f'Server={instancia};'
        f'Database=master;'
        f'Trusted_Connection=yes;'
    )
    try:
        # Tenta conectar com um timeout curto (3 segundos)
        conn = pyodbc.connect(conn_str, autocommit=True, timeout=3)
        cursor = conn.cursor()
        cursor.execute("IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'crm_faculdade') CREATE DATABASE crm_faculdade")
        print(f"✅ Sucesso! Banco criado usando a instância: {instancia}")
        sucesso = True
        conn.close()
        break 
    except:
        continue

if not sucesso:
    print("❌ Erro: Não foi possível encontrar uma instância do SQL Server ativa.")
    print("Certifique-se de que o SQL Server está instalado e o protocolo TCP/IP habilitado.")