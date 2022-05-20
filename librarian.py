from abc import ABC, abstractmethod
#importing the abstract class module

class Account(ABC):#passing abstract class as parameter so that further instance of this class can not be created,
#the reason that we have made trhis class abstracy because we wnant to secure user privacy
  def __init__(self, id, password, person,email):#this constructor takes the essential credisentials of the user and librarian as password
    self.__id = id
    self.__password = password
    self.email=email
    self.__person = person
  def resetPassword(self,NewPassword):#this function is used to reset the password
      self.__password=NewPassword

class Librarian(Account):#this class inherits from the abstract class Account,so that we can use its attributes

  Total_Books_in_Library=500
  def __init__(self, id=1, password=1234, person='Librarian',email='Lib@gmail.com'):#we have used method overriding here, and have called the constructor of the account class here
    super().__init__(id, password, person,email)
  def add_book_item(self,AddBooks=0):#this fuction is use to update the stock of the books or add new books
      self.Add_Books_in_Library=AddBooks
      self.Add_Books_in_Library+=Librarian.Total_Books_in_Library
      Librarian.Total_Books_in_Library+=self.Add_Books_in_Library
  def get_Num_Books(self):#this fuction is used to get the number of books present in the library
    return("The Total Number of book present in the Library are",self.Add_Books_in_Library)

# a1=Librarian(1,'rmt','user','rmt')
# a1.add_book_item(500)
# print(a1.get_Num_Books())
# a2=Librarian(1,'rmt','user','rmt')
# a2.add_book_item(200)
# print(a2.get_Num_Books())
