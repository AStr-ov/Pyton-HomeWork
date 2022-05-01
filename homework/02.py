# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
def prime_factors(num):
    list = []
    for i in range(2, num + 1):   
        for j in range(2, i):
            if i % j == 0:    #простые числа в диапазоне до n
                break
        else:
            if num % i == 0:  #множители числа n, в данном случае
                list.append(i)#выбираются из простых чисел
    print(f'Простые множители данного числа: {list}')
prime_factors(int(input('Введите числo: ')))