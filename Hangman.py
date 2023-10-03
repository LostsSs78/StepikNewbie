from random import *


def get_word(_list):
    return choice(_list)


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def is_valid(text):
    return text.isalpha()


def play(word):
    word_completion = ["_" for _ in range(len(word))]  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print("Давай играть в угадайку слов!")
    print(display_hangman(tries), f"\nИзначально у вас {tries} попыток!")
    print(*word_completion)

    while tries != 0:
        choice = input("Выберите, что вы хотите угадать:\n1. Букву\n2. Слово\n|> ").lower().strip()
        inp_usr = input("Угадывайте: ")
        if not is_valid(inp_usr):
            print("Вы ввели что-то не то, повторите попытку!")
            continue
        elif inp_usr in guessed_letters or inp_usr in guessed_words:
            print("Введенное Вами слово или буква уже были угаданы! Повторите снова!")
        elif inp_usr in word and (choice == "букву" or choice == "1"):
            for i in range(len(word)):
                if word[i] == inp_usr:
                    word_completion[i] = inp_usr
            guessed_letters += inp_usr
            print(display_hangman(tries))
            print(f"Вы угадали букву '{inp_usr}'!")
            print(*word_completion)
            if word_completion == [el for el in word]:
                print(f"ПОБЕДА!")
                break
        elif inp_usr == word and (choice == "слово" or choice == "2"):
            word_completion = word
            guessed_words += inp_usr
            print(f"ПОБЕДА!")
            print(*word_completion)
            break
        elif inp_usr != word and (choice == "слово" or choice == "2"):
            print(display_hangman(0))
            print(*word_completion)
            print("ВЫ ПРОИГРАЛИ!")
            break
        else:
            guessed_letters += inp_usr
            guessed_words += inp_usr
            tries -= 1
            print(f"Неплохая попытка, но нет! У вас осталось {tries} попыток!")
            print(display_hangman(tries))
            print(*word_completion)
    else:
        print("ВЫ ПРОИГРАЛИ")


word_list = ["привет", "пока", "встреча", "мама", "сестра", "мышь", "конкатенация"]

play(get_word(word_list))
