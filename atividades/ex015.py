produto = float(input(' -------------------- \nDigite o valor do produto R$: '))

parcelado = produto + (produto * 5 / 100)

avista = produto - (produto * 10 / 100)

print(f'-------------------- \nO produto tem o valor de R${produto}\n -------------------- \nparcelado tem um aumento de R${parcelado}\n -------------------- \nE a vista sai por R${avista}')