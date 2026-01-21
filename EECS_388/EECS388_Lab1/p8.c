/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h> 

int main() {
// Variables
    int integer; 
    int bit; 
    int bitset;
// Integer value and bit value from user
    printf("Enter integer:\n"); 
    scanf("%d", &integer); 
    printf("Enter bit:\n"); 
    scanf("%d", &bit); 
// Bitwise right shift
    bitset = (integer >> bit) & 1; 
// Bit check for set
    if (bitset != 0) { 
        printf("TRUE"); 
    } else { 
        printf("FALSE"); 
    } 
    return 0; 
} 
