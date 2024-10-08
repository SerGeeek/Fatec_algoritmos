'''Criar um programa em Python que permita ao usuário digitar dois números reais e uma das
básicas, sendo '1' para adição, '2' para subtração, '3' para multiplicação e '4' para divisão.
Em seguida, calcular exibir o resultado.'''

num1 = float(input('digite o primeiro numero: '))
num2 = float(input('digite o segundo numero: '))
operacao = float(input('Digite: 1 para adiçâo - 2 para subtração - 3 multiplicaçâo - 4 para divisâo: '))
if operacao == 1:
    print('O resultado da adiçâo é:', num1 + num2)
if operacao == 2:
    print('O resultado da subtraçâo é:', num1 - num2)
if operacao == 3:
    print('O resultado da multiplicaçâo é:', num1 * num2)
if operacao == 4:
    print('O resultado da divisâo é:', num1 / num2)