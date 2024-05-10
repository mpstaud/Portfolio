//
// Created by Matthew Staudacher on 5/8/24.
//
# include <iostream>
using namespace std;

int attack(int damage, int health){
    health = health - damage;
    return health;
}
int heal(int healing, int health){
    health = health + healing;
    return health;
}
basic_string<char> chooseAction(){
    string x;
    cout << "A to attack, H to heal: " << endl;
    cin >> x;
    return x;
}
basic_string<char> cpuAction(){
    string y;
    y = "A";
    return y;
}


int main(){
    int playerHealth = {100};
    int enemyHealth = {100};
    basic_string<char> dec = chooseAction();
    basic_string<char> cpu = cpuAction();
    cout << playerHealth << endl;
    cout << enemyHealth << endl;
    cout << dec << endl;
    cout << cpu << endl;
}