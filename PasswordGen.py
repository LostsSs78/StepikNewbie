from random import *


def generate_password():
    password = ""
    print(
        "Добро пожаловать в умный генератор паролей! Я могу генерировать самые надёжные и невзламываемые пароли на "
        "свете!")
    lenght = int(input("Введите желаемую длинну пароля: \n|> "))

    symbol_en = "qwertyuiopasdfghjklzxcvbnm"
    symbol_ru = "йцукенгшщзхъфывапролджэячсмитьбю"
    Symbol_en = "QWERTYUIOPASDFGHJKLZXCVBNM"
    Symbol_ru = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
    numbers = "1234567890"
    special_sym = "!@#@$%^&*()_+-=№;%:?*{}[]<>,./"

    flag_ru = False
    flag_Ru = False
    flag_num = False
    flag_Spec = False

    print("Изначально пароль состоит только из английских букв.")
    symbols = [el for el in symbol_en]
    symbols += [el for el in Symbol_en]
    flag_eng = True
    flag_Eng = True

    if input("Хотите добавить цифры? (да или нет)\n|> ").lower().strip() == "да":
        symbols += [el for el in numbers]
        flag_num = True
    if input("Хотите добавить русские буквы? (да или нет) \n|> ").lower().strip() == "да":
        symbols += [el for el in symbol_ru]
        symbols += [el for el in Symbol_ru]
        flag_ru = True
        flag_Ru = True
    if input("Хотите добавить специальные символы? (да или нет) \n|> ").lower().strip() == "да":
        symbols += [el for el in special_sym]
        flag_Spec = True

    while flag_eng or flag_Eng or flag_ru or flag_Ru or flag_num or flag_Spec:
        password = ""
        for i in range(lenght):
            password += choice(symbols)
        for c in password:
            if c in symbol_en:
                flag_eng = False
            elif c in symbol_ru:
                flag_ru = False
            elif c in Symbol_en:
                flag_Eng = False
            elif c in Symbol_ru:
                flag_Ru = False
            elif c in numbers:
                flag_num = False
            elif c in special_sym:
                flag_Spec = False
    else:
        return password

print(generate_password())