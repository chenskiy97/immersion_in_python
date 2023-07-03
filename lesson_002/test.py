'''
num = 2 + 2 * 2
digit = 36 / 6
print(num, digit)
print(num == digit)
print(num is digit)
'''
'''
a = 5
print(a, id(a))
a += 1
print(a, id(a))

txt = 'hello world'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))
'''
'''
a = c = 2
b = 3
print(a, id(a), b, id(b), c, id(c))
a = b + c
print(a, id(a), b, id(b), c, id(c))
'''
'''
x = 42
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
my_list = [x,y,z]
print(hash)
'''
'''
text = input('введите текст: ')
print(type(text), id(text), hash(text))
'''
'''
a: int = 42
b: float = float(input(': '))
a = a / b
print(a)
'''
'''
def my_func(data: list[int, float]) -> float:
    res = sum(data) / len(data)
    return res


print(my_func([2, 5.5, 15, 8.0, 13.74]))
'''
'''
a: int | float = 42
b: float = float(input(': '))
a = a / b
print(a)
'''
'''
print('Hello world'.__doc__)
print(str.__doc__)
'''
'''
print('hello world'.upper())
print('hello world.count'.count('l'))
'''
'''
print(dir('Hello world!'))
'''
'''
x = 2 ** 16 - 1
print(bin(x))
print(oct(x))
print(hex(x))
'''
'''
x = int('42')
y = int(3.145)
z = int('hello', base=30)
print(x, y, z, sep='\n')
'''
'''
import sys

STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    num *= STEP
'''
'''
num = 7_901_123_456_789
print(num)
'''
'''
print(0.1 + 0.2)
pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375
print(pi)
'''
'''
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
while data:
    print(data.pop())
'''
'''
import math

print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')
'''
'''
a = complex(2, 3)
b = complex('2+3j')
print(a, b, a == b, sep='\n')
'''
'''
a = 42
b = 5
print(divmod(a, b))

print(pow(a, b))
print(pow(a, b, 10))
'''
import fractions

f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)