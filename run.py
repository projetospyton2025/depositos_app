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
    # port = int(os.environ.get("PORT", 5000))
    port = int(os.environ.get("PORT", 1000))

    # Executa o servidor no modo de produção.
    app.run(host="0.0.0.0", port=port, debug=False)

"""

# run.py (COMENTE PARA RODAR Localmente)
# run.py (DESCOMENTE PARA RODAR Remotamente)

from app import create_app

# Criar a aplicação Flask
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)



"""
Conclusão

    Verifique o caminho do banco de dados no config.py para garantir que ele seja persistente.
    Revise as funções set_password e check_password para garantir que as senhas sejam criptografadas e verificadas corretamente.
    Verifique se db.session.commit() está sendo chamado sempre que houver alteração no banco de dados, como nas rotas de login, registro e interação com os depósitos.
    Teste diretamente no banco de dados se os dados estão sendo realmente salvos.

    1º - config.py
    2º - app/__init__.py
    3º - app/models/user.py
    4º - app/routes/main.py
    5º - depositos.db

    1. config.py

    Este arquivo contém a configuração do banco de dados. Certifique-se de que o caminho do banco de
    dados esteja configurado corretamente, como mencionei antes.

    2. app/__init__.py

    Este arquivo configura o aplicativo Flask e inicializa o banco de dados. Verifique se o banco de dados 
    está sendo inicializado corretamente e se db.create_all() está sendo chamado.

    3. app/models/user.py

    Este arquivo define o modelo de dados para os usuários. Verifique se os campos, como username, password_hash e 
    deposits, estão corretamente configurados e se a lógica de criptografia de senha (set_password e check_password) está correta.


    4. app/routes/main.py
    Este arquivo contém as rotas principais do seu aplicativo. Ele gerencia o login, registro e a manipulação de 
    depósitos. É importante garantir que o banco de dados seja atualizado corretamente aqui, especialmente quando o usuário faz login, se registra ou interage com os depósitos.
    Exemplo de uma rota importante:

    5. Banco de Dados (depositos.db)

    Verifique o conteúdo do arquivo depositos.db diretamente usando uma ferramenta como DB Browser for SQLite. 
    Veja se os dados estão sendo armazenados corretamente e se as tabelas estão sendo criadas conforme o esperado.

    
    """