import json
from passlib.hash import argon2
from tkinter import *
import tkinter.messagebox as tm

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self, bg="white", fg="black")
        self.entry_password = Entry(self, bg="white", fg="black", show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1, pady=5, padx=5)
        self.entry_password.grid(row=1, column=1, padx=5)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(row=2, pady=5, columnspan=2)

        self.logbtn = Button(self, text="Login", command=self.login_btn_clicked)
        self.logbtn.grid(row=3, column=0, padx=5, pady=2, sticky=E)

        self.newbtn = Button(self, text="New User", command = self.newUser)
        self.newbtn.grid(row=3, column=1, sticky=W, pady=2)

        self.pack(side=TOP)

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

    def login_btn_clicked(self):

        try:
            with open('userData.json', 'r') as fp:
                userPassDict = json.load(fp)
        except:
            userPassDict = {}

        while True:
            username = self.entry_username.get()
            password = self.entry_password.get()

            if username in userPassDict:
                existingHash = userPassDict[username]
                if argon2.verify(password, existingHash):
                    tm.showinfo("Login info", "Welcome " + username)
                    break
                
                else:
                    tm.showinfo("Error", "Try again.")
                    break

            else:
                tm.showinfo("Error", "Try again.")
                break

root = Tk()
lf = LoginFrame(root)
root.mainloop()

