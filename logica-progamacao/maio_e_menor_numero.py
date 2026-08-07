maior = 0
menor = 0

for numero in numeros:
    numero = float(input("Digite o pimiro numero: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

 print("O maior numero digitado foi:" maior)
 print("O menor numero digitado foi:" menor)