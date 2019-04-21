import random

print('==================Задание-1==================')

n = input('Введите трехзначное число: ')
sum = 0
for i in n:
    sum += int(i)
print('Сумма цыфр числа: ', sum)

print('==================Задание-2==================')

a = 5
print("%d = %s" % (a, bin(a)))
b = 6
print("%d = %s" % (b, bin(b)))
 
print("%d & %d = %d (%s)" % (a,b,a&b,bin(a&b)))
print("%d | %d = %d (%s)" % (a,b,a|b,bin(a|b)))
print("%d ^ %d = %d (%s)" % (a,b,a^b,bin(a^b)))
print("%d << 2 = %d (%s)" % (b,b<<2,bin(b<<2)))
print("%d >> 2 = %d (%s)" % (b,b>>2,bin(b>>2)))

print('==================Задание-3==================')

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

print('==================Задание-4==================')
 
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

print('==================Задание-5==================')

print(f'Выбранные вами буквы имеют порядковые номера: '
        f'{let1} = {let1_ind}, {let2} = {let2_ind},'
            f' и между ними находятся {let2_ind - let1_ind - 1} букв')

print('==================Задание-6==================')

num1 = int(input('Введите порядковый номер буквы\n'))
 
print(f'Под номеров {num1} находится буква "{alph[num1]}"')

print('==================Задание-7==================')

a = int(input('Введите длинну отрезка А\n'))
b = int(input('Введите длинну отрезка B\n'))
c = int(input('Введите длинну отрезка C\n'))
 
if a + b <= c or a + c <= b or b + c <= a:
    print('Такой тругольник не может существовать. Сумма длинн двух сторон меньше или равна длинне третьей стороны')
elif a != b and a != c and b != c:
    print('Треугольник разносторонний')
elif a == b == c:
    print('Треугольник равносторонний')
else:
    print('Треугольник равнобедренный')

print('==================Задание-8==================')

year = input('Введите год\n')
 
if year.isdigit():
    if int(year[-2:]) % 4 == 0:
        print('Год високосный')
    else:
        print('Год не високосный')
else:
    print('Введите год ЦИФРАМИ')

print('==================Задание-9==================')

nums = []
while len(nums) != 3:
    nums.append(int(input(f'Введите число №{len(nums) + 1}\n')))
 
a, b, c = nums[0], nums[1], nums[2]
 
if a != b and b != c:
    print('Среднее число из введенных:')
    
    if a < b < c or c < b < a:
        print(f'Вариант с условиями {b}')
    elif b < a < c or c < a < b:
        print(f'Вариант с условиями {a}')
    else:
        print(f'Вариант с условиями {c}')
else:
    print('По условию все числа должны быть разными')


print('=================Доп.задания=================')
print('==================Задание-1==================')
stats = {}
with open("pwd.txt", "r") as f:
    for line in f.read().split("\n"):
        if len(line) == 0:
            continue

        login, password = line.split(";")

        if password in stats:
            stats[password] += 1
        else:
            stats[password] = 1

# print(stats)


sorted_x = sorted(stats.items(), key=lambda kv: kv[1], reverse=True)


print(sorted_x[:10])

print('==================Задание-2==================')

secret = random.randint(1, 99)
print("Отгадайте число от 1 до 100 за 10 попыток!")
tries = 10
while True:
    if tries == 0:
        print("Попытки кончились!")
        break
    guess = int(input("Твой вариант? > "))
    tries -= 1
    if guess < secret:
        print("Это слишком мало")
    elif guess > secret:
        print("Это слишком много")
    elif guess == secret:
        print("Вы угадали!")
        break
input("Press Enter to continue!")
