"""

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
        deposits_status = json.loads(current_user.deposits or '{}')
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

@main.route('/toggle_deposit', methods=['POST'])
@login_required
def toggle_deposit():
    data = request.json
    value = data['value']
    index = data['index']
    key = f"{value}-{index}"
    
    deposits = json.loads(current_user.deposits)
    deposits[key] = True
    
    current_user.deposits = json.dumps(deposits)
    db.session.commit()
    
    return {'success': True}
    
    """
"""
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
        deposits_status = json.loads(current_user.deposits or '{}')
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

@main.route('/toggle_deposit', methods=['POST'])
@login_required
def toggle_deposit():
    data = request.json
    value = data['value']
    index = data['index']
    key = f"{value}-{index}"
    
    deposits = json.loads(current_user.deposits)
    deposits[key] = True
    
    current_user.deposits = json.dumps(deposits)
    db.session.commit()
    
    return {'success': True}

"""

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
        deposits_status = json.loads(current_user.deposits or '{}')
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
        if not data or 'value' not in data or 'index' not in data:
            return {'success': False, 'error': 'Dados inválidos'}, 400
            
        value = float(data['value'])
        index = int(data['index'])
        
        # Validação dos valores
        valid_values = [dep[0] for dep in DEPOSITS_STRUCTURE]
        if value not in valid_values:
            return {'success': False, 'error': 'Valor inválido'}, 400
            
        # Validação do índice
        max_index = next(dep[1] for dep in DEPOSITS_STRUCTURE if dep[0] == value) - 1
        if not (0 <= index <= max_index):
            return {'success': False, 'error': 'Índice inválido'}, 400
        
        # Tenta adicionar o depósito
        if current_user.add_deposit(value, index):
            return {'success': True}
        else:
            return {'success': False, 'error': 'Erro ao salvar depósito'}, 500
            
    except Exception as e:
        db.session.rollback()
        print(f"Erro no toggle_deposit: {str(e)}")
        return {'success': False, 'error': 'Erro interno'}, 500