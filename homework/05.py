#Даны два файла, в каждом из которых находится запись многочлена. 
#Задача - сформировать файл, содержащий сумму многочленов
a='10*x^2+4*x+17=0'
b='3*x^2+36*x+24=0'
data=open('f1','w')
data.writelines(a)
data.close()
data=open('f2','w')
data.writelines(b)
data.close()
a=''
a2=''
data=open('f1','r')
dat=open('f2','r')
for i in data:
    a+=i
for i in dat:
    a2+=i
data.close()
dat.close()
a2=a2[:-2]
a=a[:-2]
import re
a=re.split('[**|*|+]',a)
a2=re.split('[**|*|+]',a2)
print(a,a2)
with open('result','w') as d:
    d.write(str(int(a[0])+int(a2[0]))+'*'+a[1]+'+'+str(int(a[2])+int(a2[2]))+'*'+a[3]+'+'+str(int(a[4])+int(a2[4]))+'=0')