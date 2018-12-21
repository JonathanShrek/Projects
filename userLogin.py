def newUser():
    print('Enter a new username: ')
    newUserName = input("")
    print('Enter a new user password: ')
    newUserPass = input("")
    print('Confirm password: ')
    confirmUserPass = input("")

    if newUserPass != confirmUserPass:
        for i in range(3, 0, -1):
            if newUserPass != confirmUserPass:
                print(i, 'chances remain.')
                print('Error: Confirm password:')
                confirmUserPass = input("")
            else:
                f = open('accounts.txt', 'a+')
                f.writelines([newUserName,'\n'])
                f.close()
                print('Success')
                print('Enter username: ')
                break

if __name__ == "__main__":

    print("Enter username: ")
    print("Enter new to create a new user")
    while True:
        userinput = input("")

        if userinput == "quit" or userinput == "Quit":
            print('Goodbye')
            break

        #elif userinput == lines():
            #FIXME

        elif userinput == 'new' or userinput == 'New':
            newUser() 

        else:
            print('Error: Unknown username. Please try again.')
