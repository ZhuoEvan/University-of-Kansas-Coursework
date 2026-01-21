// main.cpp
/*
 *
 *
 *
 * 
 */

//Import External Files
#include "quash_func.h"
#include "quash_listener.h"

//Import Libraries
#include <iostream>
#include <string>

//Quash Message Function
void sQuash_msg(bool t) {
    //Start-up Message
    if (t) {
        std::cout << "  |=====================================================================|\n"
                     "  | Welcome to sQuash!\t\t\t\t\t\t\t|\n"
                     "  | A \"Quite a Shell\" program that can run executables.\t\t\t|\n"
                     "  | To read the built in functions, type \"help\" in the command line.\t|\n"
                     "  |=====================================================================|\n"
                     << std::endl;
    } else { //Termination Message
        std::cout << "  |=====================================================================|\n"
                     "  | Terminating sQuash...\t\t\t\t\t\t|\n"
                     "  |=====================================================================|\n"
                     << std::endl;
    }
    return;
}

//Main Function
int main(int argc, char* argv[]) {
    //Start-up Message
    sQuash_msg(true);

    //Start Listener
    listener(true);

    //Termination Message
    sQuash_msg(false);

    return 0;
}