def is_valid(language, action):
    res = False
    if language != "русский язык" and language != "английский язык" and language not in ['1', '2']:
        res = True
    if action != "зашифровать текст" and action != "дешифровать текст" and action not in ['1', '2']:
        res = True
    return res


def check_language(language):
    if language == "русский язык" or language == "1":
        return 1
    elif language == "английский язык" or language == "2":
        return 2


def coding(text, language, step):
    if check_language(language) == 1:
        coded = ""
        for c in text:
            if c in [chr(i) for i in range(1040, 1072)]:
                if ord(c) + step > 1071:
                    coded += chr(ord(c) + step - 32)
                else:
                    coded += chr(ord(c) + step)
            elif c in [chr(i) for i in range(1072, 1104)]:
                if ord(c) + step > 1103:
                    coded += chr(ord(c) + step - 32)
                else:
                    coded += chr(ord(c) + step)
            else:
                coded += c
        return coded
    elif check_language(language) == 2:
        coded = ""
        for c in text:
            if c in [chr(i) for i in range(65, 91)]:
                if ord(c) + step > 90:
                    coded += chr(ord(c) + step - 26)
                else:
                    coded += chr(ord(c) + step)
            elif c in [chr(i) for i in range(97, 122)]:
                if ord(c) + step > 122:
                    coded += chr(ord(c) + step - 26)
                else:
                    coded += chr(ord(c) + step)
            else:
                coded += c
        return coded


def decoding(text, language, step):
    if check_language(language) == 1:
        decoded = ""
        for c in text:
            sym = ord(c) - step
            if c in [chr(i) for i in range(1040, 1072)]:
                if sym < 1040:
                    decoded += chr(sym + 32)
                else:
                    decoded += chr(sym)
            elif c in [chr(i) for i in range(1072, 1104)]:
                if sym < 1072:
                    decoded += chr(sym + 32)
                else:
                    decoded += chr(sym)
            else:
                decoded += c
        return decoded
    elif check_language(language) == 2:
        decoded = ""
        for c in text:
            sym = ord(c) - step
            if c in [chr(i) for i in range(65, 91)]:
                if sym < 65:
                    decoded += chr(sym + 26)
                else:
                    decoded += chr(sym)
            elif c in [chr(i) for i in range(97, 123)]:
                if sym < 97:
                    decoded += chr(sym + 26)
                else:
                    decoded += chr(sym)
            else:
                decoded += c
        return decoded


print("Добро пожаловать в Шифровальну Машину Цезаря! Никто не сможет прочитать ваше письмо, кроме адресата!")
while True:
    print("Выберите язык:"
      "\n1. Русский Язык"
      "\n2. Английский Язык")

    language = input("|> ").lower().strip()

    print("Выберите действие:"
      "\n1. Зашифровать текст"
      "\n2. Дешифровать текст")

    action = input("|> ").lower().strip()

    if is_valid(language, action):
        print("Вы ввели неправильное значение, пожалуйста, повторите снова".upper())
        continue

    if check_language(language) == 1:
        max_step = 32
    elif check_language(language) == 2:
        max_step = 26

    text = input("Введите текст: \n|> ")
    if action == "зашифровать текст" or action == "1":
        step = int(input(f"Введите шаг шифрования (максимум {max_step})\n|> "))
        print(coding(text, language, step))
    elif action == "дешифровать текст" or action == "2":
        step = int(input(f"Введите шаг шифрования (максимум {max_step})\n|> "))
        print(decoding(text, language, step))

    for i in range(26):
        print(decoding("Hawnj pk swhg xabkna ukq nqj.", language, i))

