#Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

players = ['playerA', 'playerB']
first = (random.choice(players))
print(f'Первым ходит {first}')
players.remove(first)
second = players[0]
print(f'Вторым ходит {second}')
text=f'{first} вводит количество забираемых конфет от 1 до 28: '
text2=f'{second} вводит количество забираемых конфет от 1 до 28: ' 
count = 2021
first,second = 0, 0
print(f'Имеется {count} конфет.')
while count > 0:
    while first not in range(1,29):
        first = int(input(text))
        if first not in range(1,29):
            print('Введено некорректное значение')
    count -= first
    first = 0
    if count <=0:
        print('Поздравляем, Вы победили и забираете все конфеты')
    else:
        print(f'Имеется {count} конфет.')
        while second not in range(1,29):
            second=int(input(text2))
            if second not in range(1,29):
                print('Введено некорректное значение')
        count -= second
        second = 0
        if count <=0:
            print('Поздравляем, Вы победили и забираете все конфеты')
        else:
            print(f'Имеется {count} конфет')
            
