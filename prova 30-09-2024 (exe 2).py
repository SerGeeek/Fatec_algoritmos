"""Elaborar um fluxograma que permita determinar se um determinado número inteiro, digitado pelo usuário, é multiplo
de 4 ou de 6."""

numero = int(input('Digite um número inteiro: '))
if numero % 4 == 0 or numero % 6 == 0:
    print ('O seu número é múltiplo de 4 ou de 6')
else:
    print ('O seu número não é múltiplo de 4 ou de 6!')