/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>  

int main() { 
// Variable for the weight 
int weight = 0; 
// User inputs vehicle weight 
printf("Enter a vehicle weight:\n"); 
scanf("%d", &weight); 
// if else statements with inequalities for weight classification 
if (weight < 10000) { 
    printf("L"); 
} else if (weight < 26000) { 
    printf("M"); 
} else { 
    printf("H"); 
} 
    return 0;  
} 