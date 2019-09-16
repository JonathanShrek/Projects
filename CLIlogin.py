#!/usr/bin/env python

import json
#import mysql.connector as mariadb
from passlib.hash import argon2

try:
    with open('userData.json', 'r') as fp:
        userPassDict = json.load(fp)

except:
    userPassDict = {}

class user:
    def newUser(self, userPassDict):
        username = input("Enter new username: ")
        if username in userPassDict:
            print("Username already taken.")

        else:
            password = input("Enter new password: ")
            confirmPass = input("Confirm password: ") 
            for i in range(3, -1, -1):
                if password == confirmPass:
                    passHash = argon2.using(rounds=7).hash(password)
                    userPassDict[username] = passHash
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
    print("Enter new to create a new user")
    while True:
        userInput = input("Enter username: ")

        if userInput == "quit" or userInput == "Quit":
            print('Goodbye')
            break

        elif userInput == 'new' or userInput == 'New':
            userClass.newUser(userPassDict) 

        else:
            if userInput in userPassDict:
                passInput = input("Enter password: ")
                existingHash = userPassDict[userInput]
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

            else:
                print("Error: Unknown username. Please try again.")

if __name__ == "__main__":
    main()
