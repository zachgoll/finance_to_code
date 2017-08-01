#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[]){
    //make sure there are only 2 arguments total
    if(argc == 2){
    //place the argv string in it's own variable
    string key = argv[1];
    //make sure that every character in 'key' is alphabetic, and convert all letters to uppercase
    for(int i = 0; i<strlen(key); i++){
        if(isalpha(key[i])){
            key[i] = toupper(key[i]);
        } else{
            printf("Error: please enter only alphabetic characters as the key\n");
            return 1;
        }
    }
    printf("plaintext: ");
    string plaintext = get_string();
    printf("ciphertext: ");
    for(int j = 0; j<strlen(plaintext); j++){
        int currentkey = key[j%strlen(key)]-65;
        if(isupper(plaintext[j])){
            char characterupper = (((plaintext[j]-65)+currentkey)%26)+65;
            printf("%c", characterupper);
        } else if (islower(plaintext[j])){
            char characterlower = (((plaintext[j]-97)+currentkey)%26)+97;
            printf("%c", characterlower);
        } else {
            printf("%c", plaintext[j]);
        }
    }
    printf("\n");
    } else {
        printf("Error: please enter only one key\n");
        return 1;
        } 
        
    
    }
   
     
    

