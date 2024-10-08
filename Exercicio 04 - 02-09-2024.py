# pag 43 Apostila-Logica de Programacao e Algoritmos em Python

# 4) Elaborar uma rotina que, a partir de um número real digitado pelo
# usuário, mostre o seu valor absoluto.

num = float(input('Número? '))
if num <0.0:
        num = num * (-1)
print ('O valor absoluto é', num)