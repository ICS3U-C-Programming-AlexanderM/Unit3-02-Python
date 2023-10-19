#!/usr/bin/env python3
# Created By: Alex M
# Date: Oct 10, 2023
# This program makes the user guess a number .
import constants 


def main():
#get number from user 
    user_guess = int(input(print(" guess a number between 1 - 9 ")) )
    print("")
    if user_guess == constants.computer_guess:
        print (" you got it right ")
    if user_guess != constants.computer_guess:
        print ("You got it wrong")
if __name__ == "__main__": 
    main()