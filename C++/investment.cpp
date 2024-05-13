//
// Created by Matthew Staudacher on 5/2/24.
//
#include <iostream>
#include <cmath>
using namespace std;
double principal,interest_rate;
int term;

double total_value(double p,double i,int t)
{
    double result;
    result = p * pow(i, t);
    cout <<  result;
    return result;


}

int main()
    {
    cout << "Enter your principal amount: ";
    cin >> principal;
    cout << "Enter your interest rate: ";
    cin >> interest_rate;
    cout << "Enter your term in years: ";
    cin >> term;
    total_value(principal,interest_rate,term);


    }