#!/usr/bin/env python3

import os
import sys
import helpers

from analyzer import Analyzer
from termcolor import colored

def main():
    
    userTweets = []
    
    # ensure proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: ./tweet @name")
    
    # ensure proper usage
    if helpers.get_user_timeline(sys.argv[1]) == None:
        print("Error loading user: please enter a valid Twitter handle without the '@' symbol")
        sys.exit()
    # get tweets
    else:
        userTweets = helpers.get_user_timeline(sys.argv[1])

    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

# instantiate analyzer
analyzer = Analyzer(positives, negatives)
    # iterate through the first 50 of the user's tweets
    
    # determine how many tweets the user has
    numTweets = len(userTweets)
    if numTweets > 50:
        numTweets = 50

for i in range(numTweets):
    # analyze tweet
    score = analyzer.analyze(userTweets[i])
        if score > 0.0:
            print(colored(score, "green"), end=" ")
            print(colored(userTweets[i], "green"))
    elif score < 0.0:
        print(colored(score, "red"), end=" ")
            print(colored(userTweets[i], "red"))
        else:
            print(colored(score, "yellow"), end=" ")
            print(colored(userTweets[i], "yellow"))

if __name__ == "__main__":
    main()
