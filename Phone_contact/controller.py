import view
import action

def start():
    while True:
        view.select_act()
        if view.answer ==1:
            action.read()
        elif view.answer==2:
            action.add()
        elif view.answer==3:
            action.del_rec(input('Кого будем удалять? '))
        elif view.answer==4:
            print('Сеанс завершен')
            break
        else:
            print('Некорректный ввод')
        