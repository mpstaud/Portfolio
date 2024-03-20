import random


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') \
            or (player == 'p' and opponent == 'r')  \
            or (player == 's' and opponent == 'p'):
        return True


def play():
    user = input('Press r for rock, p for paper, and s for scissors--> ')
    cpu = random.choice(['r', 'p', 's'])
    if user == cpu:
        return print('You tied')
    if is_win(user, cpu):
        return print('You won!')
    else:
        return print('You lose!')


def main():
    play()


if __name__ == '__main__':
    # Run main method
    main()

else:
    print("The end")



