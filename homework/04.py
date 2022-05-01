# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 1 до 100) многочлена и 
# записать в файл многочлен степени k.
# k=2 => 2*x² + 4*x + 5 = 0

from random import randint
k=6
data=open('polynom','w')
while k>1:    
    data.write(str(randint(1,100))+'*x^'+str(k)+'+')
    k-=1
data.write(str(randint(1,100))+'*x+'+str(randint(1,100))+'=0')
data.close()
