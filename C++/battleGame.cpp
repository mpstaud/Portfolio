//
// Created by Matthew Staudacher on 5/8/24.
//
# include <iostream>
using namespace std;

int playerHealth{100};

int enemyHealth{100};

int attack(int health)
{
    health = health - 20;
    return health;
}
int heal(int health)
{
    health = health + 40;
    return health;
}
int specialAttack(int health)
{
    health = health - 35;
    return health;
}

void chooseAction(basic_string<char> x, basic_string<char> player)
{
    if (player == "Player" && x == "A")
        enemyHealth = attack(enemyHealth);
    if (player == "CPU" && x == "A")    
}



int main()
{
    basic_string<char> input;
    cout << "Attack, Special Attack, or Heal? --> " << endl;
    cin >> input >> endl;
    chooseAction(input, "Player");
    
    return 0;
}
