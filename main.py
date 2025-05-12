from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)
arquivo = 'package.json'

if os.path.exists(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as arq:
        try:
            usuarios = json.load(arq)
        except json.JSONDecodeError:
            usuarios = []
else:
    usuarios = []

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        novo_usuario = {"nome": name, "email": email}
        usuarios.append(novo_usuario)
        
        with open(arquivo, 'w', encoding='utf-8') as arq:
            json.dump(usuarios, arq, indent=4, ensure_ascii=False)
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)