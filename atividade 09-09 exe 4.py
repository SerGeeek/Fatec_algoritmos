n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))
n3 = float(input("Digite o número 3: "))
menor = 0
maior = 0
if n1 >= n2 and n3:
    maior = n1
if n2 >= n1 and n3:
    maior = n2
if n3 >= n1 and n2:
    maior = n3
if n1 <= n2 and n3:
    menor = n1
if n2 <= n1 and n3:
    menor = n2
if n3 < n1 and n2:
    menor = n3
diferenca = maior - menor
print("A diferença entre eles é de: ", diferenca)