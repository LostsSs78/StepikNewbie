from random import *


def programm_start(border):
    return randint(1, border), 0, border


def is_vaild(text):
    if text.isdigit() and 1 <= int(text) <= 100:
        return True
    else:
        return False


print("ДОБРО ПОЖАЛОВАТЬ В 'УГАДАЙКУ'!")
number, tryies, border = programm_start(int(input("ВВЕДИТЕ ВЕРХНЮЮ ГРАНИЦУ ЧИСЕЛ:::")))
while True:
    print("КОЛИЧЕСТВО ПОПЫТОК: " + str(tryies))
    inp = input("|> ВВЕДИТЕ ЧИСЛО МЕЖДУ 1 И {}:::".format(border))
    if is_vaild(inp):
        if int(inp) == number:
            print("ПОБЕДА")
            choise = input("ВЫ ХОТИТЕ НАЧАТЬ ЗАНОВО(Д - ДА, Н - НЕТ):::")
            if choise == "Д":
                number, tryies, border = programm_start(int(input("ВВЕДИТЕ ВЕРХНЮЮ ГРАНИЦУ ЧИСЕЛ:::")))
                continue
            else:
                break
        elif int(inp) > number:
            print("ПОПРОБУЙТЕ ЧИСЛО ПОМЕНЬШЕ")
            tryies += 1
            continue
        elif int(inp) < number:
            print("ПОПРОБУЙТЕ ЧИСЛО ПОБОЛЬШЕ")
            tryies += 1
            continue
    else:
        print("ВВЕДИТЕ ЧИСЛО МЕЖДУ 1 И {}".format(border))
        continue
