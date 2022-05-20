from librarian_gui import *
from library_gui import *  # importing all the funcutionality og gui module
from librarian import *
from user import *  # importing the librarian class for further usage
from tkinter import *  # used to import all the functionality from the module tkinter
#import PIL
import sys
sys.path.append('libraryManagement')
# after importing librarian as a module we import all the funtionality of the libra#rian class


class Id:  # this function is used to increment the id of the user
    def idd(self):
        with open('user_login', 'r') as f:  # this line is used to open the file in read mode
            x = f.readlines()  # this line return the list in a string
            if '\n' in x:  # used to check the last id that was assigned so that the next user is given incremented id
                x.remove('\n')
                print(x)
            if x == []:  # sees if no id has been assigned yet so it assumes the id as 0
                self.new_id = 0
            else:
                self.new_id = (x[-1][0])  # gets the last id assigned


class main_screen(Tk):
    id = 0

    def __init__(self, id=0):
        super().__init__()  # overriding the dunder of the Tk class
        i = Id()  # making i an instance of ID ,composition is used here
        i.idd()  # defining a function with in a function and then calling it to check the id
        main_screen.id = int(i.new_id)  # sets the id as the last id assigned
        # main_screen.id = main_screen.new_id
        self.geometry("300x300")  # used to set the size of the screen
        # used to put the title on the top
        self.title("LIBRARY MANAGEMENT SYSTEM")
        # setting the width,height,font in which the title is printed and placing it on the screen using pack
        Label(self, text="LIBRARY MANAGEMENT SYSTEM", bg='pink',
              width="300", height="3", font=("Calibri", 13)).pack()
        self.config(bg='cadet blue')  # setting the background color
        Label(self, text="").pack()
        # placing a button named user on the screen,second screen here creates a second screen on the interface
        Button(self, text="USER", height="3", width="30",
               command=self.second_screen).pack()
        Label(self, text="").pack()
        Label(self, text="").pack()
        # used to place the librarian botton on the screen
        Button(self, text="LIBRARIAN", height="3",
               width="30", command=Lib_screen).pack()

        self.mainloop()  # an infinite loop to run the gui till called off

    # creating a screen after the librarian/user screen that asks the user to login or register
    def second_screen(self):
        self.s1 = Toplevel(self)
        self.s1.geometry("300x300")
        self.s1.title("LIBRARY MANAGEMENT SYSTEM")
        Label(self.s1, text="LIBRARY MANAGEMENT SYSTEM", bg='pink',
              width="300", height="3", font=("Calibri", 13)).pack()
        self.s1.config(bg='cadet blue')
        Label(self.s1, text="").pack()
        Button(self.s1, text="Login", height="3",
               width="30", command=self.login).pack()
        Label(self.s1, text="").pack()
        Label(self.s1, text="").pack()
        Button(self.s1, text="Register", height="3",
               width="30", command=self.register).pack()
        self.s1.mainloop()

    def login(self):  # used to ask the user to enter the credensitials to login
        self.screen1 = Toplevel(self.s1)
        self.screen1.title("Login")
        self.screen1.geometry("350x350")
        Label(self.screen1, text="LOGIN", bg='cadet blue',
              width="300", height="3", font=("Calibri", 13)).pack()
        Label(self.screen1, text="Please enter details below to login").pack()
        Label(self.screen1, text="").pack()

        # used to verify the entered username by comparing it with names in the log
        self.username_verify = StringVar()
        # used to verify the eentered password by comparing it with password in the log
        self.password_verify = StringVar()
        # used to identify the entered id by comparing it with password in the log
        self.id = StringVar()
        Label(self.screen1, text="Username * ").pack()
        self.username_entry1 = Entry(
            self.screen1, textvariable=self.username_verify)
        self.username_entry1.pack()
        Label(self.screen1, text="").pack()
        Label(self.screen1, text="Password * ").pack()
        self.password_entry1 = Entry(
            self.screen1, textvariable=self.password_verify)
        self.password_entry1.pack()
        Label(self.screen1, text="").pack()
        Label(self.screen1, text="Id * ").pack()
        self.id_entry1 = Entry(self.screen1, textvariable=self.id)
        self.id_entry1.pack()
        Label(self.screen1, text="").pack()
        Button(self.screen1, text="Login", width=10,
               height=2, command=self.login_verify).pack()

    # displays a login successful screen after the correct info has been entered
    def login_sucess(self):
        self.screen2 = Toplevel(self.screen1)
        self.screen2.title("Success")
        self.screen2.geometry("150x100")
        Label(self.screen2, text="Login Sucess").pack()
        # command = delete2
        Button(self.screen2, text="OK", command=Main_Screen).pack()

    # displays a screen that tells the user if the entered password is wrong
    def password_not_recognised(self):
        self.screen3 = Toplevel(self.screen1)
        self.screen3.title("Success")
        self.screen3.geometry("150x100")
        Label(self.screen3, text="Password Error").pack()
        Button(self.screen3, text="OK", command=self.screen3.destroy).pack()

    def user_not_found(self):  # telling the user if the entered password or id is not found
        self.screen4 = Toplevel(self.screen1)
        self.screen4.title("Success")
        self.screen4.geometry("150x100")
        Label(self.screen4, text="User Not Found").pack()
        # command = delete4
        Button(self.screen4, text="OK", command=self.screen4.destroy).pack()

    def login_verify(self):  # verifing the password and username
        username1 = self.username_verify.get()
        password1 = self.password_verify.get()
        id1 = self.id.get()  # gets the id of the user
        self.username_entry1.delete(0, END)
        self.password_entry1.delete(0, END)
        self.id_entry1.delete(0, END)

        with open('user_login', 'r') as f:  # opening the file of user log
            value = f.read()  # reading it
            # this line of the code will run if the id,password and username are correct
            if (id1+','+username1+' '+password1)in value:
                self.login_sucess()  # calling the login success fuction to display the screen
            else:  # if user is not found than we xcall the user not found fuction to display it on the screen
                self.user_not_found()

    def register(self):  # used to display the register button on the screen
        self.screen = Toplevel(self.s1)
        self.screen.title("Register")
        self.screen.geometry("300x300")
        Label(self.screen, text="REGISTERATION", bg='cadet blue',
              width="300", height="3", font=("Calibri", 13)).pack()

        self.username = StringVar()  # storing the username entered
        self.password = StringVar()  # storing the password entered

        Label(self.screen, text="Please enter details below").pack()
        Label(self.screen, text="").pack()
        Label(self.screen, text="Username * ").pack()

        self.username_entry = Entry(
            self.screen, textvariable=self.username).pack()
        Label(self.screen, text="Password * ").pack()
        self.password_entry = Entry(
            self.screen, textvariable=self.password).pack()
        Label(self.screen, text="").pack()
        Button(self.screen, text="Register", width=10,
               height=1, command=self.register_user).pack()

    def register_user(self):  # used to register a user
        print("working")
        username_info = self.username.get()
        password_info = self.password.get()
        main_screen.id += 1
        # this line of code is used to open the log file
        file = open('user_login', "a+")
        # it appends all the info entered by the user in the file
        file.write(str(main_screen.id)+','+username_info +
                   ' ' + password_info+','+'\n')

        file.close()

        Label(self.screen, text="Registration Sucess",
              fg="green", font=("calibri", 11)).pack()
        Label(self.screen, text='')
        Label(
            self.screen, text=f'Your id is {main_screen.id} bring it when you comeback').pack()


main_screen()
