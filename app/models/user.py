# app/models/user.py

# app/models/user.py
from flask_login import UserMixin
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
import json

class User(db.Model, UserMixin):
    """
    Modelo de usuário com funcionalidades completas de autenticação e 
    gerenciamento de depósitos.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    deposits = db.Column(db.Text, default='{}')

    def set_password(self, password):
        """
        Define a senha do usuário, convertendo-a em um hash seguro.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verifica se a senha fornecida corresponde ao hash armazenado.
        """
        return check_password_hash(self.password_hash, password)

    def get_deposits(self):
        """
        Recupera os depósitos do usuário de forma segura, tratando possíveis erros.
        """
        try:
            return json.loads(self.deposits or '{}')
        except json.JSONDecodeError:
            # Se houver erro na decodificação, retorna um dicionário vazio
            self.deposits = '{}'
            db.session.commit()
            return {}

    def set_deposits(self, deposits_dict):
        """
        Atualiza os depósitos do usuário de forma segura.
        """
        try:
            self.deposits = json.dumps(deposits_dict)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao atualizar depósitos: {str(e)}")
            return False

    def add_deposit(self, value, index):
        """
        Adiciona um novo depósito de forma segura.
        """
        try:
            deposits = self.get_deposits()
            key = f"{value}-{index}"
            if key not in deposits:
                deposits[key] = True
                return self.set_deposits(deposits)
            return True
        except Exception as e:
            print(f"Erro ao adicionar depósito: {str(e)}")
            return False

@login_manager.user_loader
def load_user(user_id):
    """
    Carrega um usuário pelo ID para o Flask-Login.
    """
    return User.query.get(int(user_id))