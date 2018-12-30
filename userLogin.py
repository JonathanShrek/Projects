def fileRead():
    with open('accounts.txt') as f:
        lines = f.read().splitlines()
        return lines

def fileWrite(name, password):
    with open('accounts.txt', 'a') as out:
        out.write(name + ' ' + password + '\n')
        out.close()

def newUser():
    newUserName = input("Enter a new username: ")
    newUserPass = input("Enter a new user password: ")
    confirmUserPass = input("Confirm password: ")

    for i in range(3, -1, -1):
        if newUserPass == confirmUserPass:
            fileWrite(newUserName, newUserPass)
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

def findUser(n):
    namePassList = fileRead()
    nameList = [i.split(' ')[0] for i in namePassList]
    if n in nameList:
        return True
    else:
        return False

def passwordFunc(p):
    namePassList = fileRead()
    passList = [i.split(' ')[1] for i in namePassList]
    if p in passList:
        return True
    else:
        return False

def main():
    print("Enter new to create a new user")
    print("Enter username: ")
    while True:
        userinput = input("")

        if userinput == "quit" or userinput == "Quit":
            print('Goodbye')
            break

        elif userinput == 'new' or userinput == 'New':
            newUser() 

        else:
            if findUser(userinput) == True:
                password = input("Enter password: ")

                for i in range(3, -1, -1):
                    if passwordFunc(password) == True:
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
                            password = input("Enter password: ")

            else:
                print("Error: Unknown username.")
                print("Please try again.")

if __name__ == "__main__":
    main()
