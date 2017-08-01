/**
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include "dictionary.h"

#define LENGTH 45
#define HASHTABLE_SIZE 65536

//Initialize variables and struct

typedef struct node{
    char word[LENGTH+1];
    struct node* next;
}
node;

node* hashtable[HASHTABLE_SIZE];

int dictionarySize = 0;

//! this one is called djb2
//! originally from http://www.cse.yorku.ca/~oz/hash.html
int hash_it(char* needs_hashing)
{
    unsigned int hash = 0;
    for (int i=0, n=strlen(needs_hashing); i<n; i++)
        hash = (hash << 2) ^ needs_hashing[i];
    return hash % HASHTABLE_SIZE;
}

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    //Use a temporary variable to hold a lowercase version of the word being checked
    char temporary[LENGTH + 1];
    int lengthWord = strlen(word);
    for(int j = 0; j<lengthWord; j++){
        temporary[j] = tolower(word[j]);
    }
    //Add the terminating character to the final index of the word
    temporary[lengthWord] = '\0';
    
    //Find the address which the word belongs to
    node* cursor = hashtable[hash_it((void*)temporary)];
    
    // While the current position is still pointing to another node, check the constant word vs. the word stored
    while(cursor!=NULL){
        int spelledCorrect = strcmp((void*)cursor->word, temporary);
        if(spelledCorrect==0){
            return true;
        } else{
            cursor=cursor->next;
        }
        
    }
    return false;
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary)
{
    FILE* dp = fopen(dictionary, "r");
    char word[LENGTH+1];

    if(dp!=NULL){
    
    while(fscanf(dp, "%s\n", word) !=EOF){
    
    //Add a count to the dictionary size
    
    dictionarySize++;
    
    //Read through text file and put the current word in a node 
    
    node* new_node= malloc(sizeof(node));
      
    //Check to make sure memory is available 
    
    if(new_node==NULL){
        return 0;
    }
        
    //Copy the current word into the new node
    
    strcpy(new_node->word, word);
        
    //Put the node's word through a hash function
    
    int index = hash_it(new_node->word);
        
    //Create a pointer to the new node based on the hash value
    
    if(hashtable[index]==NULL){
        hashtable[index] = new_node;
        new_node->next = NULL;
    } 
    
    //If collision, put the hash value as part of the linked list at that address
    else {
        new_node->next = hashtable[index];
        hashtable[index] = new_node;
      }
    }
    
    //Close the file 
    
    fclose(dp);
    
    //Return true to signify success
    
    return true;
}
    //If didn't work, return false
    
    return false;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    // if dictionary is loaded, return number of words
    if (dictionarySize > 0)
    {
        return dictionarySize;
    }
        
    return 0;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    for(int i = 0; i<HASHTABLE_SIZE; i++){
        node* cursor = hashtable[i];
        while(cursor!=NULL){
            node* temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    return true;
    }
    return false;
}
