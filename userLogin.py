def newUser():
    print('Enter a new username: ')
    newUserName = input("")
    print('Enter a new user password: ')
    newUserPass = input("")
    print('Confirm password: ')
    confirmUserPass = input("")

    if newUserPass != confirmUserPass:
        for i in range(3, -1, -1):
            if newUserPass != confirmUserPass:
                print(i, 'chances remain.')
                print('Error: Confirm password:')
                confirmUserPass = input("")
    else:
        with open('accounts.txt', 'a') as out:
            out.write(newUserName + '\n')
            out.close()
        print('Success')
        print('Enter username: ')

#FIXME does not read line to check if username exists
def findUser(n):
    f = open('accounts.txt', 'r')
    name = n
    while True:
        text = f.readlines()
        f.close()
        for line in text:
            if name in text:
                print('Success')
                break
            
        else:
            print('Error: Unknown name. Try again:')
            break

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
