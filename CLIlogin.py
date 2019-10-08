#!/usr/bin/env python

import json
#import mysql.connector as mariadb
from passlib.hash import argon2

'''
This program allows users to create and login with usernames and passwords.

@author: Jonathan Shreckengost (jonathanshrek@gmail.com)
'''

# Try to open and read .json file
try:
    with open('userData.json', 'r') as fp:
        userPassDict = json.load(fp)

# If no .json create new dictionary
except:
    userPassDict = {}


# Handles all things related to the user
class user:
    
    # Method that creates a new user
    def newUser(self, userPassDict):
        username = input("Enter new username: ")
        
        # Checks if username is already taken
        if username in userPassDict:
            print("Username already taken.")

        # Create new user
        else:
            password = input("Enter new password: ")
            confirmPass = input("Confirm password: ")
            
            # Gives user 3 chances to confirm password
            for i in range(3, -1, -1):
                
                # Hashes and inserts new password into dictionary
                if password == confirmPass:
                    passHash = argon2.using(rounds=7).hash(password)
                    userPassDict[username] = passHash
                    
                    # Writes new data to the .json file
                    with open('userData.json', 'w') as fp:
                        json.dump(userPassDict, fp, sort_keys=True, indent=2)
                    print("Success")
                    break
            
                else:
                    if i == 0:
                        print("Error: Max attempts reached.")

                    else:
                        print("Error:", i, "attempts remain.")
                        confirmPass = input("Try again: ")

def main():
    userClass = user()
    print("Enter new to create a new user or quit to exit")
    
    # Loops until user quits the program
    while True:
        userInput = input("Enter username: ")

        # Allows user to properly quit the program
        if userInput == "quit" or userInput == "Quit":
            print('Goodbye')
            break

        # Allows the user to create a new user
        elif userInput == 'new' or userInput == 'New':
            userClass.newUser(userPassDict) 

        # Allows the user to login to an existing account
        else:
            
            # Confirms username is in the dictionary
            if userInput in userPassDict:
                passInput = input("Enter password: ")
                
                # Pulls the users hashed password from the dictionary
                existingHash = userPassDict[userInput]
                
                # Gives the user 3 chances to get the correct password before breaking back to the startup prompt
                for i in range(3, -1, -1):
                    if argon2.verify(passInput, existingHash):
                        print("Successfully logged in. Welcome", userInput + "!")
                        break

                    else:
                        if i == 0:
                            print("Error: Max attempts reached. Goodbye.")
                            print('')
                            print("Enter new to create a new user") 
                            break
                        else:
                            print("Incorrect password.", i, "attempts remain.")
                            passInput = input("Enter password: ")

            # Unrecognized username
            else:
                print("Error: Unknown username. Please try again.")

if __name__ == "__main__":
    main()
