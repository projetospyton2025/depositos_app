# run.py (DESCOMENTE PARA RODAR LOCALMENTE)
"""
from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
"""
# run.py (COMENTE PARA RODAR LOCALMENTE)
from app import create_app, db
import os

app = create_app()

if __name__ == '__main__':
    # Configura o contexto do aplicativo para criar tabelas no banco de dados.
    with app.app_context():
        db.create_all()

    # Obtém a porta do ambiente (Render) ou usa 5000 como padrão.
    port = int(os.environ.get("PORT", 5000))
    # Executa o servidor no modo de produção.
    app.run(host="0.0.0.0", port=port, debug=False)
