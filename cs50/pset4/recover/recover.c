#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>


#define BLOCKSIZE 512 //to avoid magic numbers

int main(int argc, char *argv[]){
    if(argc!=2){
        fprintf(stderr, "Usage: ./recover file");
        return 1;
    }
    
    // Create pointer to command line argument file
    char* infile = argv[1];
    
    // Create pointer to the open card.raw file, and check to make sure it is a valid file
    FILE* inptr = fopen(infile, "r");
    if(inptr==NULL){
        printf("Could not open %s", infile);
        return 1;
    }
    
    //Establish the setup of each new jpg to be created
    FILE* newfile;
    newfile = NULL;
    int ctr = 0;
    
    //Run a loop so that we can declare an if statement checking the end of the file later using the "newfile" variable (not global)
    while(1){
    
    //initialize buffer as an array of integers of 1 byte each   
    uint8_t buffer[BLOCKSIZE]={};
    
    //fread() each byte of a 512 byte block
    for(int i = 0; i<BLOCKSIZE; i++){
        //We have defined "newfile", so can close both newfile and card.raw if we reach the end of card.raw
        if(feof(inptr)){
            fclose(inptr);
            if(newfile!=NULL){
                fclose(newfile);
            }
            return 0;
        }
        
        fread(&buffer[i], sizeof(uint8_t), 1, inptr);
    }
    //Are the first four bytes equal to a jpeg file?
    if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && (buffer[3] == 0xe0 || buffer[3] == 0xe1)){
        
        // Have we already identified a jpeg that is open?
        if(newfile!=NULL){
        //Yes, so close the currently open jpeg to make room for a new one
        fclose(newfile);
        }
           
        //Create a character array for the new file name
        char filename[8];
        
        //Create a new jpeg file numbered according to how many files have been created already
        sprintf(filename, "%03i.jpg", ctr);
        
        //Open newly created file, check it
        newfile = fopen(filename, "w");
        if(newfile==NULL){
            fprintf(stderr, "Sorry, the file you are asking for has not been created correctly.");
            return 1;
        }
        
        // Add one to file counter
        ctr++;
        
        // write the current buffer value to the newfile
        fwrite(&buffer[0], BLOCKSIZE * sizeof (uint8_t), 1, newfile);
         
    } else if(newfile!=NULL){
        // write current buffer value to the currently open file
        fwrite(&buffer[0], BLOCKSIZE * sizeof (uint8_t), 1, newfile);
        }
    
    }
        
    // close card.raw
    fclose(inptr);
 
    // Exit the program
    return 0;
}