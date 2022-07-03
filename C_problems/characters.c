#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX_LEN 100
int main()
{
    char ch;
    scanf("%c", &ch); // first taking a character, ch as input
    scanf("\n");

    char s[MAX_LEN];
    scanf("%[^\n]%*c", &s); // taking a string s as input

    char sen[MAX_LEN];
    scanf("%[^\n]%*c", &sen);

    printf("%c\n", ch); // output ch - char
    printf(s);          // output s - string
    printf("\n");
    printf(sen);
    printf("\n");
    return 0;
}