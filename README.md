# calculadora
Calculadora criada utilizando a biblioteca tkinter para a interface gráfica em python e que insere as operações executadas no banco de dados SQL Server.

Para a integração com o SQL Server é necessário seguir o passo a passo:
1) Fazer download do SQL Server e do SQL Server Management Studio.
2) Criar um servidor e a tabela no SQL Server Management Studio.
3) Configurar um certificado SSL (pode ser um autoassinado se for ambiente de desenvolvimento).
4) Verificar se a instância do servidor tem permissão para acessar o certificado.
5) Criar um arquivo em python para as credenciais. Exemplo do código:

                           class credentialsSQLSERVER:
                                 SERVER = 'nome_servidor'
                                 DATABASE = 'nome_database'


Interface final da calculadora:

![image](https://github.com/user-attachments/assets/0cb0c6be-b103-4aeb-93b5-893cf92c11b6)

Operações de teste que foram inseridas no SQL Server:

![image](https://github.com/user-attachments/assets/c7130704-891c-4187-99cf-33617d69073b)
