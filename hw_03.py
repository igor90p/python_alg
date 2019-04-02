
from random import random

print('===============Задание-1===============')

a = [0]*8
for i in range(2,100):
    for j in range(2,10):
        if i%j == 0:
            a[j-2] += 1
i = 0
while i < len(a):
    print(i+2, ' - ', a[i])
    i += 1

print('===============Задание-2===============')

N = 10
arr = [0]*N
even = []
for i in range(N):
    arr[i] = int(random() * 10) + 10
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)

print('===============Задание-3===============')

N = 15
arr = [0]*N
for i in range(N):
    arr[i] = int(random()*100)
    print(arr[i],end=' ')
print()
 
mn = 0
mx = 0
for i in range(N):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
print('arr[%d]=%d arr[%d]=%d' % (mn+1, arr[mn], mx+1, arr[mx]))
b = arr[mn]
arr[mn] = arr[mx]
arr[mx] = b
 
for i in range(15):
    print(arr[i],end=' ')
print()

print('===============Задание-4===============')

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
print(arr)
 
num = arr[0]
max_frq = 1
for i in range(N-1):
    frq = 1
    for k in range(i+1,N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]
 
if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')

print('===============Задание-5===============')

N = 15
arr = []
for i in range(N):
        arr.append(int(random() * 100) - 50)
print(arr)
 
i = 0
index = -1
while i < N:
        if arr[i] < 0 and index == -1:
                index = i
        elif arr[i] < 0 and arr[i] > arr[index]:
                index = i
        i += 1
 
print(index+1,':', arr[index])

print('===============Задание-6===============')

N = 10
a = [0]*N
for i in range(N):
    a[i] = int(random()*50)
    print('%3d' % a[i], end='')
print()

min_id = 0
max_id = 0
for i in range(1,N):
    if a[i] < a[min_id]:
        min_id = i 
    elif a[i] > a[max_id]:
        max_id = i
print(a[min_id], a[max_id])

if min_id > max_id:
    min_id, max_id = max_id, min_id

summ = 0
for i in range(min_id+1, max_id):
    summ += a[i]
print(summ)

print('===============Задание-7===============')

N = 10
a = []
for i in range(N):
    a.append(int(random()*100))
    print("%3d" % a[i], end='')
print()
 
if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0
    
for i in range(2,N):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i
        
print("№%3d:%3d" % (min1+1, a[min1]))
print("№%3d:%3d" % (min2+1, a[min2]))

print('===============Задание-8===============')

M = 5
N = 4
a = []
for i in range(N):
    b = []
    s = 0
    print("%d-я строка:" % i)
    for j in range(M-1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    a.append(b)
 
for i in a:
    print(i)

print('===============Задание-9===============')

N = 15
M = 10
arr = []
for i in range(N):
    lst = []
    for j in range(M):
        lst.append(int(random() * 256))
    arr.append(lst)
for i in range(N):
    for j in range(M):
        print(" |%3d| " % arr[i][j], end='')
    print()
for i in range(M):
    print(" ----- ", end='')
print()
for j in range(M):
    mx = arr[0][j]
    for i in range(N):
        if arr[i][j] > mx:
            mx = arr[i][j]
    print(" |%3d| " % mx, end='')
print()
