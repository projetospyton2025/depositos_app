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
