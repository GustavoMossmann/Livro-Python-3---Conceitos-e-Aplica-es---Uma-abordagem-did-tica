print('\nExpressões Aritméticas\n')
a, b, c = 4, 5, 1

r1 = ( a + b ) / 2
print('8a = ', r1)

from math import sqrt
r2 = (-b + sqrt(b**2 - (4*a*c)))/2*a
print('8b = ', r2)

r3 = (3*a + 2*b)/(a + b)
print('8c = {0:.2f}'.format(r3))

r4 = (7.6*a) - (b**1.7)
print('8d = {0:.2f}'.format(r4))

x1, y1, x2, y2 = 1, 1, 4, 5

r5 = sqrt((x1 - x2)**2 + (y1 - y2)**2)
print('8e = ', r5)

print('\nFim do programa')
