from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)
lista = []

@app.route('/')
def index():
    return render_template('index.html', lista=lista)

@app.route('/add', methods=['POST'])
def addtarefa():
    descricao = request.form['descricao']
    lista.append(descricao)
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run()