/*
* Name: Evan Zhuo
* Assignment: EECS 348 Lab 10
* Collaborators: w3schools.com | Google Gemini | EECS330 Lab 5
*/
//main.cpp

//C++ Standard Library Imports
#include <iostream> //Standard Input and Output Stream
#include <fstream> //Standard File Stream
#include <string> //Standard String
#include <cmath> //Standard C Math

using namespace std; //Shorten Code by removing the need for std::

//Print Function | Created by Me
void print(double result) {
    cout << result << endl; //Print the result
    return; //Return
}

//Addition Function | Created by Me
void addition(double addend1) {
    double addend2 = -123.456; //Other value to add with
    double sum = 0; //Double to store sum
    sum = addend1 + addend2; //Addition process
    print(sum); //Print the sum
    return; //Return
}

//Check Sign Function | Created by Me
bool isSign(char c) {
    if(c == '+' || c == '-') return true; //Return true if c is a sign
    else return false; //Return false if c is not a sign
}

//Check Digit Function | Used EECS330 Lab5
bool isDigit(char c) {
    //Statement from EECS330_Lab5
    if (c >= '0' && c <= '9') return true; //Return true if c is a digit
    else return false; //Return false if c is not a digit
}

//Check Decimal Function | Created by Me
bool isDecimal(char c) {
    if (c == '.') return true; //Return true if c is a decimal
    else return false; //Return false if c is not a decimal
}

//Check Alphabet Function | Used Google Gemini
bool isAlphabet(char c) {
    if (c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z') return true; //Return true if c is an alphabet character
    else return false; //Return false if c is not an alphabet character
}

//Character to Integer Conversion Function | Used Google Gemini
int charToInt(char c) {
    return c - '0'; //Return the c value with the ASCII value of 0 subtracted
}

//String to Double Conversion Function | Used Google Gemini
double stringToDouble(string str) {
    //Local Variables
    double strDouble = 0.0;
    bool isNegative = false;
    bool decimalFound = false;
    int decimalPlaces = 0;

    for (size_t j = 0; j < str.length(); ++j) { //Go through all characters in the string
        if (j == 0 && isSign(str[j]) && str[j] == '-') isNegative = true; //Check for negative sign
        else if (isDigit(str[j])) { //Encountered a digit
            if (!decimalFound) { //Not a decimal situation
                strDouble = strDouble * 10 + charToInt(str[j]); //Multiply to shift all values to the left then add
            } else { //Decimal has been encountered
                strDouble = strDouble + charToInt(str[j]) * pow(10, -(decimalPlaces + 1)); //Shift the value to the right before adding
                decimalPlaces++; //Move the decimal place to the right by one
            }
        } else decimalFound = true; //Encountered a decimal point
    }
    if (isNegative) strDouble = -strDouble; //Change double to be negative
    return strDouble; //Return the double
}

//Valid Double Function | Created by Me
bool validDouble(string str) {
    //Initial Variables
    bool isNegative = false;
    bool singleDecimal = false;
    bool decimalDigit = false;
    
    for (size_t i = 0; i < str.length(); ++i) { //Check all characters in a string
        if (i == 0) { //Check the first string for sign or digit
            if (!(isDigit(str[i])) && !(isSign(str[i]))) return false; //Invalid: Not a Sign or Digit
            if (isSign(str[i]) && str[i] == '-') isNegative = true; //Check for Negative Sign
        } else { //Check other characters in the string
            if (isSign(str[i]) || isAlphabet(str[i])) return false; //Invalid: Alphabet or Sign
            if (isDigit(str[i]) || isDecimal(str[i])) { //Index is a digit or decimal
                if (isDigit(str[i]) && singleDecimal) decimalDigit = true; //Value after Decimal
                else if (isDecimal(str[i]) && singleDecimal) return false; //Invalid: Two Decimal Marks
                else if (isDecimal(str[i])) singleDecimal = true; //First decimal detected
            }
        }
    }
    //Final Condition Check
    if (isNegative && !(decimalDigit)) return false; //Invalid: Single Negative Value
    if (singleDecimal && !(decimalDigit)) return false; //Invalid: Incomplete Decimal
    return true; //Valid Double Value
}

//File Access Function | Assistance from w3schools.com
void fileAccess(string fileName) {
    string fileLine; //String Variable to Store a Line from File
    ifstream fileContent(fileName); //Read from File
    
    while(getline (fileContent, fileLine)) { //Get a line from the File until the last line
        if (validDouble(fileLine)) {
            double value = stringToDouble(fileLine);
            addition(value);
        }
    }
    fileContent.close(); //Close the File
    return; //Return
}

//Main Function | Created by Me
int main() {
    cout << "[Starting Lab 10 main.cpp Program]" << endl; //Starting Program Message
    //Local Variable
    string fileName;
    
    cout << "Enter a file name with dot extension: "; cin >> fileName; //Get File from User
    fileAccess(fileName); //Access the content of the file
    
    cout << "[Lab 10 main.cpp Program is Completed]" << endl; //End Program Message
    return 0; //Successful Program Run
}