'''num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {:.0f}.'.format(num, num))'''
import math


from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))
