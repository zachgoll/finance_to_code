#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[]){
    if(argc != 2){
        printf("Error: please enter a cipher key!\n");
        return 1;
    }
    
    else {
        int key = atoi(argv[1])%26;
        printf("plaintext:\n");
        string plaintext = get_string();
        printf("ciphertext:\n");
        for(int i = 0; i<strlen(plaintext); i++){
            if(isalpha(plaintext[i])){
                if(isupper(plaintext[i])){
                    char uppercaseletter = ((((plaintext[i]-65)+key)%26)+65);
                    printf("%c", uppercaseletter);
                } else if (islower(plaintext[i])){
                    char lowercaseletter = ((((plaintext[i]-97)+key)%26)+97);
                    printf("%c", lowercaseletter);
                }
            }
            else {
                if(isdigit(plaintext[i])){
                    printf("%c", plaintext[i]);
                } else{
                    printf(" ");
                }
            }
            
        }
    }
    printf("\n");
}
