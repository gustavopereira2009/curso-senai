import json

livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890},
    {"titulo": "Capitães da Areia", "autor": "Jorge Amado", "ano": 1937},
]


texto_json = json.dumps(livros, indent=4, ensure_ascii=False)
print(texto_json)
print(type(texto_json))