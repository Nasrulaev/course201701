king = {
    'Стивен Кинг':
        ['Оно','Сияние','Кэрри','Противостояние','Мизери']}
rowling = {
    'Дж.К.Роулинг':['Гарри Поттер и Философский камень','Гарри Поттер и Тайная комната','Гарри Поттер и Узник Азкабана','Гарри Поттер и Кубок огня',
    'Гарри Поттер и Орден Феникса','Гарри Поттер и Принц-полукровка','Гарри Поттер и Дары Смерти']}
other = {}
print('Данные для входа в тестовый аккаунт\n'
'Логин:test\n'
'Пароль:тест\n')


log = input('У вас есть аккаунт?:'.lower())
if log == 'да':
    login = input('Введите логин:')
    password = input('Введите пароль:')
    if login == 'test' and password == 'test':
        print('Вы авторизовались.Доступный список:')
        while True:
            list = ['1.Добавить автора и книгу','2.Посмотреть доступных авторов']
            for i in list:
                print(i)
            choice = input('Ваш выбор: ')
            if choice == '1':
                name = input('Введите имя автора:')
                book = input('Введите название книги:')
                other[name] = book
            if choice == '2':
                print('Книги Стивена Кинга:')
                for i in king['Стивен Кинг']:
                   print(i)
                print('\n\n\nКниги Дж.К.Роулинг:')
                for i in rowling['Дж.К.Роулинг']:
                    print(i)
                print('Книги', name)
                print(other[name])
            else:
                print('Такого пункта нет')

else:
    print('Ваши права будут ограничены.\n'
'Вы не сможете добавлять книги и авторов')
    while True:
        list = ['1.Добавить автора и книгу', '2.Посмотреть доступных авторов']
        for i in list:
            print(i)
        choice_unlog = input('Ваш выбор:')
        if choice_unlog == '1':
            print('Недоступно для неавторизованных пользователей, используйте тестовый аккаунт.')
        if choice_unlog == '2':
            print('Книги Стивена Кинга:')
            for i in king['Стивен Кинг']:
                print(i)
            print('\n\n\nКниги Дж.К.Роулинг:')
            for i in rowling['Дж.К.Роулинг']:
                print(i)
        if choice_unlog != '1' and choice_unlog != '2':
            print('Такого пункта нет.')