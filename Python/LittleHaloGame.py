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


Brute = Covenant('Jiralhanae', 300, 50)

Grunt = Covenant('Unggoy', 50, 10)

Elite = Covenant('Sangheili', 250, 75)

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
        print(random.choice(['I will wipe out your pathetic race, demon!', 'Wort Wort Wort',
                             'You will be left behind when we begin the great journey']))
    if opponent == Brute:
        print('You have encountered a savage Brute!')
        print('Enemy Health: ' + str(Brute.health))
        print()
        print(random.choice(['Spartan weak, soft inside!', 'I will crush your bones and feast on the pulp!',
                             'I will silence you heretic!']))
    if opponent == Grunt:
        print('Hey look, a grunt!')
        print()
        print('"' + "Do we really have to fight the demon? I don't wanna die!" + '"')
        print()
        #print(random.choice())
    return opponent


def main():
    enemy = random_opponent()
    time.sleep(3)
    player_health = MasterChief.health
    enemy_health = enemy.health
    res = player_attack(MasterChief.damage, enemy_health)
    if res <= 0:
        print('Attack - 150 Damage Dealt - 20 XP')
        print('Enemy Eliminated 100 XP')
    elif res > 0:
        while res > 0:
            print()
            print('Attack - 150 Damage Dealt - 20 XP')
            print()
            time.sleep(1)
            res = res - MasterChief.damage
            print('Attack - 150 Damaged Dealt - 20 XP')
            print()
            if res <= 0:
                print("Enemy Eliminated 100 XP")


if __name__ == '__main__':
    # Run main method
    main()

else:
    print("The end")