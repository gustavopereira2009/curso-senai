aprovados = 0
recuperacao = 0
reprovados = 0

for i in renge(5):
    nota = float(input("Digite a media do aluno: "))

    if nota  >= 6:
    print("Aprovado")
    Aprovado = aprovados  + 1

    elif nota >=4:
    print("Recuperacao")
    recuperacao = recupercao + 1

    else:
        print(Reprovado)

print("Aprovados:", aprovados)
print("Recuperações:", recuperacao)
print("Reprovados:", reprovados)