# Exibir o valor da soma de 5 números
# inteiros digitados pelo usuário

cont = 1
soma = 0
while cont <= 5:
    num = int(input ("Número: "))
    soma = soma + num
    cont = cont + 1
print ("A soma é", soma)