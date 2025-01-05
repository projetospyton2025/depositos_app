# app/__init__.py
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