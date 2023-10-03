number = input()
to_decimal = 0
index = -1

for i in range(len(number)):
    to_decimal += int(number[index]) * 2 ** i
    index -= 1

print(to_decimal)