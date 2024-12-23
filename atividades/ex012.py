l = float(input('Largura da parede: '))

a = float(input('Altura da parede:  ') )

m = l * a

t = m / 2

print('A sua parede tem a dimensão de {}x{} \nsua área é de {}m2 \nvoçê precisará de {:.2f}L de tinta'.format(l, a, m, t))