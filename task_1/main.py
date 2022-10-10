# Игра в крестики-нолики

import emoji


def game_field(stri_1, stri_2, stri_3):
    """Функция по выведению в консоль игрового поля.
    Аргументы stri_1, stri_2, stri_3 - строки, составляющие игровое поле размерами 3x3"""
    print()
    print("-------------------------")
    print(stri_1)
    print("-------------------------")
    print(stri_2)
    print("-------------------------")
    print(stri_3)
    print("-------------------------")
    return stri_1, stri_2, stri_3

def play(move, any_string, side_of_player):
    """Функция обработки игрового хода пользователя.
    Аргументы:
    move - номер игрового поля, на которое игрок делает ход;
    any_string - строка игрового поля;
    side_of_player - bool-переменная по определению того, кто из игроков играет
    крестиками, а кто - ноликами; ее значение задается в начале игры"""
    if move == 1:
        if side_of_player == True:
            any_string = any_string.replace("1", "X")
            print(emoji.emojize("Отличный ход! :thumbs_up:"))
        else:
            any_string = any_string.replace("1", "O")
            print(emoji.emojize("Вот это да! :thumbs_up:"))
    elif move == 2:
        if side_of_player == True:
            any_string = any_string.replace("2", "X")
            print(emoji.emojize("Поставил в тупик! :thumbs_up:"))
        else:
            any_string = any_string.replace("2", "O")
            print(emoji.emojize("Шикарный замысел! :thumbs_up:"))
    elif move == 3:
        if side_of_player == True:
            any_string = any_string.replace("3", "X")
            print(emoji.emojize("Поразил! :thumbs_up:"))
        else:
            any_string = any_string.replace("3", "O")
            print(emoji.emojize("Невероятно! :thumbs_up:"))
    elif move == 4:
        if side_of_player == True:
            any_string = any_string.replace("4", "X")
            print(emoji.emojize("Грандиозно! :thumbs_up:"))
        else:
            any_string = any_string.replace("4", "O")
            print(emoji.emojize("Потрясающе! :thumbs_up:"))
    elif move == 5:
        if side_of_player == True:
            any_string = any_string.replace("5", "X")
            print(emoji.emojize("Сделал то, что должен был! :thumbs_up:"))
        else:
            any_string = any_string.replace("5", "O")
            print(emoji.emojize("Прямой дорогой к победе! :thumbs_up:"))
    elif move == 6:
        if side_of_player == True:
            any_string = any_string.replace("6", "X")
            print(emoji.emojize("Вижу победу на горизонте! :thumbs_up:"))
        else:
            any_string = any_string.replace("6", "O")
            print(emoji.emojize("Не ожидал! :thumbs_up:"))
    elif move == 7:
        if side_of_player == True:
            any_string = any_string.replace("7", "X")
            print(emoji.emojize("Победа близится! :thumbs_up:"))
        else:
            any_string = any_string.replace("7", "O")
            print(emoji.emojize("А тебя не проведешь! :thumbs_up:"))
    elif move == 8:
        if side_of_player == True:
            any_string = any_string.replace("8", "X")
            print(emoji.emojize("Хитрый ход! :thumbs_up:"))
        else:
            any_string = any_string.replace("8", "O")
            print(emoji.emojize("Вот что значит прекрасно выбранная стратегия! :thumbs_up:"))
    elif move == 9:
        if side_of_player == True:
            any_string = any_string.replace("9", "X")
            print(emoji.emojize("Мастер! :thumbs_up:"))
        else:
            any_string = any_string.replace("9", "O")
            print(emoji.emojize("В предвкушении победы! :thumbs_up:"))
    return any_string

