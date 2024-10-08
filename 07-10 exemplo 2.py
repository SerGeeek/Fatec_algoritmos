# Exibir o valor da média de 8 números
# reais digitados pelo usuário

cont = 1
soma = 0.0
while cont <= 8:
    num = float(input('Valor: '))
    soma = soma + num
    cont = cont + 1
media = soma / 8
print ("A média é", media)