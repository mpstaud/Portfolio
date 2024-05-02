import pyfirmata
import time


digits = []
places = []
decimal = []
length = len(decimal)
myNumber = decimal.append(int(input('Enter a number: ')))

board = pyfirmata.Arduino('/dev/cu.usbmodem101')    # establishes the serial connection with the Arduino Board


def led(integer):
    board.digital[integer].write(1)

def transistors():
    if digits[0] == 1:
        led(4)
    if digits[1] == 1:
        led(5)
    if digits[2] == 1:
        led(6)
    if digits[3] == 1:
        led(7)

def convert(num):
    if num >= 1:
        convert(num // 2)
    print(num % 2, end='')
    digits.append(num % 2)


if __name__ == '__main__':
    for i in range(length):
        convert(decimal[i])
    transistors()

'''for j in range(binary_length):
    ones_n_zeros = digits[j]
    print(ones_n_zeros)
    if ones_n_zeros == 1:
        places.append(j)
        print(places)'''





'''
 for i in range(0, 15):
    board.digital[13].write(1)
    board.digital[12].write(0)
    board.digital[11].write(1)
    board.digital[10].write(0)

    time.sleep(1)
    board.digital[13].write(0)
    board.digital[12].write(1)
    board.digital[11].write(0)
    board.digital[10].write(1)
    time.sleep(1)
'''