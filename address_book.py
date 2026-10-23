import pandas as pd
print("=== АДРЕСНАЯ КНИГА ===")
# Создаем пустую таблицу с нужными колонками
# Задаем ФИО как индекс (главную колонку)
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
    choice = input("Выберите действие (1-5): ")
    if choice == '1':
        print("\n--- Список контактов ---")
        if len(address_book) == 0:
            print("Книга пуста!")
        else:
            print(address_book)
    elif choice == '2':
        print("\n--- Добавление нового контакта ---")
        fio = input("Введите ФИО: ")
        adres = input("Введите Адрес: ")
        phone = input("Введите Телефон: ")
        bday = input("Введите Дату рождения: ")
        # Добавляем строку в таблицу
        address_book.loc[fio] = [adres, phone, bday]
        print("Контакт успешно добавлен!")
    elif choice == '3':
        print("\n--- Удаление контакта ---")
        fio = input("Введите ФИО для удаления: ")
        # Проверяем, есть ли такое ФИО в списке
        if fio in address_book.index:
            address_book = address_book.drop(fio)
            print("Контакт удален!")
        else:
            print("Такого человека нет в списке!")
    elif choice == '4':
        print("\n--- Изменение контакта ---")
        fio = input("Введите ФИО контакта, который хотите изменить: ")
        if fio in address_book.index:
            print("Введите новые данные:")
            adres = input("Новый адрес: ")
            phone = input("Новый телефон: ")
            bday = input("Новая дата рождения: ")
            # Перезаписываем данные по этому ФИО
            address_book.loc[fio] = [adres, phone, bday]
            print("Данные изменены!")
        else:
            print("Такого человека нет в списке!")
    elif choice == '5':
        print("Выход из программы.")
        running = False
    else:
        print("Неверная команда, введите число от 1 до 5!")
