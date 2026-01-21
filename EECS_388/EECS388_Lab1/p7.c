/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main() {
// Variables
    int temp;
    int *temp_ptr;
// User inputs integer
    printf("Enter integer:\n");
    scanf("%d", &temp);
// Assigning pointer to temp address
    temp_ptr = &temp;
// Printing all outputs
    printf("\n");
    printf("%d\n", temp);
    printf("%d\n", *temp_ptr);
    printf("%p\n", &temp);
    printf("%p\n", temp_ptr);
    return 0;
}