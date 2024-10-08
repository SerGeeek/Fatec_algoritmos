n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))
n3 = int(input("Digite o número 3: "))
n4 = int(input("Digite o número 4: "))
maior = 0
if n1 % 2 == 0:
    maior = n1
if n2 % 2 == 0 and n2 > maior:
    maior = n2
if n3 % 2 == 0 and n3 > maior:
    maior = n3
if n4 % 2 == 0 and n4 > maior:
    maior = n4
if maior == 0:
    print("Não existem números pares.")
else:
    print("O maior número par é: ", maior)