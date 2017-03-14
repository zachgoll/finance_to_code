/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */

#include <cs50.h>

#include "helpers.h"
#include <stdio.h>

/**
 * Returns true if value is in array of n values, else false.
 * Test: ./generate 1000 50 | ./find 127
 * Simple test: ./generate 10 2 | ./find 36285
 */
bool search(int value, int values[], int n)
{
    int start = 0;
    int end = n-1;
    while(end >= start){
        int middle = (start+end) / 2;
        if(values[middle]==value){
            return true;
        } else if (values[middle]>value){
            end =  middle - 1;
        } else {
            start = middle + 1;
        }
        
    }
    return false;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    int swap, position, k, c;
    for(k = 0; k<(n-1); k++){
        position = k;
        for(c = k+1; c<n; c++){
            if(values[c]<values[position]){
                position = c;
            }
            if(position!=k){
                swap = values[c];
                values[c] = values[position];
                values[position] = swap;
            }
        }
    }   
    return;
}
