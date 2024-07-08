//
// Created by Matthew Staudacher on 6/27/24.
//

#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>  // for rand and srand
#include <ctime>    // for time

using namespace std;

// Define classes Covenant and UNSC similar to Python

class Covenant {
public:
    string species;
    int health;
    int damage;

    Covenant(string sp, int hp, int dmg) : species(sp), health(hp), damage(dmg) {}
};

class UNSC {
public:
    string rank;
    string name;
    int health;
    int damage;

    UNSC(string rk, string nm, int hp, int dmg) : rank(rk), name(nm), health(hp), damage(dmg) {}
};

// Declare instances of Covenant and UNSC

Covenant Brute("Jiralhanae", 300, 200);
Covenant Grunt("Unggoy", 50, 25);
Covenant Elite("Sangheili", 250, 100);

UNSC MasterChief("Master Chief Petty Officer", "John 117", 1000, 150);

// Function to simulate player's attack
int player_attack(int damage, int health) {
    return health - damage;
}

// Function to randomly select opponent and simulate encounter
Covenant random_opponent() {
    int choice = rand() % 3;
    switch (choice) {
        case 0:
            cout << "You have encountered a Sangheili Warrior!" << endl;
            cout << "Enemy Health: " << Elite.health << endl;
            cout << (rand() % 2 ? "I will wipe out your pathetic race, demon!" : "Wort Wort Wort") << endl;
            return Elite;
        case 1:
            cout << "You have encountered a savage Brute!" << endl;
            cout << "Enemy Health: " << Brute.health << endl;
            cout << (rand() % 3 ? "Spartan weak, soft inside!" :
                     (rand() % 2 ? "I will crush your bones and feast on the pulp!" :
                      "I will silence you heretic!")) << endl;
            return Brute;
        case 2:
            cout << "Hey look, a grunt!" << endl;
            cout << "Enemy Health: " << Grunt.health << endl;
            cout << (rand() % 3 ? "\"Do we really have to fight the demon?\"" :
                     (rand() % 2 ? "He was just about to retire!" :
                      "Oh no, I didn't mean to turn these on")) << endl;
            return Grunt;
    }
    // Default return (though not expected to reach here)
    return Grunt;
}

// Function to simulate attack logs
void attack_log(int res) {
    if (res <= 0) {
        cout << "Attack - 150 Damage Dealt - 20 XP" << endl;
        cout << "Enemy Eliminated 100 XP" << endl;
    } else {
        while (res > 0) {
            cout << endl << "Arghshwaaahh" << endl;
            cout << "Attack - 150 Damage Dealt - 20 XP" << endl;
            res -= MasterChief.damage;
            cout << endl << "Agghhhhh" << endl;
            cout << "Attack - 150 Damaged Dealt - 20 XP" << endl;
            if (res <= 0) {
                cout << "*Fainting Noises*" << endl;
                cout << "Enemy Eliminated 100 XP" << endl;
            }
        }
    }
}

// Function to simulate the play process
void play() {
    Covenant enemy = random_opponent();
    // Delay for 2 seconds
    // Equivalent to Python's time.sleep(2)
    // Note: C++ doesn't have a built-in sleep method; this would typically be implemented differently.
    int player_health = MasterChief.health;
    int enemy_health = enemy.health;
    int res = player_attack(MasterChief.damage, enemy_health);
    // Simulate attack logs
    attack_log(res);
}

// Main function to run the game loop
int main() {
    // Seed the random number generator
    srand(time(nullptr));

    // Loop to play the game 4 times
    for (int i = 0; i < 4; ++i) {
        play();
        // Delay for 1 second
        // Equivalent to Python's time.sleep(1)
        // Note: C++ doesn't have a built-in sleep method; this would typically be implemented differently.
    }

    return 0;
}

