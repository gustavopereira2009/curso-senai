nome = input("Qual seu nome ? : ")
serie = int(input("Qual a sua serie ? : "))
idade = int(input("Qual a sua idade ?  : "))
nota = float(input("Qual a sua nota ? :  "))

if nome == "Eduarda":
    print("Reprovado")

elif nota > 70 and serie == 2:
    print("Reprovado")

elif idade < 18 and nota < 70:
    print("Vai estudar")

elif nome == "Moya" and idade == 22 and nota >=90:
    print("Sencacional")

else:
    print("Cansei, é sexta!")