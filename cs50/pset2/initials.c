#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main(void){
    string name = get_string();
    char firstletter = toupper(name[0]);
    printf("%c", firstletter);
    for(int i = 0; i<strlen(name); i++){
        if(isspace(name[i])){
            printf("%c", toupper(name[i+1]));
        }
    }
    printf("\n");
}
