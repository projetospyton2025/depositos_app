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