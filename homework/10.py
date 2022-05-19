# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

num = int(input("Введите число: "))
a = [i for i in range(2,num) if not num % i ] # поиск всех множителей числа
print(f'Множители числа {num}: {a}')
def prime(x):                 # метод проверки числа на простое
    count=0
    for i in range(2,x//2+1):
        if x%i==0:
            count+=1
    if count==0:
        return(x) 
[print(f'Простыми числами из множителей числа {num} являются {list(filter(lambda x: x!=None, map(prime,a)))}')] # map применяет метод проверки простого числа к списку с множителями, filter оставляет элементы, содержащие значение
