import json
from passlib.hash import argon2
from tkinter import *

class User:
    def newUser(self, userPassDict):
        username = input("Enter new username: ")
        if username in userPassDict:
            print("Username already taken.")

        else:
            password = input("Enter new password: ")
            confirmPass = input("Confirm password: ") 
            for i in range(3, -1, -1):
                if password == confirmPass:
                    passHash = argon2.using(rounds=4).hash(password)
                    userPassDict[username] = passHash
                    with open('userData.json', 'w') as fp:
                        json.dump(userPassDict, fp, sort_keys=True, indent=4)
                    print("Success")
                    break
            
                else:
                    if i == 0:
                        print("Error: Max attempts reached.")

                    else:
                        print("Error:", i, "attempts remain.")
                        confirmPass = input("Try again: ")

def main():
    userClass = User()

    try:
        with open('userData.json', 'r') as fp:
            userPassDict = json.load(fp)
    except:
        userPassDict = {}

    while True:
        username = input("Enter username: ") 

        if username == 'new' or username == 'New':
            userClass.newUser(userPassDict)

        elif username in userPassDict:
            password = input("Enter password: ")
            existingHash = userPassDict[username]
            if argon2.verify(password, existingHash):
                print("Welcome.")
                break
            
            else:
                print("Error: Try again.")

        else:
            print("Error: Try again.")

if __name__ == "__main__":
    main()
