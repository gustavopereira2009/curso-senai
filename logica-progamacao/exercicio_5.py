import json

arquivo = "clientes.json"

try:
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        clientes = json.load(arquivo)
except FileNotFoundError:
    clientes = []


novo_cliente = {
    "nome": input("Nome: "),
    "email": input("E-mail: "),
    "idade": int(input("Idade: ")),
}


clientes.append(novo_cliente)

with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)
 
print(f"Cliente adicionado! Total de clientes: {len(clientes)}")