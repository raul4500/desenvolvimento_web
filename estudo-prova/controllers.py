from flask import Blueprint,redirect, render_template, request, url_for
from models import tarefas, addTarefas

tarefas_controller = Blueprint('tarefas', __name__)

@tarefas_controller.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@tarefas_controller.route('/add', methods=['POST'])
def add():
    descricao = request.form['descricao']
    addTarefas(descricao)
    return redirect(url_for('tarefas.index'))