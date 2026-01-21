/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main(){
// Variables  
    char string[100];
    int i;
    int length = 0;
// User inputs the string
    printf("Enter string:\n");
    scanf("%s", string);
// For loop that ends when it reaches a space
    for (i = 0; string[i] != '\0'; i++) {
        if (string[i] == ' ') {
            break;
        } else {
            length++;
        }
    }
    printf("%d", length);
    return 0;
}