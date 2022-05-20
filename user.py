###### Libarary User ########


class Address:#this class is use to print the city and the country in which the library is located in
  def __init__(self,city, country):
    self.__city = city
    self.__country = country
  def lib(self):#this function returns the location of library and is used to print it on the screen
    print(f'the library is in  {self.__city}  {self.__country} ')
class Person:#this class is used to take the name and email of the user as input
  dic = {}#we have initialized a dictionary so that we can place the name and email of the user in it for record
  member_id = 0 #used to assign an id ,unique for every person to the user
  def __init__(self, name, email):#this fuction is used to initialize the name and email
    self.name = name
    self.email = email

    Person.member_id += 1 #incrementing the id
    print('Your Id is',Person.member_id,'bring it when you return the book')

  def user_info(self):#this fuction is used to place the essential info of the user in the dictionary defined above
    Person.dic[Person.member_id] = [self.name, self.email]#this line of code is used to place the info of the user in a list and than into the dictionary defined above
    return Person.dic


# class Constants:
#     def __init__(self):
#         self.MAX_BOOKS_ISSUED_TO_A_USER = 5
#         self.MAX_LENDING_DAYS = 10
import datetime as dt #importing the date time module to keep track of the date
class date:
    def __init__(self):#this fuction is used to initialize the date
        self.due_day = 0
        self.creation_date = dt.datetime.now()#this line of code is used to keep track of the time the book was added,bought or the time it needs to be returned
        self.today = self.creation_date.strftime('%d')#formatting of the date in dd/mm/yy format
        self.due_date()#this line of code gives us the due date to return the book
    def issue_date(self):#this function is used to print thhe date and time the book was issued
        self.creation_date = dt.datetime.now()#gives the current date and time
        print('the book issued on', self.creation_date)
    def due_date(self):#this function gives us the time and date the book needs to be returned on
        self.month =self.creation_date.strftime('%m')
        if int(self.today) > 20 :
            if int(self.month)%2 == 0:
                due = 30 - int(self.today)
                self.due_day = 10 - due
            elif int(self.month)%2 != 0:
                due = 31 - int(self.today)
                self.due_day = 10 - due
        else:
            self.due_day = int(self.today) + 10
            # print('you have 10 days to return the book')
        return self.due_day
    def check_fine(self):#this fuction is used to check if fine is applicable or not
        # print('Welcome !!! Now you can return the book')
        day = input('Enter today date in local format dd/mm/yy')#takes the current date as input
        self.d = day[:2]
        self.m = day[3:5]
        print(self.month)
        if int(self.today)<= int(self.d) <=self.due_day:#this line of the code checks if the user is retrurning the book before the deadline or after the line 
            print('no fine')
        elif int(self.month) != self.m:#if the due date has been passed,fine is charged
            print('You\'re a month late , fine is applicable for you' )
        else:
            print('you run out of day , You have to pay of 50 Rs for fine')
class BookReservation(date):#this class is inheriting from the date class, because this class keeps track of when the book was reserved
  def __init__(self):
    super().__init__()#overriding the init method of the date class
    # d = date()
    # self.__creation_date = d.creation_date
  def add_book(self):#this fuction takes the name of the book and the author so that the book can be reserved
    book_name = input('enter book name')
    author_name = input('enter author name')
    BookItem.book[book_name]=author_name
    print('your book add successfully')


  def return_book(self):#this fuction is used to get the retrurned book
    id = int(input('enter your Id please'))#we take the id of the user as input
    x = Person.dic.get(id)#it first checks if the user has lend the book
    if len(x)==2:#this line of code checks the users id in the dictionary to see if any book is found there, if the list only shows the name and email than it promts the user to lend the book first
        print('first lend then return the book')
    else:#this line is run if the user has indeed lend the book
        print('you lend the book',Person.dic[id][2])#this line of code gets the book the user lended
        date.check_fine(self)#this line checks if fine is applicable or not by calling the date class
        print('Your book return successfully')

  def fetch_reservation_details(self):#gets the details regarding reservation
    reserve = input('enter the name of book you want to reserve')
    if reserve not in BookItem.book:#sees if the mentioned book is in the book dictionary
        print('Book is not available to reserve')
    else:
        print('your book is reserve now, you can lend it whenever you want')



class BookItem:#contains the list of books available


    book = {'silent patient by Alex Michaelides': '90$','alchemist by polu coello':'50$', 'One Hundred Years of Solitude by  Gabriel García Márquez':'100$' ,'War and Peace by Leo Tolstoy':'80$','Lolita by Vladimir Nabokov':'40$','In Search of Lost Time by Marcel Proust':'120$','Ulysses by abc':'100$',
             'The Great Gatsby by':'120$','One Hundred Years of Solitude by Gabriel Garcia Marquez':'100$' ,'Hamlet by William Shakespeare':'200$','harry potter by JK Rowling':'200$','The Handmaid\'s Tale by Margaret Atwood':'30$',
             'Educated by Tara Westover':'45$','Where the Crawdads Sing by Delia Owens':'39$','A Thousand Splendid Suns by Khaled Hosseini':'90$'}
  
class BookLending(BookItem,date):#inherits from BookItem and date
  def __init__(self):
    super().__init__()#overrriding the init method of date class
    self.d=date()#the date class is passed as an instance here,without which the book lending class would not work,hinting towards composition
  def lend_book(self):
    try:#exception is used here for errors
      user_input = input('Enter the name of book you want to lend')
      if user_input in BookItem.book:#checking if the entered book is available in the library or not
        print(f'the book{user_input} is issued')#lending the wanted book
        print(f'the issued date is {self.d.creation_date}')#used to print the date the book was issued on
        print(f'the due date is {self.d.due_day}')#used to print the due date to return the book
        Person.dic[Person.member_id].append(user_input)#this line of code appends the lended book to the user in the dictionary to keep track


      else:
        print('Book is not available')
    except:
      print('try it again')
          
#






