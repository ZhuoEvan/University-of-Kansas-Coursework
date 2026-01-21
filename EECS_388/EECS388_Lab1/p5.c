/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main() {
// Variables
    int size;
    int i, j ,element;
    int count = 0;
    int total = 0;
// User inputs array size and elements
    printf("How big is the array?\n");
    scanf("%d", &size);
    int collect[size];
    int duplicate[size];
    for (i = 0; i < size; i++) {
        printf("Enter element %d:\n", i + 1); 
        scanf("%d", &element);
        collect[i] = element;
    }
// For loops to find duplicates
    printf("\n");
    for (i = 0; i < size; i++) {
        count++;
        for (j = count; j < size; j++) {
            if (collect[i] == collect[j]) {
                duplicate[collect[i]] = 'A';
            }
        }
    }
// For loop to register a duplicate number once
    for (i = 0; i < 10; i++) {
          if (duplicate[i] == 'A') {
              total++;
          }
    }
    printf("%d\n", total);
    return 0;
}