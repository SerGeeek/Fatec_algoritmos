"""
26) Elaborar um programa que calcule e exiba o comprimento de uma 
circunferência, a partir de um raio (R), digitado pelo usuário e que deverá 
ser um número real positivo. O comprimento é obtido através da fórmula: 
2 x π x R.
"""

r = float(input("Digite o raio:"))
if r > 0:
        c = 6.28 * r
        print(c)
else:
    print ("Digite um valor superior a zero!")