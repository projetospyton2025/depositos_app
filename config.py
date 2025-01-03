# config.py
class Config:
    SECRET_KEY = 'sua_chave_secreta_aqui'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///depositos.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

