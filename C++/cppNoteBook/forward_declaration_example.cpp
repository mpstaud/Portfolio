//
// Created by Work Environment on 10/8/2024.
//
#include <iostream>
/*
Generally, you should declare and define your functions before they are used. But when you have a ton
 of functions and aren't sure which ones call each other, you can declare it at the beginning so at
 least the compiler knows what the function is as in goes through the code sequentially
*/
int add(int x, int y);
//note: technically only the parameter types are required in the declaration, but it's best practice to put/keep the names in there
//int add(int, int); is valid syntax
//you can also just copy the function header and add a semicolon

int main()
{
    std::cout << "The sum of 3 and 4 is: " << add(3, 4) << '\n';
    return 0;
}

int add(int x, int y)
{
    return x + y;
}