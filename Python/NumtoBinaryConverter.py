
decimal = []
myNumber = decimal.append(int(input('Enter a number: ')))
length = len(decimal)


def convert(num):
    if num >= 1:
        convert(num // 2)
    print(num % 2, end='')


for i in range(length):
    convert(decimal[i])




