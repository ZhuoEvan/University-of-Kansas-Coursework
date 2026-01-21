/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h> 

int main() 
// Variables for the calculator 
{ 
int one = 0; 
char operation = '+'; 
int two = 0; 
int result = 0; 
// Receiving the 1st operand and operation from the user 
printf("Enter 1st operand:\n"); 
scanf("%d", &one); 
printf("Enter operation:\n"); 
scanf(" %c", &operation); 
// Seperating square function from other functions 
    if (operation == 's') { 
        result = one * one; 
        printf("%d", result); 
    } else { 
        printf("Enter 2nd operand:\n"); 
        scanf("%d", &two); 
// Taking 2nd operand from user 
// Using a switch to do the correct operation 
        switch(operation) 
        { 
            case'+': 
            result = one + two; 
            printf("%d", result); 
            break; 
            case'-': 
            result = one - two; 
            printf("%d", result); 
            break; 
            case'*': 
            result = one * two; 
            printf("%d", result); 
            break; 
            case'/': 
            result = one / two; 
            printf("%d", result); 
            break; 
        } 
} 
    return 0; 
} 