dia = int(input('Quantos dias alugados? : ' ))
km = float(input('Quantos km rodados? : '))

d = 60 * dia
k = 0.15 * km

f = d + k

print('O total a pagar é R${:.2f}'.format(f))