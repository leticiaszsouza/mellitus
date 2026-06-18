from flask import Flask
from flask import request, render_template, redirect, url_for 
app = Flask(__name__)

@app.route ('/')
def index():
    return render_template('index.html')

@app.route ('/login')
def login(): 
    return render_template ('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        return redirect(url_for('dashboard')) 

    return render_template('cadastro.html')

@app.route ('/dashboard')
def dashboard():
    return render_template ('dashboard.html')

@app.route ('/criarregistro', methods=['GET', 'POST'])
def criarregistro():
    if request.method == 'POST':
        data_hora = request.form.get('data-hora')
        glicemia = request.form.get('glicemia')
        carboidratos = request.form.get('carboidratos')

        return redirect(url_for('dashboard')) 
    return render_template ('criarregistro.html')

@app.route ('/registros')
def registros():
    return render_template ('registros.html')

@app.route ('/perfil')
def perfil():
    usuario = {
        'nome': 'Letícia Souza',
        'email': 'leticia0819@email.com',
        'idade': 18,
        'tipo_diabetes': 'Tipo 1'}
    
    return render_template('perfil.html', usuario=usuario)

@app.route ('/configuracoes')
def configuracoes():
    return render_template ('configuracoes.html')

@app.route('/contatos', methods=['GET', 'POST'])
def contatos():
    success_message = None
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        assunto = request.form.get('assunto')
        mensagem = request.form.get('mensagem')

        # Aqui você pode enviar um e-mail ou salvar a mensagem em banco.
        success_message = 'Recebemos sua mensagem! Retornaremos em breve.'

        return render_template(
            'contatos.html',
            success_message=success_message,
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem,
        )
 
    return render_template('contatos.html')