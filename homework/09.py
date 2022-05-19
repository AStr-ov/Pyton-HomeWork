#Реализуйте RLE алгоритм:реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.

st ='AVEGOOMMMMMMMMMMMMMMUURRRKIIIIIIIIIISS'
with open('init','w')as d:
    d.writelines(st)       # создается исходный файл с текстом
from_file = ''             # создается промежуточная переменная
with open('init','r')as d:
    for i in st:
        from_file += i     # в переменную копируются данные исходного файла
with open('kod','w') as d:
    for i in range(len(from_file)):            # модуль сжатия
        if from_file[i] != from_file[i-1]:   
            d.write(str(from_file.count(from_file[i]))) # запись в файл количества символов
            d.write(from_file[i])               # запись в файл символов
    
nums = [(from_file.count(from_file[i])) for i in range(len(from_file)) if from_file[i] != from_file[i-1]] # Список количества символов
chars = [from_file[i] for i in range(len(from_file)) if from_file[i] != from_file[i-1]]           # Список символов

with open('again','w')as d:               # запись в файл
    for i in (map(lambda x,y: x*y,nums,chars)): # модуль восстановления
        d.write(str(i))  
