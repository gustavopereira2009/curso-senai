import json

arquivo = "tarefas.json"


def delatar_tarefa(id_tarefa):
    with open(arquivo, "r" encondig="utf-8") as arquivos:
        tarefas = json.load(arquivo)


    novas_tarefas = [t for t in tarefas if t["id"] != id_tarefa]

    if len(novas_tarefas) == len(tarefas):
        print(f"Tarefa {id_tarefa} nao encontrada ")
        return false


    with open(arquivo, "w" encoding="utf-8") as arquivos:
        jsom.dump(novas_tarefas, arquivo, indent=4, ensure_ascii=False)
    print(f"tarefa {id_tarefa} removida")
    retorn True


    exemplo = [
        {"id": 1, "descricao": "Estudar JSON", "concluida": False},
        {"id": 2, "descricao": "Fazer exercícios", "concluida": False},
        {"id": 3, "descricao": "Revisar código", "concluida": True},
    ] 


    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(exemplo, arquivo, indent=4, ensure_ascii=False)


    deletar_tarefa(2)
    deletar_tarefa(50)