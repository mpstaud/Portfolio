//
// Created by Matthew Staudacher on 5/8/24.
//
# include <iostream>


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


int main()
{

    while (playerHealth > 0 && enemyHealth > 0){
        std::basic_string<char> input;
        std::cout << "Attack, Special Attack, or Heal?" << std::endl;
        std::cin >> input;
        if (input == "A")
            enemyHealth = attack(enemyHealth);
        else if (input == "H")
            playerHealth = heal(playerHealth);
        else if (input == "S")
            enemyHealth = specialAttack(enemyHealth);
        else
            std::cout << "Character not allowed" << std::endl;

        
    }
    if (playerHealth <= 0)
        std::cout << "You Lose" << std::endl;
    if (enemyHealth <= 0)
        std::cout << "You " << "are " << "victorious!";


    return 0;
}
