"""
8) A partir de cinco números reais, digitados pelo usuário, exibir o valor da 
média considerando apenas os números que são maiores que zero e 
menores do que mil.
"""
n1 = float(input ("Digite o número 1: "))
n2 = float(input ("Digite o número 2: "))
n3 = float(input ("Digite o número 3: "))
n4 = float(input ("Digite o número 4: "))
n5 = float(input ("Digite o número 5: "))
soma = 0.0
cont = 0
if n1 > 0 and n1 < 1000:
    soma = soma + n1
    cont = cont + 1
if n2 > 0 and n2 < 1000:
    soma = soma + n2
    cont = cont + 1
if n3 > 0 and n3 < 1000:
    soma = soma + n3
    cont = cont + 1
if n4 > 0 and n4 < 1000:
    soma = soma + n4
    cont = cont + 1
if n5 > 0 and n5 < 1000:
    soma = soma + n5
    cont = cont + 1
if cont != 0: 
    print ("A média é:",(soma/cont))
else:
    print ("Nenhum dos números atende os requisitos!")