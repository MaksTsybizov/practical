# Практическая 1 / 10 вар 
# Задание 1 Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение, иначе сообщение об их отсутствии.

from random import randint
lst = [randint(1,10) for i in range(10)]
print(lst)
AAA = [i for i in set(lst) if lst.count(i) > 1]
if len(AAA) == 0:
   print("Повторяющихся элементов нет")
else:
   print(AAA)
   
   
   
# Задание 2 
arr = [1, 2, 3, 10, 20, 23, 43, 5, 6, 7]    # и т.д.
print(*arr)
print(*[0 if i < 10 else 1 if i > 20 else i for i in arr])
