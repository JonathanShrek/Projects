def newUser():
    print('Enter a new username: ')
    newUserName = input("")
    print('Enter a new user password: ')
    newUserPass = input("")
    print('Confirm password: ')
    confirmUserPass = input("")

    #FIXME range is bugged
    if newUserPass != confirmUserPass:
        for i in range(3, -1, -1):
            if newUserPass != confirmUserPass:
                print(i, 'chances remain.')
                print('Error: Confirm password:')
                confirmUserPass = input("")
    else:
        with open('accounts.txt', 'a') as out:
            out.write(newUserName + ' ' + newUserPass + '\n')
            out.close()
        print('Success')
        print('Enter username: ')


#FIXME does not read line to check if username exists
def findUser(n):
    with open('accounts.txt', 'r') as f:
        text = f.readlines()
        name = n
        if name in text:
            print('Success')
            
        else:
            print('Error: Unknown name. Try again:')
        f.close()

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
