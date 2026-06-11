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

@app.route ('/registros')
def registros():
    return render_template ('registros.html')

@app.route ('/criarregistro')
def criarregistro():
    return render_template ('criarregistro.html')

@app.route ('/relatorio')
def relatorio():
    return render_template ('relatorio.html')

