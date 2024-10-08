# criar um programa que receba três números inteiros (a,b e c) e exiba o maior deles.

a = float(input ("Digite o número 1:"))
b = float(input ("Digite o número 2:"))
c = float(input ("Digite o número 3:"))
if (a > b) and (a > c):
    print ('Maior =', a)
else:
    if b > c:
        print ('Maior =', b)
    else:
        print ('Maior =', c)