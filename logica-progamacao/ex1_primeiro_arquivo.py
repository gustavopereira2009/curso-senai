import json

produto = {
    "Nome": "Notebook",
    "Preco": 3500.00,
    "Estoque": 12,
    "Categorias": ["Informatica", "Eletronicos"]
}

with open("Produtos.json", "w", encoding="utf-8") as arquivo:
    json.dump(produto, arquivo, ident=4, ensure_ascii=False)

print("Arquivo produto.json criado com sucesso!")