def check_win(user_list, user_win):
    """Функция по проверке наличия победной комбинации.
    Аргументы:
    user_list - список, составленный из элементов игрового поля, на которых игрок расположил свой
    игровой знак (крестик или нолик);
    user_win - bool-переменная, заканчивающая игру при значении true"""
    if user_list == [1, 2, 3]\
        or user_list == [1, 3, 2] \
        or user_list == [2, 1, 3] \
        or user_list == [2, 3, 1] \
        or user_list == [3, 2, 1] \
        or user_list == [3, 1, 2] \
        or user_list == [1, 4, 7] \
        or user_list == [1, 7, 4] \
        or user_list == [4, 1, 7] \
        or user_list == [4, 7, 1] \
        or user_list == [7, 1, 4] \
        or user_list == [7, 4, 1] \
        or user_list == [1, 5, 9] \
        or user_list == [1, 9, 5] \
        or user_list == [5, 1, 9] \
        or user_list == [5, 9, 1] \
        or user_list == [9, 1, 5] \
        or user_list == [9, 5, 1] \
        or user_list == [4, 5, 6] \
        or user_list == [4, 6, 5] \
        or user_list == [5, 4, 6] \
        or user_list == [5, 6, 4] \
        or user_list == [6, 4, 5] \
        or user_list == [6, 5, 4] \
        or user_list == [7, 8, 9] \
        or user_list == [7, 9, 8] \
        or user_list == [8, 7, 9] \
        or user_list == [8, 9, 7] \
        or user_list == [9, 7, 8] \
        or user_list == [9, 8, 7] \
        or user_list == [3, 5, 7] \
        or user_list == [3, 7, 5] \
        or user_list == [5, 3, 7] \
        or user_list == [5, 7, 3] \
        or user_list == [7, 3, 5] \
        or user_list == [7, 5, 3] \
        or user_list == [2, 5, 8] \
        or user_list == [2, 8, 5] \
        or user_list == [5, 2, 8] \
        or user_list == [5, 8, 2] \
        or user_list == [8, 2, 5] \
        or user_list == [8, 5, 2] \
        or user_list == [3, 6, 9] \
        or user_list == [3, 9, 6] \
        or user_list == [6, 3, 9] \
        or user_list == [6, 9, 3] \
        or user_list == [9, 3, 6] \
        or user_list == [9, 6, 3]:\
        user_win = True
    return user_win

str_1 = "   1       2       3    "
str_2 = "   4       5       6    "
str_3 = "   7       8       9    "

user_choice = int(input("Игра в крестики-нолики\n"
                        "Нажмите 1, если хотите сыграть с другим пользователем, "
                         "или нажмите 2, если хотите сыграть с компьютером:\n"))
while user_choice not in range(1, 3):
    user_choice = int(input("Вы ввели неверное число. Попробуйте еще раз: "))
win = False
step = 0
if user_choice == 1:
    player_1 = str(input("Введите имя игрока, играющего крестиками: "))
    print(emoji.emojize(f"Привет, {player_1}! :red_heart:"))
    user_list_1 = list()
    user_side_1 = True
    player_2 = str(input("Введите имя игрока, играющего ноликами: "))
    print(emoji.emojize(f"Привет, {player_2}! :red_heart:"))
    user_list_2 = list()
    user_side_2 = False
    game_range = list(range(1, 10))

    print()
    print("-------------------------")
    print(str_1)
    print("-------------------------")
    print(str_2)
    print("-------------------------")
    print(str_3)
    print("-------------------------")

    while win == False:
        game_move = int(input(f"На какую клетку вы хотите поставить свой знак, {player_1}? "))
        while game_move not in game_range:
            game_move = int(input("Такой клетки нет на игровом поле или она уже занята! Попробуйте снова: "))
        str_1 = play(game_move, str_1, user_side_1)
        str_2 = play(game_move, str_2, user_side_1)
        str_3 = play(game_move, str_3, user_side_1)
        game_range.remove(game_move)
        user_list_1.append(game_move)
        game_field(str_1, str_2, str_3)
        win = check_win(user_list_1, win)
        if win == True:
            print(emoji.emojize(f"{player_1} победил(а)! :thumbs_up:"))
            break
        step += 1
        if step >= 9:
            print("Ничья!")
            break
        game_move = int(input(f"На какую клетку вы хотите поставить свой знак, {player_2}? "))
        while game_move not in game_range:
            game_move = int(input("Такой клетки нет на игровом поле или она уже занята! Попробуйте снова: "))
        str_1 = play(game_move, str_1, user_side_2)
        str_2 = play(game_move, str_2, user_side_2)
        str_3 = play(game_move, str_3, user_side_2)
        game_range.remove(game_move)
        user_list_2.append(game_move)
        game_field(str_1, str_2, str_3)
        win = check_win(user_list_2, win)
        if win == True:
            print(emoji.emojize(f"{player_2} победил(а)! :thumbs_up:"))
            break
        step += 1
        if step >= 9:
            print("Ничья!")
            break

