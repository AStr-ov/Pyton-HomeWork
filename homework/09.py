#Реализуйте RLE алгоритм:реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.

s='AVEGOOMUURRRKS'              
# with open('str_chars','w') as d:  #создание исходного файла
#     d.writelines(s)
print(f'Текст исходного файлы - {s}') 
       
from_file = ''  # прмежуточная переменная-строка (для удобства) 
d= open('str_chars','r')
for i in d:
    from_file += i  # копирование данных исходного файла
d.close()

with open('rle','w') as data:             # запись в файл
        for i in range(len(from_file)):   # модуль сжатия
            if from_file[i] != from_file[i-1]:
                data.write(str(from_file.count(from_file[i])))
                data.write(from_file[i])
                
kod = ''       # прмежуточная переменная-строка (для удобства)         
g=open('rle','r')
for i in g:
    kod += i  # копирование из файла с результатом сжатия
print(f'Результат работы модуля сжатия RLE - {kod}')

with open('again','w') as data:    # запись в файл 
    for i in range(0,len(kod),2):  #модуль восстановления
        data.write(int(kod[i])*kod[i+1])
