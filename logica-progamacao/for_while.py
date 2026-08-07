numeros = [1,2,3,4,5]
soma = 0 

for numero in numeros:
    soma = soma + numero
    soma += numero
    print(soma)
print(soma)




senha_correta = input("Diigite a senha correta")
senha = input("Digite a senha")


while senha != senha_correta:
    print("Senha incorreta. Tentre novamente")
    senha = input("Digite a senha: ")

     print("Seja bem vindo!")
    

while true:
    numero = int(input)
    soma += numero
    if numero == 0:
        break
        print(soma)
