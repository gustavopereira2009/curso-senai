import json 

json_string = '{"usuario": "dev_python", "dev_python", "nivel": "Intermediario","ativo": True}'
dados = json.loads(json_string)

if dados["ativo"]:
    print(f"Bem-vindo, {dados['usuario']}! Nível: {dados['nivel']}.")

else:
     print("Usuário inativo. Acesso negado.")