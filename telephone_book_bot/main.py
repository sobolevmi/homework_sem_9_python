import telebot
import config
import file_work

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text="Добро пожаловать! Я - ваш персональный телефонный справочник-бот!\n"
                                                        "Чтобы работать со мной:\n"
                                                        "1. Для добавления информации о новом контакте введите команду: /add\n"
                                                        "2. Для просмотра информации о контактах введите команду: /view\n"
                                                        "3. Для экспорта данных из справочника введите команду: /export\n")


@bot.message_handler(commands=["add"])
def start_addition(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text="Для добавления информации в справочник в следующем формате:\n"
                                                        "\n"
                                                        "Фамилия,\n"
                                                        "Имя,\n"
                                                        "Номер телефона,\n"
                                                        "Описание введенного номера\n"
                                                        "\n"
                                                        "Введите команду: /add_column\n"
                                                        "\n"
                                                        "Для добавления информации в справочник в следующем формате:\n"
                                                        "\n"
                                                        "Фамилия, Имя, Номер телефона, Описание введенного номера\n"
                                                        "\n"
                                                        "Введите команду: /add_row\n"
                                                        "\n"
                                                        "Алгоритм добавления нового контакта:\n"
                                                        "1. Отправьте фамилию контакта. Дождитесь моего ответа\n"
                                                        "2. Отправьте имя контакта. Дождитесь моего ответа.\n"
                                                        "3. Отправьте контактный номер телефона. Дождитесь моего ответа.\n"
                                                        "4. Отправьте комментарий к номеру телефона. Дождитесь моего ответа.\n"
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
            file_work.add_to_file_column(text)
        else:
            file_work.add_to_file_column("\n")
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
            file_work.add_to_file_row(text)
        else:
            file_work.add_to_file_row("\n")
            bot.send_message(chat_id=message.from_user.id, text="Вы отлично справились! Введите команду, "
                                                                "чтобы продолжить работать со мной")


@bot.message_handler(commands=["view"])
def view_file(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text="Если данные контактов записаны в справочнике в формате столбца, введите команду /view_column\n"
                                                        "Если данные контактов записаны в справочнике в формате строчек, введите команду /view_row\n")


@bot.message_handler(commands=["view_column"])
def view_column(message: telebot.types.Message):
    result_view_column = " "
    result_view_column = file_work.view_file_column(result_view_column)
    bot.send_message(chat_id=message.from_user.id, text=result_view_column)


@bot.message_handler(commands=["view_row"])
def view_row(message: telebot.types.Message):
    result_view_row = " "
    result_view_row = file_work.view_file_row(result_view_row)
    bot.send_message(chat_id=message.from_user.id, text=result_view_row)


@bot.message_handler(commands=["export"])
def view_file(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text="Если данные контактов записаны в справочнике в формате столбца, введите команду /export_column\n"
                                                        "Если данные контактов записаны в справочнике в формате строчек, введите команду /export_row\n")


@bot.message_handler(commands=["export_column"])
def export_column(message: telebot.types.Message):
    file_work.export_file_column()
    bot.send_message(chat_id=message.from_user.id, text="Ваши данные успешно экспортированы!")


@bot.message_handler(commands=["export_row"])
def export_row(message: telebot.types.Message):
    file_work.export_file_row()
    bot.send_message(chat_id=message.from_user.id, text="Ваши данные успешно экспортированы!")


bot.polling()