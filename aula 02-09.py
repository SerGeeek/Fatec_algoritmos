# pag 37  Apostila-Logica de Programacao e Algoritmos em Python

from datetime import datetime

nome = input ("Digite seu nome aqui:")
anoNasc = int(input ("Digite o ano de nascimento:"))
hoje = datetime.now()
anoAtual = int (f'{hoje:%Y}')
idade = anoAtual - anoNasc
maioridade = ""
site = ""
if idade >= 18:
    maioridade = "maior"
    site = "YouTube"
else:
    maioridade = "menor"
    site = "Disney"
print (nome, "a sua idade é", idade, "anos e você é", maioridade,"de idade")
print ('e sugerimos o site', site)