p = float(input('Qual é o preço do produto: '))

d =  p - (p * 5 / 100)

print('O produto com o preço de {} reais, tera o desconto de 5%, chegando no valor de {:.2f}'.format(p, d))
