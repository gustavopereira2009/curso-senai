import json

with open("Produtos.json", "r", encondig="utf-8") as arquivos:
    produto = json.load(arquivo)

print(f"Produto: {produto['nome']} | Preço: R$ {produto['preco']} | Estoque: {produto['estoque']} unidades")