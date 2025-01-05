# recreate_db.py
import sqlite3
import os

def recreate_database():
    try:
        # Remove o banco existente se houver
        db_path = 'instance/depositos.db'
        if os.path.exists(db_path):
            os.remove(db_path)
            print(f"Banco de dados antigo removido: {db_path}")
        
        # Cria novo banco
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Cria a tabela user
        cursor.execute('''
        CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(150) NOT NULL UNIQUE,
            password_hash VARCHAR(150) NOT NULL,
            deposits TEXT
        )
        ''')
        
        conn.commit()
        conn.close()
        
        print("Banco de dados recriado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao recriar banco de dados: {str(e)}")

if __name__ == "__main__":
    recreate_database()