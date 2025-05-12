import json
import os

arquivo = 'package.json'


# Passo 1: Verifica se o arquivo existe e carrega os dados
if os.path.exists(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as arq:
        try:
            usuarios = json.load(arq)
        except json.JSONDecodeError:
            usuarios = []
else:
    usuarios = []

# Passo 2: Coleta novos dados do usuário
nome1 = input("Digite seu nome: ")
senha1 = input("Digite sua senha: ")

novo_usuario = {"nome": nome1, "senha": senha1}
usuarios.append(novo_usuario)

# Passo 3: Salva todos os usuários no arquivo novamente
with open(arquivo, 'w', encoding='utf-8') as arq:
    json.dump(usuarios, arq, indent=4, ensure_ascii=False)

os.system('cls')

print("Usuário adicionado com sucesso!")


with open(arquivo, 'r', encoding='utf-8') as arq:
    print(json.load(usuarios, arq, indent=4, ensure_ascii=False))
