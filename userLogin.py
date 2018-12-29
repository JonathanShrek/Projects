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
    with open('accounts.txt', 'r') as f:
        for i, line in enumerate(f):
            namePassList = line.split(' ')
            if n == namePassList[0]: 
                valid = True
                break
            else:
                valid = False

    if valid == True:
        print("Success")
    else:
        print('')
        print("Error: Unknown username.")
        print("Enter username: ")


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
            findUser(userinput)

if __name__ == "__main__":
    main()
