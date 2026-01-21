/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main() {
// Variables
    char hex[4];
    int i;
// User inputs hex number
    printf("Please enter a hex number:\n");
    scanf("%s", hex);
// If else statements to print the hexadecimal number into binary number
    for (i = 0; i < 4; i++) {
        if (hex[i] == '1') {
            printf("0001");
        } else if (hex[i] == '2') {
            printf("0010"); 
        } else if (hex[i] == '3') {
            printf("0011");
        } else if (hex[i] == '4') {
            printf("0100");
        } else if (hex[i] == '5') {
            printf("0101");
        } else if (hex[i] == '6') {
            printf("0110");
        } else if (hex[i] == '7') {
            printf("0111"); 
        } else if (hex[i] == '8') {
            printf("1000");
        } else if (hex[i] == '9') {
            printf("1001");
        } else if (hex[i] == 'A') {
            printf("1010");
        } else if (hex[i] == 'B') {
            printf("1011");
        } else if (hex[i] == 'C') {
            printf("1100"); 
        } else if (hex[i] == 'D') {
            printf("1101");
        } else if (hex[i] == 'E') {
            printf("1110");
        } else if (hex[i] == 'F') {
            printf("1111");
        }
    }

    return 0;
}