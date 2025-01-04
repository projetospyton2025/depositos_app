# run.py (DESCOMENTE PARA RODAR Localmente)
# run.py (COMENTE PARA RODAR Remotamente)

"""
from app import create_app, db
import os

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db_path = os.path.join(os.getcwd(), 'depositos.db')
        print(f"Caminho do banco de dados: {db_path}")
        print(f"Banco existe? {os.path.exists(db_path)}")
        db.create_all()
    app.run(debug=True)
"""

"""
from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
"""

# run.py (COMENTE PARA RODAR Localmente)
# run.py (DESCOMENTE PARA RODAR Remotamente)

"""
from app import create_app, db
import os

app = create_app()

if __name__ == '__main__':
    # Configura o contexto do aplicativo para criar tabelas no banco de dados.
    with app.app_context():
        db.create_all()

    # Obtém a porta do ambiente (Render) ou usa 5000 como padrão.
    port = int(os.environ.get("PORT", 1000))
    # Executa o servidor no modo de produção.
    app.run(host="0.0.0.0", port=port, debug=False)
"""
# Adicione no início do run.py:
import logging
logging.basicConfig(level=logging.DEBUG)


# run.py
from app import create_app, db
import os

app = create_app()

if __name__ == '__main__':
    # Configura o contexto do aplicativo para criar tabelas no banco de dados
    with app.app_context():
        db.create_all()
        
    # Obtém a porta do ambiente ou usa 5000 como padrão
    port = int(os.environ.get("PORT", 5000))
    # Executa o servidor
    app.run(host="0.0.0.0", port=port, debug=True)