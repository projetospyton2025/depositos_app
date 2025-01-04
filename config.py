# config.py

"""
class Config:
    SECRET_KEY = 'sua_chave_secreta_aqui'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///depositos.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
"""

# caminho absoluto
import os

class Config:
    SECRET_KEY = 'sua_chave_secreta_aqui'
    db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'depositos.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

