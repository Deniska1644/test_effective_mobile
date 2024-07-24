from interface import *

def main():
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
        elif cmd == '0':
            break
            

if __name__=='__main__':
    main()