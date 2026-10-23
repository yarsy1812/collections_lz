import pandas as pd
print("=== АДРЕСНАЯ КНИГА ===")
# Создаем пустую таблицу с нужными колонками
columns = ['Адрес', 'Телефон', 'Дата рождения']
address_book = pd.DataFrame(columns=columns)
address_book.index.name = 'ФИО'
# Переменная для работы цикла меню
running = True
while running == True:
    print("\nМЕНЮ:")
    print("1. Показать все контакты")
    print("2. Добавить контакт")
    print("3. Удалить контакт")
    print("4. Изменить контакт")
    print("5. Выйти")
    choice = str(input("Выберите действие (1-5): "))
    #если выбрал список контактов
    if choice == '1':
        print("\n--- Список контактов ---")
        # проверим пустой ли датафрейм
        rows_count = 0
        for index in address_book.index:
            rows_count += 1
        if rows_count == 0:
            print("Книга пуста!")
        else:
            print(address_book)
            #если выбрал добавить контакт
    elif choice == '2':
        #просим данные
        print("\n--- Добавление нового контакта ---")
        fio = str(input("Введите ФИО: "))
        adres = str(input("Введите Адрес: "))
        phone = str(input("Введите Телефон: "))
        bday = str(input("Введите Дату рождения: "))
        new_data = [adres, phone, bday]
        address_book.loc[fio] = new_data
        #выводим что все успешно
        print("Контакт успешно добавлен!")
        #если выбрал удалить
    elif choice == '3':
        print("\n--- Удаление контакта ---")
        fio = str(input("Введите ФИО для удаления: "))
        is_exist = False
        if fio in address_book.index:
            is_exist = True
        if is_exist == True:
            address_book = address_book.drop(fio)
            #выводим результат
            print("Контакт удален!")
        else:
            #если нет такого контакта
            print("Такого человека нет в списке!")
            #если выбрал изменить контакт
    elif choice == '4':
        print("\n--- Изменение контакта ---")
        fio = str(input("Введите ФИО контакта, который хотите изменить: "))
        # проверка 
        find_status = False
        if fio in address_book.index:
            find_status = True
            #если контакт есть меняем
        if find_status == True:
            print("Введите новые данные:")
            adres = str(input("Новый адрес: "))
            phone = str(input("Новый телефон: "))
            bday = str(input("Новая дата рождения: "))
            updated_data = [adres, phone, bday]
            address_book.loc[fio] = updated_data
            print("Данные изменены!")
            #если нет контакта
        else:
            print("Такого человека нет в списке!")
            #если выбрал выйти из команды
    elif choice == '5':
        print("Выход из программы.")
        running = False
        #проверка что ввел номер от 1 до 5
    else:
        print("Неверная команда, введите число от 1 до 5!")
        pass
