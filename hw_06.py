import random
import mem_info as sm

print('==================Задача-1==================')

n = input('Введите трехзначное число: ')
sum = 0
for i in n:
    sum += int(i)
print('Сумма цыфр числа: ', sum)

sm.get_size(n, sum)

print('==================Задача-2==================')

print("Координаты точки A(x1; y1):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))
 
print("Координаты точки B(x2; y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))
 
print("Уравнение прямой, проходящей через эти точки:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2
print(" y = %.2f*x + %.2f" % (k, b))

sm.get_size(x1, y1, x2, y2, k, b)

print('==================Задача-3==================')

a = int(input('Введите первое число диапазона\n'))
b = int(input('Введите второе число диапазона\n'))
 
print(f'Случайное число из выбранного вами диапазона = {random.randint(a, b)}')
 
# случайное вещественное число;
 
a = float(a)
b = float(b)
num = random.uniform(a, b)
 
print(f"Случайное вещественное число из выбранного вами диапазона = {format(num, '.3f')}")
 
# случайный символ.
 
let1 = input('Введите первую букву диапазона (английские, нижний регистр)\n')
let2 = input('Введите вторую букву диапазона (английские, нижний регистр)\n')
 
alph = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
let1_ind = alph.index(let1)
let2_ind = alph.index(let2)
 
rand_let = alph[random.randint(let1_ind, let2_ind)]
 
print(f'Случайная буква из выбранного вами дипазона - "{rand_let}"')


sm.get_size(a, b, let1, let2, alph, let1_ind, let2_ind, rand_let)


