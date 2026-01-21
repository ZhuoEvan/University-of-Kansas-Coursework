/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>  

int main() {
// Variables
    int num;
    int i;
    int j;
    int prime;
// Prime number from the user
    printf("Enter a number:\n");
    scanf("%d", &num);
// Checking all numbers from 2 to the number by the user
    for (i = 2; i <= num; i++) {
        prime = 1;
// Equation to check for prime numbers
        for (j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                prime = 0;
                break;
            }
        }
// Printing the prime numbers
        if (prime) {
            printf("%d ", i);
        }
    }
    return 0;
}