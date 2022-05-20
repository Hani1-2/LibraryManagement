from tkinter import *

from user import date, Person, BookItem
from librarian import *
#from PIL import ImageTk


class User:  # this class is used to maintain the user log
    d = {}  # this line creates a dictionary to store all the credentials and important info of the user

    def __init__(self):
        self.USER_LOG()

    def USER_LOG(self, n='user_login'):  # passing the file as a parameter
        self.n = n
        with open(self.n, 'r') as f:  # this statement is used to open the file
            # reads the lines of the file and returns its len
            x = len(f.readlines())
            f.seek(0)
            for i in range(x):
                v = f.readline()
                v1 = v.split(',')  # splits the line on the basis of colon
                if '\n' in v1:
                    # this removes that \n and gets the last value assigned to any user, so that a next id can be assigned to the user
                    v1.remove('\n')
                User.d[v1[0]] = v1[1:]


# this class is used to create all the custom functionality and place it on the screen
class Main_Screen(Tk, Frame):
    def __init__(self):
        super().__init__()
        self.date = date  # calling the date class and passing it as the value to an instance
        # calling the book item class and passing it as a value to an instance
        self.Book = BookItem.book
        self.title('LIBRARY')  # used to place the title
        self.geometry('800x900')
        self.screen = Frame(self)  # used to place a frame in the screen
        Label(self.screen, text="WELCOME TO LIBRARY", width="300", height="5", font=("Bodoni MT Black", 15)).pack(
            side=TOP)
        self.config(bg='cadet blue')
        # photo = ImageTk.PhotoImage(file=r'C://Users/Hp/PycharmProjects/CEP1/book1.png' )
        # Label(self.screen, image=photo).pack()
        # the button command is used to place the buttons regarding different functionality on the screen
        Button(self.screen, text="Display Book", width='20', height='2', fg='black', font=("Calibri", 10, "bold"), bd=6, bg='pink',
               command=self.displaybook).pack()
        Button(self.screen, text="General Info ", width='20', height='2', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, bg='olive drab1', command=self.GeneralInfo).pack()
        Button(self.screen, text="Lend Book", width='20', height='2', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, bg='powder blue', command=self.Lend_Book).pack()
        Button(self.screen, text="Book Reservation", width='20', height='2', fg='black', font=("Calibri", 10, "bold"), bd=6, bg='plum1',
               command=self.book_reserve).pack()
        Button(self.screen, text="Return Book", width='20', height='2', fg='black', font=("Calibri", 10, "bold"), bd=6, bg='MediumPurple1',
               command=self.Return_Book).pack()
        Button(self.screen, text="Library Info", width='20', height='2', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, bg='yellow', command=self.LIBRARY_INFO).pack()
        Button(self.screen, text="Payment Method", width='20', height='2', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, bg='khaki1', command=self.payment).pack()
        Button(self.screen, text="Maintain Log", width='20', height='2', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, bg='PaleGreen3', command=self.Maintain_USerLog).pack()
        # this button is used to destroy the screen that displays the custom functionality
        Button(self.screen, text="Exit", width='20', height='2', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, bg='PaleGreen3', command=self.destroy).pack()
        Label(self.screen, text="CHOOSE ONE OPTION", width="300",
              height="8", font=("Bodoni MT Black", 15)).pack()

        self.screen.pack()
        self.mainloop()  # displaying all the gui features on the screen

    # this function is used to display the gui format for the information regarding the library address
    def LIBRARY_INFO(self):
        # used to place anything at the top of the screen
        self.s1 = Toplevel(self.screen)
        self.s1.geometry("300x300")  # setting the size of the screen
        self.s1.title("LIBRARY INFO")
        Label(self.s1, text="LIBRARY INFO", bg='cadet blue', width="300",
              height="3", font=("Bodoni MT Black", 13)).pack()
        self.s1.config(bg='cadet blue')
        Label(self.s1, text="", bg='cadet blue').pack()
        Button(self.s1, text="CHECK INFO", bg='turquoise', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, height="3", width="30", command=self.Address).pack()
        self.s1.mainloop()

    def Address(self):  # used to display the address of the library
        Label(self.s1, text="", bg='cadet blue').pack()
        Label(self.s1, text=f'The library is in  Karachi , Pakistan ',
              height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    # this function checks whether fine is applicable but does it in a gui format,
    def Check_Fine(self):
        # this function is using the features of the date class
        self.s3 = Toplevel(self.screen)
        self.s3.geometry("700x700")
        self.s3.title("CHECK FINE")
        Label(self.s3, text="CHECK FINE", bg='cadet blue', width="300",
              height="3", font=("Bodoni MT Black", 13)).pack()
        self.s3.config(bg='cadet blue')
        Label(self.s3, text="", bg='cadet blue').pack()
        Label(self.s3, text="", bg='cadet blue').pack()
        Label(self.s3, text='Fine applied if you return book after 10 days',
              height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s3, text="", bg='cadet blue').pack()
        self.day = self.date()
        self.x = self.day.due_day
        Button(self.s3, text="Check Fine", bg='turquoise', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, height="3", width="30", command=self.check_fine).pack()
        self.s3.mainloop()

    def check_fine(self):  # this function is used to place all the features regarding the fine issued on the screen
        # and is directly related to the Check_Fine function defined above
        # e7 here represents the entries that we have made till now to be displayed on the screen,
        y = self.e7.get()
        # this enytry checks if the user has lend a book or not
        # recalls if any book is lended by using the id of the user as refrence,
        l = User.d[self.idd]
        # it then searches in the user log to see which books lended by user.
        try:
            if y not in l:
                Label(self.s3, text='You dont lend this book ').pack()
            else:
                l.remove(y)
                print(l)
                Label(self.s3, text='', bg='cadet blue').pack()
                Label(self.s3, text='Welcome !!! Now you can return the book', height="3", font=(
                    "Calibri", 10, "bold"), bg='cadet blue').pack()
                Label(self.s3, text='', bg='cadet blue').pack()
                l = Label(self.s3, text='Enter today date in local format dd/mm/yy',
                          height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
                self.e1 = Entry(self.s3)
                self.e1.pack()
                Label(self.s3, text='', bg='cadet blue').pack()
                self.dat = date()
                self.dat.issue_date()
                self.dat.due_date()
                Button(self.s3, text='click', bg='turquoise', fg='black', font=(
                    "Calibri", 10, "bold"), bd=6, height="3", width="30", command=self.fine).pack()
        except:
            Label(self.s3, text='First lend the book sorry!!!', height="3",
                  font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def Maintain_USerLog(self):
        self.s7 = Toplevel(self.screen)
        self.s7.geometry("500x500")
        self.s7.title("Maintain User Log")
        Label(self.s7, text="Maintain User Log", bg='cadet blue',
              width="300", height="3", font=("Bodoni MT Black", 13)).pack()
        self.s7.config(bg='cadet blue')
        Label(self.s7, text="", bg='cadet blue').pack()
        Label(self.s7, text="Enter your Id please", height="3",
              font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s7, text="", bg='cadet blue').pack()
        self.e8 = Entry(self.s7)
        self.e8.pack()
        Button(self.s7, text="check_log", bg='turquoise', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, height="3", width="30", command=self.history).pack()
        self.s7.mainloop()

    def history(self):  # this function is used to display the log of the user to him when he exits or write the log of the user in user_history file
        string = ''
        self.c = self.e8.get()
        try:
            if self.c in self.a.d:
                self.log = self.a.d[self.c]
                print(self.log)
                for i in self.log:
                    string += (i+',')
                print(string)
            else:
                User()
                if self.c in User.d:
                    for i in self.log:
                        string += (i + ',')
                    print(string)
        except:
            Label(self.s7, text='You don\'t have any log', bg='cadet blue').pack()

        with open('user_history', 'a') as f1:
            # here you can change file formatting
            y = f1.write(str(self.c)+','+''+string+'\n')
            Label(self.s7, text=f'Your id is {self.c}', height="3", font=(
                "Calibri", 10, "bold"), bg='cadet blue').pack()
            Label(self.s7, text='', bg='cadet blue').pack()
            Label(self.s7, text=f'and your history is {string}', height="3", font=(
                "Calibri", 10, "bold"), bg='cadet blue').pack()

    def fine(self):  # checks for the fine and is directly related to the date class
        e = self.e1.get()
        self.d = e[:2]
        self.m = e[3:5]
        # print(type(e))
        # print(self.day.today, int(self.d), self.day.due_day)
        try:
            if int(self.day.today) <= int(self.d) <= self.day.due_day:
                Label(self.s3, text='', bg='cadet blue').pack()
                Label(self.s3, text='no fine', height="3", font=(
                    "Calibri", 10, "bold"), bg='cadet blue').pack()
                Label(self.s3, text='Your book return successfully', height="3", font=(
                    "Calibri", 10, "bold"), bg='cadet blue').pack()
            else:
                Label(self.s3, text='you run out of day , You have to pay of 50 Rs for fine',
                      height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        except:
            Label(self.s3, text='Sorry!!! check your input', height="3",
                  font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def Return_Book(self):  # used to display the return book widget on the screen and is directly related to the date class imported above
        self.s3 = Toplevel(self.screen)
        self.s3.geometry("800x800")
        self.s3.title("Return Book")
        Label(self.s3, text="Return Book", bg='cadet blue', width="300",
              height="2", font=("Bodoni MT Black", 13)).pack()
        self.s3.config(bg='cadet blue', height="4")
        Label(self.s3, text="", bg='cadet blue').pack()
        self.day = self.date()
        self.x = self.day.due_day
        Button(self.s3, text="return book", bg='turquoise', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, height="2", width="30", command=self.return_book).pack()
        self.s3.mainloop()

    # used to take the id as input and then checks if any book has been lended or not
    def return_book(self):
        Label(self.s3, text="",  bg='cadet blue').pack()
        Label(self.s3, text='enter your Id please:', height="3",
              font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        self.e2 = Entry(self.s3)
        self.e2.pack()
        Label(self.s3, text='',  bg='cadet blue').pack()
        Button(self.s3, text='click', bg='turquoise', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, command=self.returnb).pack()

    def returnb(self):  # takes the name of the book that the user wants to return ad input and also is used to put the gui widgets on the screen
        self.idd = self.e2.get()
        try:
            if self.idd in self.a.d:
                x = self.a.d[self.idd]
                print(x)
                print(len(x))
                if len(x) == 1:
                    Label(self.s3, text='Before Exit , kindly maintain your log first after lend any book ',
                          height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
                    Label(self.s3, text='So that you can return the book', height="3", font=(
                        "Calibri", 10, "bold"), bg='cadet blue').pack()
                    Label(self.s3, text='where you can see either you lend any book or not',
                          height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
                else:
                    Label(self.s3, text=f'you lend the book {x[1:]}', height="3", font=(
                        "Calibri", 10, "bold"), bg='cadet blue').pack()
                    Label(self.s3, text='', bg='cadet blue').pack()
                    Label(self.s3, text='Enter book name you want to return', height="3", font=(
                        "Calibri", 10, "bold"), bg='cadet blue').pack()
                    self.e7 = Entry(self.s3)
                    self.e7.pack()
                    Label(self.s3, text='', bg='cadet blue').pack()
                    Button(self.s3, text='check fine', bg='turquoise', fg='black', font=("Calibri", 10, "bold"), bd=6,
                           command=self.check_fine).pack()
            else:
                User()
                x = User.d[(self.idd)]
                print(x)
                if len(x) == 1:
                    Label(self.s3, text='Before Exit , kindly maintain your log first , so that you can return the book ',
                          height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
                    Label(self.s3, text='So that you can return the book', height="3", font=("Calibri", 10, "bold"),
                          bg='cadet blue').pack()
                    Label(self.s3, text='where you can see either you lend any book or not', height="3",
                          font=("Calibri", 10, "bold"), bg='cadet blue').pack()
                else:
                    Label(self.s3, text=f'you lend the book {x[1:]}',  height="3", font=(
                        "Calibri", 10, "bold"), bg='cadet blue').pack()
                    Label(self.s3, text='', bg='cadet blue').pack()
                    Label(self.s3, text='Enter book name you want to return',  height="3", font=(
                        "Calibri", 10, "bold"), bg='cadet blue').pack()
                    self.e7 = Entry(self.s3)
                    self.e7.pack()
                    Label(self.s3, text='', bg='cadet blue').pack()
                    Button(self.s3, text='check fine', bg='turquoise', fg='black', font=(
                        "Calibri", 10, "bold"), bd=6, command=self.check_fine).pack()
        except:
            Label(self.s3, text='Invalid Input',  height="3", font=(
                "Calibri", 10, "bold"), bg='cadet blue').pack()

    def Lend_Book(self):  # displays the lend book features on the screen
        self.s2 = Toplevel(self.screen)
        self.s2.geometry("800x800")
        self.s2.title("LEND BOOK")
        self.s2.Book = BookItem.book
        Label(self.s2, text="Lend Book", bg='cadet blue', width="300",
              height="3", font=("Bodoni MT Black", 13)).pack()
        self.s2.config(bg='cadet blue')
        Label(self.s2, text='You have 10 days to return the book',
              height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s2, text="Enter your Id please", height="3",
              font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        self.u = Entry(self.s2)
        self.u.pack()
        Button(self.s2, text='click', bg='turquoise', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, height="1", width="30", command=self.lend_id).pack()

    def lend_id(self):  # used to take the name of the book that the user wants to lend as input and display related widgets on the screen
        self.b = self.u.get()
        Label(self.s2, text="",  bg='cadet blue').pack()
        Label(self.s2, text='Enter the name of book you want to lend:',
              height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        self.e3 = Entry(self.s2)
        self.e3.pack()
        Label(self.s2, text='',  bg='cadet blue').pack()
        Button(self.s2, text='price', bg='turquoise', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, height='3', width="30", command=self.price).pack()
        Label(self.s2, text='',  bg='cadet blue').pack()
        Button(self.s2, text='lend', bg='turquoise', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, height="3", width="30", command=self.lend_book).pack()
        self.day = self.date()
        self.x = self.day.due_day
        Label(self.s2, text='',  bg='cadet blue').pack()
        Button(self.s2, text='confirm order', bg='turquoise', fg='black', font=(
            "Calibri", 10, "bold"), bd=6, height="1", width="30", command=self.log1).pack()
        self.s2.mainloop()

    def price(self):  # this fuction fetch the price of book
        x = self.e3.get()
        Label(self.s2, text='', bg='cadet blue').pack()
        if x in BookItem.book:
            n = BookItem.book[x]
            Label(self.s2, text=f'The price of book is {n}', height="3", font=(
                "Calibri", 10, "bold"), bg='cadet blue').pack()
        else:
            Label(self.s2, text='Please check the name of book', height="3",
                  font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def log1(self):  # this function is used to append all the information or basically history of the user and is calleed when the user maintains his log
        self.k = self.b
        self.a = User()
        self.a.USER_LOG('user_history')
        try:
            if self.k in self.a.d:
                self.c = str(self.e3.get())
                self.a.d[self.k].append(self.c)
                print(self.a.d)
            else:
                User()
                if self.k in User.d:
                    self.User.d[self.k].append(self.c)
                    print(self.User.d)
        except:
            Label(self.s2, text='Please check the name of book', height="3",
                  font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def lend_book(self):  # this function is used to check the date on which the book is issued and the due date as well
        book = BookItem.book
        e = str(self.e3.get())
        from user import date
        if e in book:
            Label(self.s2, text=f'the book {e} is issued', height="3", font=(
                "Calibri", 10, "bold"), bg='cadet blue').pack()
            w = date.issue_date(self)
            Label(self.s2, text=f'The issue date is {self.creation_date}', height="3", font=(
                "Calibri", 10, "bold"), bg='cadet blue').pack()
            Label(self.s2, text=f'The due date is {self.x}', height="3", font=(
                "Calibri", 10, "bold"), bg='cadet blue').pack()
        else:
            Label(self.s2, text='Book is not available', height="3",
                  font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    # this function is used to display all the gui widgets related to reserving books on the main screen
    def book_reserve(self):
        self.s4 = Toplevel(self.screen)
        self.s4.geometry("400x400")
        self.s4.title("Book Reservation")
        Label(self.s4, text="Book Reservation", bg='cadet blue',
              width="300", height="3", font=("Bodoni MT Black", 15)).pack()
        self.s4.config(bg='cadet blue')
        Label(self.s4, text="", bg='cadet blue').pack()
        Label(self.s4, text="", bg='cadet blue').pack()
        Button(self.s4, text="Add Book", fg='black', font=("Calibri", 10, "bold"),
               bd=6, height="3", width="30", bg='PaleGreen', command=self.add_books).pack()
        Label(self.s4, text="", bg='cadet blue').pack()
        Label(self.s4, text="", bg='cadet blue').pack()
        Button(self.s4, text="Reservation Details", fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="30", bg='PaleGreen',
               command=self.fetch_reservation_detail).pack()
        self.day = self.date()
        self.x = self.day.due_day
        self.s4.mainloop()

    def add_books(self):  # this function is used to display all the gui widgets related to adding books on the main screen
        self.s5 = Toplevel(self.screen)
        self.s5.geometry("600x600")
        self.s5.title("Add Book")
        Label(self.s5, text="Add Book", bg='cadet blue', width="300",
              height="3", font=("Bodoni MT Black", 13)).pack()
        self.s5.config(bg='cadet blue')
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="Enter book name:",  height="3",
              font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        self.e4 = Entry(self.s5)
        self.e4.pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="Enter author name:",  height="3",
              font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        self.e5 = Entry(self.s5)
        self.e5.pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        Button(self.s5, text="Add", fg='black', font=("Calibri", 10, "bold"),
               bd=6, height="3", width="20", command=self.add_book).pack()

    def add_book(self):  # this function is used to add book in the library stock by the user,basically donating it to the library
        bname = self.e4.get()
        aname = self.e5.get()
        BookItem.book[bname] = aname
        Librarian.Total_Books_in_Library += 1
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text='Your book add successfully',  height="3",
              font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        print(BookItem.book)

    # this function is used to display all the gui widgets regarding reservation on the screen
    def fetch_reservation_detail(self):
        self.s6 = Toplevel(self.screen)
        self.s6.geometry("600x600")
        self.s6.title("Fetch Reservation Details")
        Label(self.s6, text="Fetch Reservation Details", bg='cadet blue', width="300", height="3",
              font=("Bodoni MT Black", 13)).pack()
        self.s6.config(bg='cadet blue')
        Label(self.s6, text="", bg='cadet blue').pack()
        Label(self.s6, text="Enter the name of book you want to reserve:",
              height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s6, text="", bg='cadet blue').pack()
        self.e6 = Entry(self.s6)
        self.e6.pack()
        Label(self.s6, text="", bg='cadet blue').pack()
        Button(self.s6, text="Reserve", fg='black', font=("Calibri", 10, "bold"),
               bd=6, height="3", width="20", command=self.fetch_reservation_details).pack()

    def fetch_reservation_details(self):
        # this function checks if the book wanted by user is available in the library or not
        Label(self.s6, text="", bg='cadet blue').pack()
        re = str(self.e6.get())
        from user import BookReservation
        if re not in BookItem.book:
            Label(self.s6, text='Book is not available to reserve', height="3", font=(
                "Calibri", 10, "bold"), bg='cadet blue').pack()
        else:
            Label(self.s6, text='We have this book in our library, so you can lend it whenever you want',
                  height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def payment(self):  # this function is used to display all the gui labels and buttons on the screen
        self.s8 = Toplevel(self.screen)
        self.s8.geometry("500x500")
        self.s8.title("PAYMENT")
        Label(self.s8, text="PAYMENT", bg='cadet blue', width="300",
              height="3", font=("Bodoni MT Black", 13)).pack()
        self.s8.config(bg='cadet blue')
        Label(self.s8, text="", bg='cadet blue').pack()
        Label(self.s8, text=" enter your id", bg='cadet blue').pack()
        self.e9 = Entry(self.s8)
        self.e9.pack()
        Button(self.s8, text='click', bg='turquoise', fg='black', font=("Calibri", 10, "bold"), bd=6, height="2",
               width="30", command=self.paycheck1).pack()
        Label(self.s8, text="", bg='cadet blue').pack()
        self.s8.mainloop()

    def paycheck1(self):  # this function is used to take the payment of the book reserved,added
        self.ci = self.e9.get()
        try:
            if self.ci in self.a.d:
                xi = self.a.d[self.ci]
                print(len(xi))
                if len(xi) <= 1:
                    Label(
                        self.s8, text="You dont take any book , so why you want to pay", bg='cadet blue').pack()
                else:
                    x = self.a.d[self.ci]
                    Label(
                        self.s8, text=f'You have to pay for {x[1:]}', bg='cadet blue').pack()
                    Label(self.s8, text='').pack()

                    Label(self.s8, text="", bg='cadet blue').pack()
                    Label(self.s8, text="Enter your Account No for payment", height="3", font=("Calibri", 10, "bold"),
                          bg='cadet blue').pack()
                    self.e5 = Entry(self.s8)
                    self.e5.pack()
                    Label(self.s8, text="", bg='cadet blue').pack()
                    Button(self.s8, text='click', bg='turquoise', fg='black', font=("Calibri", 10, "bold"), bd=6,
                           height="2", width="30", command=self.paycheck).pack()

            elif self.ci in User.d:
                x1 = User.d[self.ci]
                print(len(x1))
                if len(x1) <= 1:
                    Label(
                        self.s8, text="You dont take any book , so why you want to pay", bg='cadet blue').pack()
                else:
                    x = self.a.d[self.ci]
                    Label(
                        self.s8, text=f'You have to pay for {x[1:]}', bg='cadet blue').pack()
                    Label(self.s8, text='').pack()

                    Label(self.s8, text="", bg='cadet blue').pack()
                    Label(self.s8, text="Enter your Account No for payment", height="3", font=("Calibri", 10, "bold"),
                          bg='cadet blue').pack()
                    self.e5 = Entry(self.s8)
                    self.e5.pack()
                    Label(self.s8, text="", bg='cadet blue').pack()
                    Button(self.s8, text='click', bg='turquoise', fg='black', font=("Calibri", 10, "bold"), bd=6,
                           height="2", width="30", command=self.paycheck).pack()
        except:
            Label(self.s8, text='frist lend book please', bg='cadet blue').pack()

    def paycheck(self):  # this function is used to display the label on the screen that the amount charged has been paied
        self.Ac = self.e5.get()
        try:
            if len(self.a.d[self.ci]) <= 1:
                Label(self.s8, text='Zero amount deducted', height="3",
                      font=("Calibri", 10, "bold"), bg='cadet blue').pack()

            elif self.Ac.isdigit():
                Label(self.s8, text='Amount is paid', height="3", font=(
                    "Calibri", 10, "bold"), bg='cadet blue').pack()
                Label(self.s8, text='Thank you come again', height="3",
                      font=("Calibri", 10, "bold"), bg='cadet blue').pack()
            else:
                Label(self.s8, text='Invalid Account No', height="3",
                      font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        except:
            Label(self.s8, text='sorry some payment error', height="3",
                  font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def GeneralInfo(self):  # this function is used to display the general rules about the libraray
        self.s5 = Toplevel(self.screen)
        self.s5.geometry("600x600")
        self.s5.title("General Info")
        Label(self.s5, text="General Info", bg='cadet blue', width="300",
              height="3", font=("Bodoni MT Black", 13)).pack()
        self.s5.config(bg='cadet blue')
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="Welcome to Student Library", height="3",
              font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="You can lend books for 10 days", height="3",
              font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="After 10 days fine will be applicable to all students",
              height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="You can reserve book and Add books of your choice",
              height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="There is a payment method by Account",
              height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    # this function is used to display the information and names of the book on the screen
    def displaybook(self):
        self.s6 = Toplevel(self.screen)
        self.s6.geometry("600x600")
        self.s6.title("Display Book")
        Label(self.s6, text="Display Book", bg='cadet blue', width="300",
              height="3", font=("Bodoni MT Black", 13)).pack()
        self.s6.config(bg='cadet blue')
        Label(self.s6, text="", bg='cadet blue').pack()
        for i in BookItem.book:
            Label(self.s6, text=f'{i}\n', height="3", font=(
                "Calibri", 10, "bold"), bg='cadet blue').pack()
# Main_Screen()
