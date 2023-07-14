# phonebook = {}

# def add_contact(name, phone):
#     phonebook[name] = phone
#     print("Контакт добавлен")

# def delete_contact(name):
#     if name in phonebook:
#         del phonebook[name]
#         print("Контакт удален")
#     else:
#         print("Контакт не найден")

# def search_contact(name):
#     if name in phonebook:
#         print("Номер телефона:", phonebook[name])
#     else:
#         print("Контакт не найден")

# def list_contacts():
#     if phonebook:
#         for name, phone in phonebook.items():
#             print(name + ": " + phone)
#     else:
#         print("Справочник пуст")

# while True:
#     print("\nТелефонный справочник")
#     print("1. Добавить контакт")
#     print("2. Удалить контакт")
#     print("3. Поиск контакта")
#     print("4. Показать все контакты")
#     print("5. Выйти")
    
#     select = input("Выберите действие (1-5): ")

#     if select == '1':
#         name = input("Введите имя контакта: ")
#         phone = input("Введите номер телефона: ")
#         add_contact(name, phone)
#     elif select == '2':
#         name = input("Введите имя контакта для удаления: ")
#         delete_contact(name)
#     elif select == '3':
#         name = input("Введите имя контакта для поиска: ")
#         search_contact(name)
#     elif select == '4':
#         list_contacts()
#     elif select == '5':
#         print("Программа завершена")
#         break
#     else:
#         print("Ошибка")
