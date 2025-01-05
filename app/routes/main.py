#Este arquivo contém as rotas principais do seu aplicativo. Ele gerencia o login, registro e a manipulação de depósitos.
#  É importante garantir que o banco de dados seja atualizado corretamente aqui, especialmente quando o usuário faz login, se registra ou interage com os depósitos.

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from app.models.user import User
from app import db
import json

main = Blueprint('main', __name__)

DEPOSITS_STRUCTURE = [
    (5.00, 20, 100.00),
    (10.00, 30, 300.00),
    (20.00, 30, 600.00),
    (50.00, 40, 2000.00),
    (75.00, 40, 3000.00),
    (100.00, 40, 4000.00)
]

@main.route('/')
def index():
    if current_user.is_authenticated:
        # Recarrega o usuário do banco de dados para garantir dados atualizados
        user = User.query.get(current_user.id)
        try:
            deposits_status = json.loads(user.deposits or '{}')
            print(f"Deposits carregados para {user.username}: {deposits_status}")  # Debug log
        except json.JSONDecodeError:
            print(f"Erro ao decodificar deposits para {user.username}")  # Debug log
            deposits_status = {}
        
        total_clicked = sum(float(key.split('-')[0])
                          for key, value in deposits_status.items()
                          if value)
                          
        return render_template('index.html',
                             deposits_structure=DEPOSITS_STRUCTURE,
                             deposits_status=deposits_status,
                             total_clicked=total_clicked)
    return render_template('index.html')



@main.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        login_user(user)
        return redirect(url_for('main.index'))

    flash('Usuário ou senha inválidos')
    return redirect(url_for('main.index'))

@main.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if User.query.filter_by(username=username).first():
        flash('Usuário já existe')
        return redirect(url_for('main.index'))

    user = User(username=username, deposits='{}')
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    login_user(user)
    return redirect(url_for('main.index'))

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
# Em app/routes/main.py, atualize a rota toggle_deposit:
@main.route('/toggle_deposit', methods=['POST'])
@login_required
def toggle_deposit():
    try:
        data = request.json
        value = data['value']
        index = data['index']
        key = f"{value}-{index}"

        # Recarrega o usuário do banco de dados
        user = User.query.get(current_user.id)
        
        # Carrega os depósitos existentes
        try:
            deposits = json.loads(user.deposits or '{}')
        except json.JSONDecodeError:
            deposits = {}
        
        # Marca o depósito
        deposits[key] = True
        
        # Salva de volta no banco
        user.deposits = json.dumps(deposits)
        print(f"Salvando deposits para {user.username}: {deposits}")  # Debug log
        
        # Commit explícito
        db.session.add(user)
        db.session.commit()
        
        return {'success': True, 'deposits': deposits}
        
    except Exception as e:
        print(f"Erro ao salvar depósito: {str(e)}")  # Debug log
        db.session.rollback()
        return {'success': False, 'error': str(e)}, 500

"""
        ADICIONADO  a rota de teste check_deposits também no main.py
"""
@main.route('/check_deposits')
@login_required
def check_deposits():
    try:
        # Buscar o usuário diretamente do banco de dados
        user = User.query.get(current_user.id)
        deposits = json.loads(user.deposits or '{}')
        return {
            'username': user.username,
            'deposits': deposits,
            'raw_deposits': user.deposits
        }
    except Exception as e:
        return {'error': str(e)}, 500