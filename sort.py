#include<
from random import randint
#>

#const()
#{
lt = []
qua = 0
#}

#int()
#{
for i in range(10):

    l = randint(0, 100)

    lt.append(l)

a = int(input("Какое число ищем? "))

for j in range(len(lt)):
    if lt[j] == a:
        qua += 1

if qua > 0:
    print(f'Найдено совподений: {qua}')
else:
    print(f'Совпадений:  {qua}')
#}
