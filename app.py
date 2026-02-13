from flask import Flask, render_template, redirect, request, flash
import requests

ENDPOINT_API = "https://api.thecatapi.com/v1/images/search"

app = Flask(__name__)
app.secret_key = "rebeca123"

# Rota da Página Inicial
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Rota para processar a solicitação
@app.route('/cat', methods=['GET', 'POST'])
def cat():
    if request.method == 'GET':
        return redirect('/')
    
    # Remove espaços em branco antes e depois e trata valor vazio
    nome = request.form.get('nome', '').strip()

    if not nome:
        flash("ERRO! Você precisa digitar um nome!")
        return redirect('/')
    
    resposta = requests.get(ENDPOINT_API)

    if resposta.status_code == 200:
        dados = resposta.json() #JSON para dicionário
        url_imagem = dados[0]['url']
    else:
        flash("ERRO! Os gatos estão dormindo... Volte mais trarde!")
        return redirect('/')

    return render_template('index.html', nome=nome, url_imagem=url_imagem)

if __name__ == '__main__':
    app.run(debug=True)    