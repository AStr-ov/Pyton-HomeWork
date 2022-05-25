import In
l_name='Введите Фамилию: '
f_name='Введите Имя: '
phone = 'Введите номер телефона: '
file = 'phone'
def add():
    with open(file,'a')as d:
        d.write(In.inn(l_name,f_name,phone))
        d.write(f'*****\n')

def read():
    with open(file,'r')as d:
        [print(i,end=' ')for i in d]

read()
def del_rec(name):
    book2 = ''
    res = ''
    with open(file,'r')as d:
        for i in d:            
            book2 += i
    with open(file,'w')as d:
        for i in book2.split('*****'):
            if name not in i:
                d.write(i)
                d.write('*****')
                    

 
    

