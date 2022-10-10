def add_to_file_column(any_string):
    """Функция по добавлению информации о контакте в файл в формате '1 контакт - 4 строки'.
    Аргумент any_string - введенная пользователем информация о контакте"""
    with open("telephone_book_1.txt", "a") as file:
        file.write(any_string + "\n")


def add_to_file_row(any_string):
    """Функция по добавлению информации о контакте в файл в формате '1 контакт - 1 строка'.
    Аргумент any_string - введенная пользователем информация о контакте"""
    with open("telephone_book_2.txt", "a") as file:
        file.write(any_string + " ")


def view_file_column(result_view):
    """Функция по выводу информации о контактах в формате '1 контакт - 4 строки'.
    Аргумент result_view - пустая строка, в которую запишется вся информация из файла"""
    with open("telephone_book_1.txt", "r") as file:
        for line in file:
            result_view = result_view + line
        if result_view == " ":
            result_view = "В справочнике нет ни одного контакта"
    return result_view


def view_file_row(result_view):
    """Функция по выводу информации о контактах в формате '1 контакт - 1 строка'.
    Аргумент result_view - пустая строка, в которую запишется вся информация из файла"""
    with open("telephone_book_2.txt", "r") as file:
        for line in file:
            result_view = result_view + line
        if result_view == " ":
            result_view = "В справочнике нет ни одного контакта"
    return result_view


def export_file_column():
    """Функция по экспорту информации о контактах в формате '1 контакт - 4 строки'"""
    with open("telephone_book_1.txt", "r") as old_file:
        with open("export_telephone_book_1.txt", "a") as new_file:
            for line in old_file:
                new_file.write(line)

def export_file_row():
    """Функция по экспорту информации о контактах в формате '1 контакт - 1 строка'"""
    with open("telephone_book_2.txt", "r") as old_file:
        with open("export_telephone_book_2.txt", "a") as new_file:
            for line in old_file:
                new_file.write(line)