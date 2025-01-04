# app/__init__.py

#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
#from config import Config

#db = SQLAlchemy()
#login_manager = LoginManager()

#def create_app():
#    app = Flask(__name__)
#    app.config.from_object(Config)
    
#    db.init_app(app)
#    login_manager.init_app(app)
#    login_manager.login_view = 'main.index'
    
#    from app.routes.main import main
#    app.register_blueprint(main)
    
#    return app


"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Caminho absoluto para a raiz do projeto
    project_root = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(project_root, '../depositos.db')  # '../' sobe para a raiz do projeto
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o SQLAlchemy
    db.init_app(app)

    # Importa as rotas e modelos
    with app.app_context():
        from app.routes import main
        app.register_blueprint(main)

        from app.models import user  # Certifique-se de importar os modelos
        
        # Cria o banco de dados, se ele ainda não existir
        db.create_all()

    return app
"""
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Inicializando extensões
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Configuração do banco de dados
    project_root = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(project_root, '../depositos.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "sua-chave-secreta"  # Altere para uma chave segura

    # Inicializando extensões com o app
    db.init_app(app)
    login_manager.init_app(app)

    # Configuração do login
    login_manager.login_view = "main.login"

    # Registrando rotas
    with app.app_context():
        from app.routes.main import main
        app.register_blueprint(main)

        # Importa modelos e cria o banco de dados
        from app.models.user import User
        db.create_all()

    return app
"""
"""
#Este arquivo configura o aplicativo Flask e inicializa o banco de dados. Verifique se o banco de dados está sendo inicializado corretamente e se db.create_all() está sendo chamado.

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Inicializando extensões
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados
    project_root = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(project_root, 'depositos.db')  # Usando caminho correto
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'sua-chave-secreta'  # Defina uma chave secreta segura

    # Inicializando extensões
    db.init_app(app)
    login_manager.init_app(app)

    # Registrando rotas
    from app.routes.main import main
    app.register_blueprint(main)

    # Criando banco de dados
    with app.app_context():
        db.create_all()

    return app
"""

# No início de __init__.py, adicione: arquivo de log para rastrear problemas:
import logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import logging

# Configuração do logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    try:
        # Garante que o diretório instance existe
        os.makedirs(app.instance_path, exist_ok=True)
        
        # Define o caminho do banco de dados na pasta instance
        db_path = os.path.join(app.instance_path, 'depositos.db')
        
        app.config.update(
            SECRET_KEY='sua-chave-secreta-muito-segura',
            SQLALCHEMY_DATABASE_URI=f'sqlite:///{db_path}',
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )
        
        # Inicialização das extensões
        db.init_app(app)
        login_manager.init_app(app)
        login_manager.login_view = 'main.index'
        
        # Registro das rotas
        from app.routes.main import main
        app.register_blueprint(main)
        
        # Criação das tabelas
        with app.app_context():
            db.create_all()
            logging.info(f"Banco de dados inicializado em: {db_path}")
            
    except Exception as e:
        logging.error(f"Erro na configuração do banco de dados: {str(e)}")
        raise
        
    return app