import random
import time


class Covenant:
    def __init__(self, species, health, damage):
        self.species = species
        self.health = health
        self.damage = damage


class UNSC:
    def __init__(self, rank, name, health, damage):
        self.rank = rank
        self.name = name
        self.health = health
        self.damage = damage


Brute = Covenant('Jiralhanae', 300, 200)

Grunt = Covenant('Unggoy', 50, 25)

Elite = Covenant('Sangheili', 250, 100)

Jackal = Covenant('Kigyar', 100, 50)

MasterChief = UNSC('Master Chief Petty Officer', 'John 117', 1000, 150)


def player_attack(damage, health):
    result = health - damage
    return result


def random_opponent():
    opponent = random.choice([Elite, Brute, Grunt])
    if opponent == Elite:
        print('You have encountered a Sangheili Warrior!')
        print('Enemy Health ' + str(Elite.health))
        print()
        print(random.choice(['I will wipe out your pathetic race, demon!', 'Wort Wort Wort']))
    if opponent == Brute:
        print('You have encountered a savage Brute!')
        print('Enemy Health: ' + str(Brute.health))
        print()
        print(random.choice(['Spartan weak, soft inside!', 'I will crush your bones and feast on the pulp!',
                             'I will silence you heretic!']))
    if opponent == Grunt:
        print('Hey look, a grunt!')
        print('Enemy Health: ' + str(Grunt.health))
        print()
        print(random.choice(['"' + "Do we really have to fight the demon?" + '"',
                            'He was just about to retire!', "Oh no, I didn't mean to turn these on"]))
        print()

    return opponent


def attack_log(res):
    if res <= 0:
        print('Attack - 150 Damage Dealt - 20 XP')
        print('Enemy Eliminated 100 XP')
    elif res > 0:
        while res > 0:
            print()
            print('Arghshwaaahh')
            print('Attack - 150 Damage Dealt - 20 XP')
            print()
            time.sleep(1)
            res = res - MasterChief.damage
            print('Agghhhhh')
            print('Attack - 150 Damaged Dealt - 20 XP')
            print()
            if res <= 0:
                print('*Fainting Noises*')
                print("Enemy Eliminated 100 XP")


def play():
    enemy = random_opponent()
    time.sleep(2)
    player_health = MasterChief.health
    enemy_health = enemy.health
    res = player_attack(MasterChief.damage, enemy_health)
    enemy_attack = player_attack(enemy.damage, player_health)
    attack_log(res)


def main():

    for i in range(0, 4):
        play()
        time.sleep(1)


if __name__ == '__main__':
    # Run main method
    main()

else:
    print("The end")