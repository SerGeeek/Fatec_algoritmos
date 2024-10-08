# 4) Considerando uma moeda lançada 10 vezes, criar uma aplicação que determine
# o número de ocorrências de cada um dos lados.

cont = 1
ncaras = 0
ncoroas = 0
while cont <= 10:
    lado = int (input ("Digite 1 para CARA ou 2 para COROA: "))
    if lado == 1:
        ncaras = ncaras +1
        cont = cont + 1
    elif lado == 2:
        ncoroas = ncoroas +1
        cont = cont + 1
    else:
        print ("ERRO! Digite apenas 1 ou 2!")
print ("Caras = ", ncaras, "\ncoroas = ", ncoroas)