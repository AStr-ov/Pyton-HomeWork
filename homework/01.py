# Вычислить число Пи c заданной точностью
def Pi(num):
    import math
    print(f'Число Пи с {num} знаками после запятой: {round(math.pi,num)}')
Pi(7)