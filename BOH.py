def binary(number):
    result = ""
    while number != 0:
        result += str(number % 2)
        number //= 2
    return result[::-1]


def octal(number):
    result = ""
    while number != 0:
        result += str(number % 8)
        number //= 8
    return result[::-1]


def hex(number):
    result = ""
    while number != 0:
        res = number % 16
        repl = [chr(i) for i in range(97, 123)]
        if res > 9:
            res = repl[res - 10].upper()
        result += str(res)
        number //= 16
    return result[::-1]


print("Перевод десятичных чисел в двоичную, восьмеричную и шестнадцатеричную системы счисления")
number = int(input("Введите число:\n|> "))
print(binary(number))
print(octal(number))
print(hex(number))
