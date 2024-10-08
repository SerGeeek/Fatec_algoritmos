"""
Usar .upper() no fim faz com que mesmo que os cornudo digite minusculo,
o codigo ainda funciona!

"""

# comentário curto

est = input ("Digite a sigla da região sudeste: ").upper()
if est == "SP":
    print ("São Paulo")
elif est == "RJ":
    print ("Rio de Janeiro")
elif est == "MG":
    print ("Minas Gerais")
elif est == "ES":
    print ("Espírito Santo")
else:
    print ("Desconhecido")