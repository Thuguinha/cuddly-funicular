import math

ag = float(input('Digite o angulo em graus: '))

ar = math.radians(ag)

s = math.sin(ar)
c = math.cos(ar)
t = math.tan(ar)

print('O Seno de {}°: {:.2f}'.format(ag, s))
print('O Cosseno de {}°: {:.2f}'.format(ag, c))
print('o Tangente de {}°: {:.2f}'.format(ag, t))