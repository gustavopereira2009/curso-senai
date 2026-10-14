import json

ARQUIVO = "estoque.json"
 
 
def atualizar_preco(id_produto, novo_preco):
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)
 
    for produto in produtos:
        if produto["id"] == id_produto:
            produto["preco"] = novo_preco
            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
            print(f"Preço do produto '{produto['nome']}' atualizado para R$ {novo_preco:.2f}")
            return True


 print(f"Produto com id {id_produto} não encontrado.")
    return False


    exemplo = [
        {"id": 1, "nome": "Mouse", "preco": 50.0},
        {"id": 2, "nome": "Teclado", "preco": 120.0},
        {"id": 3, "nome": "Monitor", "preco": 900.0},
    ]


with open (ARQUIVO, "w", encoding="utf-8") as arquivo:
    jsom.dump(exemplo, arquivo, indent=4, ensure_ascii=False)


    atulizar_preco(2, 149.00)
    atualizar_preco(99,10.0)