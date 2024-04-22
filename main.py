def copy_contact_from_file(source_filename, destination_filename, line_number):
    try:
        with open(source_filename, 'r') as source_file:
            lines = source_file.readlines()
            if 0 < line_number <= len(lines):
                contact_to_copy = lines[line_number - 1]
                with open(destination_filename, 'a') as destination_file:
                    destination_file.write(contact_to_copy)
                print("Контакт успешно скопирован в другой файл.")
            else:
                print("Некорректный номер строки.")
    except IOError:
        print("Ошибка при чтении или записи файла.")
def display_contacts(contacts):
    if not contacts:
        print("Справочник пуст.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Телефон: {contact[3]}")


def save_contacts_to_file(contacts, filename):
    try:
        with open(filename, 'w') as file:
            for contact in contacts:
                file.write(','.join(contact) + '\n')
        print("Контакты успешно сохранены в файл.")
    except IOError:
        print("Ошибка при сохранении файла.")


def import_contacts_from_file(filename):
    contacts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                contact = line.strip().split(',')
                contacts.append(contact)
        print("Контакты успешно импортированы из файла.")
    except IOError:
        print("Ошибка при чтении файла.")
    return contacts


def search_contacts(contacts, key):
    found_contacts = []
    for contact in contacts:
        if key.lower() in [value.lower() for value in contact]:
            found_contacts.append(contact)
    return found_contacts


def add_contact(contacts):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contacts.append([surname, name, patronymic, phone])
    print("Контакт успешно добавлен.")


def main():
    contacts = []
    while True:
        print("\n1. Вывести контакты")
        print("2. Сохранить контакты в файл")
        print("3. Импортировать контакты из файла")
        print("4. Найти контакт")
        print("5. Добавить контакт")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            filename = input("Введите имя файла для сохранения: ")
            save_contacts_to_file(contacts, filename)
        elif choice == '3':
            filename = input("Введите имя файла для импорта: ")
            contacts = import_contacts_from_file(filename)
        elif choice == '4':
            key = input("Введите фамилию, имя, отчество или номер телефона для поиска: ")
            found_contacts = search_contacts(contacts, key)
            display_contacts(found_contacts)
        elif choice == '5':
            add_contact(contacts)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")


if __name__ == "__main__":
    main()
