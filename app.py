from flask import Flask, render_template
app = Flask(__name__)

@app.route ('/')
def index():
    return render_template('index.html')

@app.route ('/login')
def login():
    return render_template ('login.html')

@app.route ('/cadastro')
def cadastro():
    return render_template ('cadastro.html')

@app.route ('/dashboard')
def dashboard():
    return render_template ('dashboard.html')

@app.route ('/criarregistro')
def criarregistro():
    return render_template ('criarregistro.html')

@app.route ('/registros')
def registros():
    return render_template ('registros.html')

@app.route ('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route ('/configuracoes')
def configuracoes():
    return render_template ('configuracoes.html')

