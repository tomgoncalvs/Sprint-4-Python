import cx_Oracle

def conn():
    # Credenciais do banco de dados
    db_username = ''
    db_password = ''
    db_host = 'localhost'
    db_port = '1521'
    db_service_name = 'ORCL'

# Criação da DSN (Data Source Name)
    db_dsn = cx_Oracle.makedsn(db_host, db_port, service_name=db_service_name)

    try:
        # Estabelecendo a conexão
        connection = cx_Oracle.connect(db_username, db_password, dsn=db_dsn)
        print("Conexão bem-sucedida com o Oracle Database")
        return connection  # Retorna a conexão aberta
        
    except cx_Oracle.DatabaseError as e:
        # Em caso de erro na conexão
        error, = e.args
        print("Erro ao conectar ao Oracle Database")
        print(f"Código do erro: {error.code}")
        print(f"Mensagem de erro: {error.message}")
        return None