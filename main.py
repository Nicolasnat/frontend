from flask import Flask, render_template, request, flash
import json
import os

app = Flask(__name__)
arquivo = 'package.json'
app.secret_key = "your_secret_key"

if os.path.exists(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as arq:
        try:
            mesas = json.load(arq)
        except json.JSONDecodeError:
            mesas = []
else:
    mesas = []
mesa_qtde = 4

@app.route("/", methods=["GET", "POST"])
def homepage():
    return render_template("index.html")

@app.route("/reserva", methods=["GET", "POST"])
def reserva():

    mesas_ocupadas = len(mesas)
    mesas_disponiveis = mesa_qtde - mesas_ocupadas

    if request.method == "POST":
        # Verifica se ainda há mesas disponíveis
        if mesas_disponiveis <= 0:
            flash("Desculpe, não há mesas disponíveis no momento!", "error")
            return render_template("index.html", mesas_disponiveis=mesas_disponiveis)
        
        name = request.form["name"]
        email = request.form["email"]
        mesa = request.form["mesa"]
        mesa_quant = request.form["mesa_quant"]

        
        remessa = {"nome": name, "email": email, "mesa": mesa, "quantidade de mesas": mesa_quant}
        mesas.append(remessa)
       
        with open(arquivo, 'w', encoding='utf-8') as arq:
            json.dump(mesas, arq, indent=4, ensure_ascii=False)

        flash("Reserva realizada com sucesso!", "success")
        mesas_disponiveis -= 1  # Atualiza a quantidade disponível
        print(mesas_disponiveis)

    return render_template("reserva.html", mesas_disponiveis = mesas_disponiveis)


if __name__ == "__main__":
    app.run(debug=True)