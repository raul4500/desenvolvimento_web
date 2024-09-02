from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Acessando dados da requisição
        nome = request.form['nome']
        turma = request.form['turma']
        professor = request.form['professor']
        data = request.form['data']
        dificuldade = request.form['dificuldade']
        nota = request.form['nota']

        # Redirecionando para a página de resultado com os dados
        return render_template('result.html', nome=nome, turma=turma, professor=professor, 
                               data=data, dificuldade=dificuldade, nota=nota)
    return render_template('form.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)