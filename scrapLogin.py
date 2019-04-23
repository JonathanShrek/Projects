#!/usr/bin/env python

class fileManipulation:
    def fileRead(self):
        with open('accounts.txt') as f:
            lines = f.read().splitlines()
            return lines

    def fileWrite(self, name, password):
        with open('accounts.txt', 'a') as out:
            out.write(name + ' ' + password + '\n')
            out.close()

class password:
    def hash_password(self, password):
        from hashlib import blake2b
        h = blake2b(digest_size=64)
        passwordByte = str.encode(password)
        h.update(passwordByte)
        return h.hexdigest()

    def passwordFunc(self, p):
        read = fileManipulation()
        passClass = password()
        namePassList = read.fileRead()
        passList = [i.split(' ')[1] for i in namePassList]
        passHash = passClass.hash_password(p)
        if passHash in passList:
            return True
        else:
            return False

class user:
    def newUser(self):
        passClass = password()
        fileClass = fileManipulation()
        newUserName = input("Enter a new username: ")
        newUserPass = input("Enter a new user password: ")
        confirmUserPass = input("Confirm password: ")

        for i in range(3, -1, -1):
            if newUserPass == confirmUserPass:
                passHash = passClass.hash_password(newUserPass)
                fileClass.fileWrite(newUserName, passHash)
                print("Success.")
                print("Enter username: ")
                break

            else:
                if i == 0:
                    print("Error: Max attempts reached.")
                    print('')
                    print("Enter username:")
                    print("Enter new to create a new user")
                    break

                else:
                    print('')
                    print("Password confirmation unsuccessful.")
                    print(i, "attempts remaining.")
                    confirmUserPass = input("Confirm password: ")

    def findUser(self, n):
        fileClass = fileManipulation()
        namePassList = fileClass.fileRead()
        nameList = [i.split(' ')[0] for i in namePassList]
        if n in nameList:
            return True
        else:
            return False

def main():
    userClass = user()
    passClass = password()
    print("Enter new to create a new user")
    print("Enter username: ")
    while True:
        userinput = input("")

        if userinput == "quit" or userinput == "Quit":
            print('Goodbye')
            break

        elif userinput == 'new' or userinput == 'New':
            userClass.newUser() 

        else:
            if userClass.findUser(userinput) == True:
                passInput = input("Enter password: ")

                for i in range(3, -1, -1):
                    if passClass.passwordFunc(passInput) == True:
                        print("Successfully logged in. Welcome", userinput + "!")
                        break

                    else:
                        if i == 0:
                            print("Error: Max attempts reached. Goodbye.")
                            print('')
                            print("Enter new to create a new user") 
                            print("Enter username: ")
                            break
                        else:
                            print("Incorrect password.", i, "attempts remain.")
                            passInput = input("Enter password: ")

            else:
                print("Error: Unknown username.")
                print("Please try again.")

if __name__ == "__main__":
    main()
