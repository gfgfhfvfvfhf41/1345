
"""
№1
a = input("Введите 3 числа через пробел: ").split()
mul = 1
avg = 0
sum = 0
for i in a:
    mul = mul * float(i)
    avg += int(i)
    sum += int(i)
print(mul, avg/3, sum)
"""

"""
№2
a = float(input("Введите 1 координату: "))
a1 = float(input("Введите 2 координату: "))
if a1 > a:
    print(f'Длина отрезка: {a1-a}')
elif a > a1:
    print(f'Длина отрезка: {a-a1}')
"""

"""
№3
import random
a = random.randint(100, 999)
print(a//100, a//10)
#for i in str(a):
#    print(i)
"""

"""
№4
a, b = b, a
"""

"""
№5
a, b = b, a
"""

"""
№6
import random
a = random.randint(2, 16)
o = ''
while a > 0:
    o = str(a % 2) + o
    a = a // 2
print(o)
"""

"""
№7
import random
a = random.randint(2, 16)
o = ''
d = 0
while a > 0:
    o = str(a % 2) + o
    a = a // 2
for i in o:
    d = d * 2 + int(i)
print(d)
"""

"""
№8
a = int(input("Введите число, которое нужно возвести: "))
b = int(input("Введите число, которое будет степенью: "))
d = int(a)
while b > 1:
    a = a * d
    b = b - 1
print(a)

#либо можно с циклом фор
a = int(input("Введите число, которое нужно возвести: "))
b = int(input("Введите число, которое будет степенью: "))
d = int(a)
for i in range(b-1):
    a *= d
print(a)
"""

"""
№9
a = int(input("Введите возводимое число: "))
a2 = a * a
a4 = a2 * a2
a8 = a4 * a4
a10 = a8 * a2
print(a10)
"""

"""
№10
import random
n = int(input("Введите кол-во студентов: "))
a = random.randint(2, n)
students = []
for i in range(n):
    students.append(i)
print(students[a])
"""

"""
№11
import random
a = float(input("Введите число а: "))
b = float(input("Введите число b, которое должно быть больше числа а: "))
i = 3
while i > 0:
    n = random.randint(a-1, b-1)
    i = i - 1
    print(n)
"""

"""
№12
import random
a = float(input("Введите число а: "))
b = float(input("Введите число b, которое должно быть больше числа а: "))
i = 3
while i > 0:
    n = random.randint(a-1, b)
    i = i - 1
    print(n)
"""

"""
№13
a = int(input("Введите 1 сторону: "))
b = int(input("Введите 2 сторону: "))
c = int(input("Введите 3 сторону: "))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c))**0.5 
print(s)
"""

"""
№14
from math import pi
radius = float(input("Введите радиус: "))
s = pi * (radius**2)
c = 2 * pi * radius
print(f'Площадь: {s}\nДлина окружности {c}')
"""

"""
№15
a = float(input("Введите массу апельсинов в киллограммах: "))
for n in range(30):
     a = a - (a/100)*1
print(a)
"""
