crianca = 0
adolescente = 0
adulto = 0
idoso = 0

for i in range(10):
    idade = int(input("Idade: "))
    
    if idade < 12:
        crianca += 1
    elif idade < 18:
        adolescente += 1
    elif idade < 60:
        adulto += 1
    else:
        idoso += 1

print("Crianças:", crianca)
print("Adolescentes:", adolescente)
print("Adultos:", adulto)
print("Idosos:", idoso)
