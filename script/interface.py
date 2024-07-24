import re

from operations import BoockWorker
from models import ModelBoock


def added_boock():
    year_pattern = r'\b\d{4}\b'
    keys = ['title', 'author', 'year']
    values = []

    for key in keys:
        result = input(f'введите {key}: ')
        values.append(result)

    if re.match(year_pattern, values[-1]):        
        boock_dict = dict(zip(keys, values))
        boock = ModelBoock(**boock_dict)    
        result = BoockWorker().add_boock(boock)
        if result != None:
            print(f'книга добавленна')
        else:
            print(f'такая книга существует')
    else:
        print('год должен быть числовым значением, книга не добавлена')


def deleted_boock():
    try:    
        id = int(input('введите id книги: '))
        result = BoockWorker().del_boock(id)
        if result:
            print('книга удалена')
        print('такого id нет в базе')
    except ValueError:
        print('нужно ввести положительное число')


def finded_boock():
    keys = ['title', 'author', 'year']
    values = []

    for key in keys:
        result = input(f'введите {key}, если данный фильтр не нужен, просто нажмите enter: ')
        values.append(result)

    boock_filters = dict(zip(keys, values))
    result = BoockWorker().find_boock(**boock_filters)
    print(f'найдено {len(result)} книг')
    for _ in result:
        print(f'id:{_["id"]} Автор:{_["author"]} Название:{_["title"]} Год:{_["year"]}\n')


def showed_all_boocks():
    all_boocks = BoockWorker().show_all_boocks()
    if len(all_boocks) >=1:
        for _ in all_boocks:
            print(f'id:{_["id"]} Автор:{_["author"]} Название:{_["title"]} Год:{_["year"]} Статус:\n')
    else:
        print('библиотека пока пуста')


def changed_status_boock():
    try:
        id = int(input('Введите id книги, которой нужно поменять статус'))
        boock_changed = BoockWorker().find_boock_by_id(id)
        if boock_changed:
            if boock_changed['status'] == 'sold':
                answer = input(f'поменять статус {boock_changed["title"]}, {boock_changed["author"]} на have?')
                if answer == 'y':
                    BoockWorker().change_status_boock(id,'have')
                    print('статус книги изменен')
                else:
                    print('статус книги не изменен, так как вы нажали что-то друго кроеме "y"')
            else:
                answer = input(f'поменять статус {boock_changed["title"]}, {boock_changed["author"]} на sold?')
                if answer == 'y':
                    BoockWorker().change_status_boock(id,'sold')
                    print('статус книги изменен')
                else:    
                    print('статус книги не изменен, так как вы нажали что-то друго кроеме "y"')
        else:
            print('книги по такому id не существует')      
    except ValueError:
        print('id должно быть положительным числом')


def menu():
    welcome_fraze = '\n 1. Добавить книгу\n 2. Удалить книгу(по id)\n 3. Поск книги(название книги, автору или году)\n 4. Показать все книги \n 5. Изменение статуса книги\n'
    status = 1
    while status == True:
        cmd = input(welcome_fraze)
        if cmd == '1':
            added_boock()
        elif cmd == '2':
            deleted_boock()
        elif cmd == '3':
            finded_boock()
        elif cmd == '4':
            showed_all_boocks()
        elif cmd == '5':
            changed_status_boock()
        else:
            pass






menu()

# try:

# except ValueError: