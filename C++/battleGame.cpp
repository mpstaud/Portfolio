//
// Created by Matthew Staudacher on 5/8/24.
//
# include <iostream>
using namespace std;
int playerHealth{100};
int enemyHealth{100};

int attack(int health){
    health = health - 20;
    return health;
}
int heal(int health){
    health = health + 40;
    return health;
}
void chooseAction(basic_string<char> x, basic_string<char> player){
    if (player == "Player" && x == "A")
        enemyHealth = attack(enemyHealth);
    if (player == "CPU" && x == "A")
        
        
        
        
        
        
        
    
}



int main(){
    
    basic_string<char> dec = chooseAction();
    basic_string<char> cpu = cpuAction();
    cout << playerHealth << endl;
    cout << enemyHealth << endl;
    cout << dec << endl;
    cout << cpu << endl;
    return 0;
}
