# 1. Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141

from math import pi

def roundNum(num) -> float:
  count = 0
  while num != 1:
    num *= 10
    count += 1
  result = int(pi*(10**count))
  result /= 10**count
  return result

digit = float(input('Введите вешествено число точности: '))

print(roundNum(digit))



# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Input N: '))
mult = []
for i in range(2, int(number ** 0.5) + 2):
    while number % i == 0:
        mult.append(i)
        number //= i
if number != 1:
    mult.append(int(number))
print(mult)


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]


import random

myList = []
for i in range(10):
    myList.append(random.randint(1, 10))
print(myList)

newList = []
for i in myList:
    if myList.count(i) < 2:
       newList.append(i)
print(newList)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

from random import Random, randint

file = open('data1.txt','w', encoding = 'utf-8') 

k = int(input('Введите k: '))

string = ''
   
while k >= 0:
        number = randint(0, 2)
        if k > 1:
            string += f'{number}x^{k}'
        elif k == 1:
            string += f'{number}x'
        elif k == 0:
            string += f'{number} = 0'
        if k > 0:
            string += ' + '
        k -= 1 

file.write(str(string))
file.close()

print(string)




# 
# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).

from numpy.polynomial import Polynomial
from random import randint

k1 = int(input('Input K1: '))
k2 = int(input('Input K2: '))

poly1 = Polynomial([randint(-100, 100) for i in range(k1 + 1)])
poly2 = Polynomial([randint(-100, 100) for j in range(k2 + 1)])

print(poly1)
print(poly2)
summa = poly1 + poly2
print(summa)


with open('file01.txt', 'w', encoding='utf-8') as file:
    file.write(f"{poly1}")

with open('file02.txt', 'w', encoding='utf-8') as file:
    file.write(f"{poly2}")

with open('file01.txt','r') as file:
    firstPolyMath = file.readline()
    firstPoly = firstPolyMath.split()

with open('file02.txt','r') as file:
    secondPolyMath = file.readline()
    secondPoly = secondPolyMath.split()

summaPoly = poly1 + poly2

with open('summa_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'({poly1}) + ({poly2}) = {summaPoly}')