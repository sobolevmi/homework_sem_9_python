import telebot
import config

bot = telebot.TeleBot(TOKEN)

def add_to_file_column(any_string):
    with open("telephone_book_1.txt", "a") as file:
        file.write(any_string + "\n")

def add_to_file_row(any_string):
    with open("telephone_book_2.txt", "a") as file:
        file.write(any_string + " ")

@bot.message_handler(commands=["start"])
def start_message(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text="Добро пожаловать! Я - ваш персональный телефонный справочник-бот!\n"
                                                        "Чтобы работать со мной:\n"
                                                        "1. Для добавления информации о новом контакте введите команду /add\n"
                                                        "2. Для просмотра информации о контактах введите команду /view\n"
                                                        "3. Для экспорта данных из справочника введите команду /export\n")

@bot.message_handler(commands=["add"])
def start_addition(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text="Для добавления информации в справочник в следующем формате:\n"
                                                        "\n"
                                                        "Фамилия,\n"
                                                        "Имя,\n"
                                                        "Номер телефона,\n"
                                                        "Описание введенного номера\n"
                                                        "\n"
                                                        "Введите команду /add_column\n"
                                                        "\n"
                                                        "Для добавления информации в справочник в следующем формате:\n"
                                                        "\n"
                                                        "Фамилия, Имя, Номер телефона, Описание введенного номера\n"
                                                        "\n"
                                                        "Введите команду /add_row\n"
                                                        "\n"
                                                        "Алгоритм добавления нового контакта:\n"
                                                        "1. Отправьте фамилию контакта. Дождитесь моего ответа\n"
                                                        "2. Отправьте имя контакта. Дождитесь моего ответа\n"
                                                        "3. Отправьте контактный номер телефона. Дождитесь моего ответа\n"
                                                        "4. Отправьте комментарий к номеру телефона. Дождитесь моего ответа\n"
                                                        "\n"
                                                        "Чтобы завершить добавление информации о контакте, введите end\n")

@bot.message_handler(commands=["add_column"])
def addition_column(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text="Введите данные контакта")
    @bot.message_handler(func=lambda message: True)
    def add_writing_column(message: telebot.types.Message):
        text = message.text
        if text != "end":
            bot.reply_to(message, text)
            add_to_file_column(text)
        else:
            add_to_file_column("\n")
            bot.send_message(chat_id=message.from_user.id, text="Вы отлично справились! Введите команду, "
                                                            "чтобы продолжить работать со мной")

@bot.message_handler(commands=["add_row"])
def addition_row(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text="Введите данные контакта")
    @bot.message_handler(func=lambda message: True)
    def add_writing_row(message: telebot.types.Message):
        text = message.text
        if text != "end":
            bot.reply_to(message, text)
            add_to_file_row(text)
        else:
            add_to_file_row("\n")
            bot.send_message(chat_id=message.from_user.id, text="Вы отлично справились! Введите команду, "
                                                                "чтобы продолжить работать со мной")


@bot.message_handler(commands=["view"])
def view_file(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text="Если данные контактов записаны в справочнике в формате столбца, введите команду /view_column\n"
                                                        "Если данные контактов записаны в справочнике в формате строчек, введите команду /view_row\n")
@bot.message_handler(commands=["view_column"])
def view_file_column(message: telebot.types.Message):
    with open("telephone_book_1.txt", "r") as file:
        result_view_column = " "
        for line in file:
            result_view_column = result_view_column + line
        bot.send_message(chat_id=message.from_user.id, text=result_view_column)

@bot.message_handler(commands=["view_row"])
def view_file_row(message: telebot.types.Message):
    with open("telephone_book_2.txt", "r") as file:
        result_view_row = " "
        for line in file:
            result_view_row = result_view_row + line
        bot.send_message(chat_id=message.from_user.id, text=result_view_row)

@bot.message_handler(commands=["export"])
def view_file(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text="Если данные контактов записаны в справочнике в формате столбца, введите команду /export_column\n"
                                                        "Если данные контактов записаны в справочнике в формате строчек, введите команду /export_row\n")
@bot.message_handler(commands=["export_column"])
def view_file_column(message: telebot.types.Message):
    with open("telephone_book_1.txt", "r") as old_file:
        with open("export_telephone_book_1.txt", "a") as new_file:
            for line in old_file:
                new_file.write(line)
            bot.send_message(chat_id=message.from_user.id, text="Ваши данные успешно экспортированы!")

@bot.message_handler(commands=["export_row"])
def view_file_row(message: telebot.types.Message):
    with open("telephone_book_2.txt", "r") as old_file:
        with open("export_telephone_book_2.txt", "a") as new_file:
            for line in old_file:
                new_file.write(line)
            bot.send_message(chat_id=message.from_user.id, text="Ваши данные успешно экспортированы!")

bot.polling()


            #
            #     user_surname = str(input("Введите фамилию: "))
            #     file.write(str(user_surname + "\n"))
            #     user_name = str(input("Введите имя: "))
            #     file.write(str(user_name + "\n"))
            #     user_phone = str(input("Введите номер телефона: "))
            #     file.write(str(user_phone + "\n"))
            #     user_description = str(input("Введите описание номера телефона: "))
            #     file.write(str(user_description + "\n"))
            #     file.write("\n")
            # elif choice_format == "2":
            #     user_surname = str(input("Введите фамилию: "))
            #     file.write(str(user_surname + " *** "))
            #     user_name = str(input("Введите имя: "))
            #     file.write(str(user_name + " *** "))
            #     user_phone = str(input("Введите номер телефона: "))
            #     file.write(str(user_phone + " *** "))
            #     user_description = str(input("Введите описание номера телефона: "))
            #     file.write(str(user_description) + "\n")
            # elif choice_format == "q":
            #     break
            # else:
            #     while choice_format != "1" and choice_format != "2":
            #         print("Вы ввели неверное число, попробуйте снова \n")
            # continue_input = str(input("Нажмите 1, если хотите добавить еще один контакт, "
            #                             "или нажмите q, чтобы завершить добавление контактов \n"))
            # if continue_input == "q":
            #     break
            # if continue_input != "1" and continue_input != "q":
            #     while continue_input != "1" and continue_input != "q":
            #         print("Вы ввели неверное число, попробуйте снова \n")