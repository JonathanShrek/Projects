#FIXME error with namePassList. Bug reading usernames.
def fileRead():
    with open('accounts.txt', 'r') as f:
        for i, line in enumerate(f):
            namePassList = line.split(' ')
            print(namePassList)
        return namePassList

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
    name = namePassList[0]
    if n == name: 
        return True
    else:
        return False

#FIXME bugged. Not detecting correct password
def passwordFunc(p):
    namePassList = fileRead()
    password = namePassList[1]
    if p == password:
        return True
    else:
        return False

def main():
    print("Enter username: ")
    print("Enter new to create a new user")
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
                if passwordFunc(password) == True:
                    print("Successfully logged in. Welcome", userinput)

                else:
                    print("Wrong password. Please try again.")

            else:
                print("Error: Unknown username.")
                print("Please try again.")

if __name__ == "__main__":
    main()
