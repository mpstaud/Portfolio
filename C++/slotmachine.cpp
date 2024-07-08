//
// Created by Matthew Staudacher on 7/1/24.
//
# include <iostream>
#include <vector>
#include <string>


int main(){
    std::vector<std::string> myVector;
    myVector.push_back("Hello");
    myVector.push_back("World");
    myVector.push_back("This");
    myVector.push_back("is");
    myVector.push_back("a");
    myVector.push_back("vector");

    // Print the contents of the vector
    for (const auto& str : myVector) {
        std::cout << str << std::endl;
    }

    return 0;
}