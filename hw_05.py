from collections import Counter, deque

print('===============Задание-1===============')

num_ = int(input('Сколько предприятий? '))
items_ = {}
sum_all = Counter()

for i in range(num_):
    title = input(f'Предприятие {i + 1}. Название: ')
    sum_ = (
            int(input('Прибыль за квартал 1: ')) +
            int(input('Прибыль за квартал 2: ')) +
            int(input('Прибыль за квартал 3: ')) +
            int(input('Прибыль за квартал 4: '))
            )
    avg_ = sum_ / 4

    items_[title] = Counter(
        {
        'sum_': sum_,
        'avg_': avg_
        }
    )
    sum_all += items_[title] 

avg_all = sum_all['sum_'] / num_
print(f'Средняя прибыль за год: {avg_all}')

high = {j for j in items_ if items_[j]['sum_'] >= avg_all}
low = set(items_.keys()) - set(high)
print(f'Выше среднего: {high}')
print(f'Ниже среднего: {low}')

print('===============Задание-2===============')

LIST_HEX = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

def hex_dec(hex_num):
    hex_list = deque(hex_num)
    hex_list.reverse()
    dec_sum = 0
    mult = 0
    for i in hex_list:
        num_index = LIST_HEX.index(i.upper())
        if mult != 0:
            dec_sum += num_index * (16 ** mult)
        else:
            dec_sum += num_index
        mult += 1
    return dec_sum

def dec_hex(dec_num):
    list_num = []

    whole = dec_num // 16
    remain = dec_num % 16

    if whole == 0 and remain == 0:
        list_num.append(0)

    while whole != 0 or remain != 0:
        if whole > 15:
            list_num.append(LIST_HEX[remain])
            remain = whole % 16
            whole = whole // 16
        else:
            list_num.append(LIST_HEX[remain])
            list_num.append(LIST_HEX[whole])
            whole = 0
            remain = 0

    result = deque(list_num)
    result.reverse()
    return list(result)

input_num1 = list(input('Введите первое шестнадцатиричное число: '))
input_num2 = list(input('Введите второе шестнадцатиричное число: '))

print('Первое число: ', input_num1)
print('Второе число: ', input_num2)

num1_dec = hex_dec(input_num1)
num2_dec = hex_dec(input_num2)

print('Сумма чисел равна: ', dec_hex(num1_dec + num2_dec))
print('Произведение чисел равно: ', dec_hex(num1_dec * num2_dec))
