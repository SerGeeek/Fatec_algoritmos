"""O IPVA de um veículo é calculado tomando como base o valor do veículo, o combustível utilizado e o tipo do veículo
que serão digitados pelo usuário. Em seguida, o IPVA será calculado como 5% do valor do veículo, no caso de automóveis
movidos a gasolina ou flex. Já para carros movidos somente a etanol, eletricidade ou gás ou qualquer desses três
combustíveis combinados, a alíquota é de 4%. Para motos, camionetes cabine simples e ônibus ou micro-ônibus a alíquota
é de 2,5% e para caminhões, de 1,5%. Elaborar um programa em Python que, a partir destas informações, calcule e mostre
o valor do IPVA."""

valor = float(input('Digite o valor de seu veículo: '))
tipo = int(input('Digite 1 = para Automóveis / 2 = para motos, camionetes cabine simples, ônibus ou micro-ônibus / 3 = para caminhões: '))
comb = int(input('Digite 1 = para Gasolina ou Flex / 2 = para etanol, elétrico ou gás / 3 = Nenhum dos anteriores: '))
if tipo == 1 and comb == 1:
    print ('O valor de seu IPVA é de:', valor * (5/100))
if tipo == 1 and comb == 2:
    print ('O valor de seu IPVA é de:', valor * (4/100))
if tipo == 2:
    print ('O valor de seu IPVA é de:', valor * (2.5/100))
if tipo == 3:
    print ('O valor de seu IPVA é de:', valor * (1.5/100))
    