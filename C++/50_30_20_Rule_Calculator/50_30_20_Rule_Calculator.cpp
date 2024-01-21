// 50_30_20_Rule_Calculator.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
double income = 0.00;


int main()
{
    cout << "What's your monthly take home pay? :" << endl;
    cin >> income;
    int needs = income / 2;
    int wants = income * 0.3;
    int savings = income / 5;

    cout << "You can afford to spend" << " $" << needs << " on needs," << "$" << wants << " on wants," << "and $" << savings << " on savings" << endl;



    
}


