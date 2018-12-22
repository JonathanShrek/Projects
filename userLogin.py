def newUser():
    newUserName = input("Enter a new username: ")
    newUserPass = input("Enter a new user password: ")
    confirmUserPass = input("Confirm password: ")

    #FIXME range is bugged
    if newUserPass != confirmUserPass:
        for i in range(3, -1, -1):
            if newUserPass != confirmUserPass:
                print(i, 'chances remain.')
                confirmUserPass = input("Error: Confirm password: ")
    else:
        with open('accounts.txt', 'a') as out:
            out.write(newUserName + ' ' + newUserPass + '\n')
            out.close()
        print('Success')
        print('Enter username: ')


#FIXME does not read line to check if username exists
def findUser(n):
    with open('accounts.txt', 'r') as f:
        for i, line in enumerate(f):
            if n in line: 
                valid = True
                break
            else:
                valid = False

    if valid == True:
        print("Success")
        print('')
    else:
        print("Error: Unknown username.")
        print("Enter username: ")


def main():
    print("Enter username: ")
    print("Enter new to create a new user")
    while True:
        userinput = input("")
        print('')

        if userinput == "quit" or userinput == "Quit":
            print('Goodbye')
            break

        elif userinput == 'new' or userinput == 'New':
            newUser() 

        else:
            findUser(userinput)

if __name__ == "__main__":
    main()
