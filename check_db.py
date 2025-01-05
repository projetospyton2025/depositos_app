# Salve este arquivo como check_db.py na pasta raiz do projeto (C:/depositos_app/check_db.py)

# VERIFICA O BANCO DE DADOS



import sqlite3
import os

def check_database():
    try:
        # Verifica se o arquivo do banco existe
        db_path = 'instance/depositos.db'
        print(f"Verificando banco de dados em: {os.path.abspath(db_path)}")
        print(f"O arquivo existe? {os.path.exists(db_path)}\n")

        # Conecta ao banco
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Verifica a estrutura da tabela
        cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='user'")
        print("Estrutura da tabela:")
        print(cursor.fetchone()[0])
        
        # Verifica os dados dos usuários
        print("\nDados dos usuários:")
        cursor.execute("SELECT id, username, deposits FROM user")
        users = cursor.fetchall()
        if not users:
            print("Nenhum usuário encontrado no banco de dados.")
        else:
            for row in users:
                print(f"ID: {row[0]}")
                print(f"Username: {row[1]}")
                print(f"Deposits: {row[2]}")
                print("-" * 50)
        
        conn.close()
        
    except Exception as e:
        print(f"Erro ao verificar banco de dados: {str(e)}")

if __name__ == "__main__":
    check_database()
    
    
   

""" VERIFICA SE O BANDO DE DADOS FOI RECRIADO E EXISTE
# check_db.py
import sqlite3
import os

def check_database():
    try:
        db_path = 'app/depositos.db'
        print(f"Verificando banco de dados em: {os.path.abspath(db_path)}")
        print(f"O arquivo existe? {os.path.exists(db_path)}\n")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Lista todas as tabelas no banco
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        
        print("Tabelas encontradas no banco:")
        if not tables:
            print("Nenhuma tabela encontrada!")
        else:
            for table in tables:
                print(f"- {table[0]}")
                # Mostra a estrutura de cada tabela
                cursor.execute(f"PRAGMA table_info({table[0]})")
                columns = cursor.fetchall()
                print("  Colunas:")
                for col in columns:
                    print(f"    {col[1]} ({col[2]})")
        
        conn.close()
        
    except Exception as e:
        print(f"Erro ao verificar banco de dados: {str(e)}")

if __name__ == "__main__":
    check_database()
    
"""

"""

05/01/2025  18:16    <DIR>          .
05/01/2025  18:16    <DIR>          ..
05/01/2025  18:21    <DIR>          app
04/01/2025  14:48               873 app.log
05/01/2025  18:17             2.612 check_db.py
04/01/2025  13:19               464 config.py
04/01/2025  14:33    <DIR>          Deposito_app-Dados
05/01/2025  17:38    <DIR>          instance
03/01/2025  14:46             1.096 LICENSE
03/01/2025  14:46               131 README.md
05/01/2025  18:16               984 recreate_db.py
04/01/2025  17:33               512 requirements.txt
04/01/2025  16:06             1.700 run.py
04/01/2025  16:40    <DIR>          venv
04/01/2025  13:19    <DIR>          __pycache__
               8 arquivo(s)          8.372 bytes
               7 pasta(s)   365.007.884.288 bytes disponíveis

C:\depositos_app>python check_db.py
Verificando banco de dados em: C:\depositos_app\app\depositos.db
O arquivo existe? True

Tabelas encontradas no banco:
- user
  Colunas:
    id (INTEGER)
    username (VARCHAR(150))
    password_hash (VARCHAR(150))
    deposits (TEXT)
- sqlite_sequence
  Colunas:
    name ()
    seq ()

C:\depositos_app>python recreate_db.py
Banco de dados antigo removido: app/depositos.db
Banco de dados recriado com sucesso!

C:\depositos_app>python check_db.py
Verificando banco de dados em: C:\depositos_app\app\depositos.db
O arquivo existe? True

Estrutura da tabela:
CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(150) NOT NULL UNIQUE,
            password_hash VARCHAR(150) NOT NULL,
            deposits TEXT
        )

Dados dos usuários:
Nenhum usuário encontrado no banco de dados.

C:\depositos_app>
"""