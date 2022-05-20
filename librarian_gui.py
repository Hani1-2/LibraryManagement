from librarian import *
from tkinter import *
from user import *
class Lib_screen(Tk,Frame):
    def __init__(self):
        super().__init__()
        self.title('LIBRARY')
        self.minsize(400, 500)
        self.maxsize(500, 800)
        self.screen1 = Frame(self)
        Label(self.screen1, text="LIBRARIAN", width="300", height="5" ,bg='cadet blue',font=("Bodoni MT Black", 15)).pack(
            side=TOP)
        self.config(bg='cadet blue')
        Button(self.screen1, text="Check Stock",bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="30", command=self.check_stock).pack()
        Button(self.screen1, text="Add Books",bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="30",command=self.Add_book).pack()
        self.screen1.pack()
        self.mainloop()

    def check_stock(self):
        self.sc1 = Toplevel(self.screen1)
        self.sc1.geometry("700x700")
        self.sc1.title("check_stock")
        Label(self.sc1, text="check_stock", bg='cadet blue', width="300", height="3", font=("Bodoni MT Black", 13)).pack()
        self.sc1.config(bg='cadet blue')
        Label(self.sc1, text="", bg='cadet blue').pack()
        Label(self.sc1, text="How many books you want to add ?", bg='cadet blue').pack()
        self.e10 = Entry(self.sc1)
        self.e10.pack()
        Button(self.sc1, text="check",bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="30",command = self.check_stock1).pack()

    def check_stock1(self):
        e1 = int(self.e10.get())
        Librarian.Total_Books_in_Library += e1
        Label(self.sc1, text=f"The total books in library is {Librarian.Total_Books_in_Library}", height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()

        print(Librarian.Total_Books_in_Library)
        self.sc1.mainloop()


    def Add_book(self):
        self.sc2 = Toplevel(self.screen1)
        self.sc2.geometry("600x600")
        self.sc2.title("Add Book")
        Label(self.sc2, text="Add Book", bg='cadet blue', width="300", height="3", font=("Bodoni MT Black", 13)).pack()
        self.sc2.config(bg='cadet blue')
        Label(self.sc2, text="", bg='cadet blue').pack()
        Label(self.sc2, text="Enter book name with author:",  height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.sc2, text="", bg='cadet blue').pack()
        self.e11 = Entry(self.sc2)
        self.e11.pack()
        Label(self.sc2, text="", bg='cadet blue').pack()
        Label(self.sc2, text="Enter price of book in dollars:",  height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.sc2, text="", bg='cadet blue').pack()
        self.e12 = Entry(self.sc2)
        self.e12.pack()
        Label(self.sc2, text="", bg='cadet blue').pack()
        Button(self.sc2, text="Add", fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="20", command=self.Add_books).pack()
        self.sc2.mainloop()
    def Add_books(self):
        bname1 = self.e11.get()
        aname2 = self.e12.get()
        BookItem.book[bname1] = aname2
        Librarian.Total_Books_in_Library += 1
        Label(self.sc2, text="", bg='cadet blue').pack()
        Label(self.sc2, text='Your book add successfully',  height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        print(BookItem.book)
# Lib_screen()

