import pyodbc
from sqlCredentials import credentialsSQLSERVER

class sql_database():

    def __init__(self):
        try:
            #configura conexão com o banco

            connectionString = (
                f'DRIVER={{ODBC Driver 18 for SQL Server}};'
                f'SERVER={credentialsSQLSERVER.SERVER};'
                f'DATABASE={credentialsSQLSERVER.DATABASE};'
                f'Trusted_Connection=yes;'
                f'Encrypt=yes;'  # Habilita a criptografia SSL
                #f'TrustServerCertificate=yes;'  # Aceita certificados SSL não confiáveis
            )

            self.conexao = pyodbc.connect(connectionString)
            print('Conexão estabelecida com sucesso.')

            cursor = self.conexao.cursor()
            cursor.execute('SELECT @@version')

            row = cursor.fetchone()
            print(f'Versão do SQL Server: {row[0]}')
            cursor.close()

        except pyodbc.Error as e:
            print(f'Erro ao conectar ao SQL Server: {e}')
    
    def insert_table(self, math_expression, result, status):

        cursor = self.conexao.cursor()

        query = f"""INSERT INTO dbo.calculadora(math_expression, result, status_operation)
                    VALUES ('{math_expression}', '{result}', '{status}')"""

        cursor.execute(query)
        cursor.commit()
        cursor.close()
        self.conexao.close()