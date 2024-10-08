preco = float(input('Insira o valor do produto:'))
qtd = float(input("Insira a quantidade do produto:"))
des = float(input("Insira o desconto:"))
total = (preco * qtd) - des
print(f'Valor final é R${total:.2f}')