elif user_choice == 2:
    player = str(input("Введите ваше имя: "))
    print(emoji.emojize(f"Привет, {player}! :red_heart:"))
    player_list = list()
    player_side = False

    from random import randint
    cpu_choice = list()
    cpu_side = False

    game_range = list(range(1, 10))

    side = int(input("Вы хотите сыграть крестиками или ноликами? Нажмите 1, если хотите сыграть крестиками, "
                     "или нажмите 2, если хотите сыграть ноликами: "))
    while side not in range(1, 3):
        side = int(input("Вы ввели неверное число. Попробуйте еще раз: "))
    game_range = list(range(1, 10))

    print()
    print("-------------------------")
    print(str_1)
    print("-------------------------")
    print(str_2)
    print("-------------------------")
    print(str_3)
    print("-------------------------")

    if side == 1:
        player_side = True
        while win == False:
            game_move = int(input(f"На какую клетку вы хотите поставить свой знак, {player}? "))
            while game_move not in game_range:
                game_move = int(input("Такой клетки нет на игровом поле или она уже занята! Попробуйте снова: "))
            str_1 = play(game_move, str_1, player_side)
            str_2 = play(game_move, str_2, player_side)
            str_3 = play(game_move, str_3, player_side)
            game_range.remove(game_move)
            player_list.append(game_move)
            game_field(str_1, str_2, str_3)
            win = check_win(player_list, win)
            if win == True:
                print(emoji.emojize(f"{player} победил(а)! :thumbs_up:"))
                break
            step += 1
            if step >= 9:
                print("Ничья!")
                break
            game_move = randint(1, 10)
            while game_move not in game_range:
                game_move = randint(1, 10)
            str_1 = play(game_move, str_1, cpu_side)
            str_2 = play(game_move, str_2, cpu_side)
            str_3 = play(game_move, str_3, cpu_side)
            game_range.remove(game_move)
            cpu_choice.append(game_move)
            game_field(str_1, str_2, str_3)
            win = check_win(cpu_choice, win)
            if win == True:
                print(f"Компьютер победил(а)!")
                break
            step += 1
            if step >= 9:
                print("Ничья!")
                break
    if side == 2:
        cpu_side = True
        while win == False:
            game_move = randint(1, 10)
            while game_move not in game_range:
                game_move = randint(1, 10)
            str_1 = play(game_move, str_1, cpu_side)
            str_2 = play(game_move, str_2, cpu_side)
            str_3 = play(game_move, str_3, cpu_side)
            game_range.remove(game_move)
            cpu_choice.append(game_move)
            game_field(str_1, str_2, str_3)
            win = check_win(cpu_choice, win)
            if win == True:
                print(f"Компьютер победил(а)!")
                break
            step += 1
            if step >= 9:
                print("Ничья!")
                break
            game_move = int(input(f"На какую клетку вы хотите поставить свой знак, {player}? "))
            while game_move not in game_range:
                game_move = int(input("Такой клетки нет на игровом поле или она уже занята! Попробуйте снова: "))
            str_1 = play(game_move, str_1, side)
            str_2 = play(game_move, str_2, side)
            str_3 = play(game_move, str_3, side)
            game_range.remove(game_move)
            player_list.append(game_move)
            game_field(str_1, str_2, str_3)
            win = check_win(player_list, win)
            if win == True:
                print(emoji.emojize(f"{player} победил(а)! :thumbs_up:"))
                break
            step += 1
            if step >= 9:
                print("Ничья!")
                break