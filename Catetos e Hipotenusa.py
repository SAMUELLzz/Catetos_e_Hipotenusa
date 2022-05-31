from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip =  (ca ** 2 + co ** 2) ** (1/2)
print(f'A hipotenusa vai medir: {hip:.2f}')