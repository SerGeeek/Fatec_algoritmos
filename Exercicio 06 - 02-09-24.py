# pag 43 Apostila-Logica de Programacao e Algoritmos em Python

# 6) Considerando que a aprovação de um aluno em determinada disciplina
# requer uma média final maior ou igual a 6,0 (seis). Elaborar um programa
# que receba duas notas, realize o calculo da média, exiba o valor calculado
# e também se o aluno está aprovado ou reprovado.

nome = input ("Digite seu nome aqui:")
notaPort = float(input ("Digite sua nota de Matemática:"))
notaMat = float(input ("Digite sua nota de Português:"))
media = (notaPort + notaMat) / 2
resultado = ""
if media >= 6:
    resultado = "aprovado"
else:
    resultado = "reprovado"
print (nome, "a sua media é", media, "e você está", resultado,"nestas duas matérias")
