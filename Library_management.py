# # Define a library management class which has a dictionary of books where key is 
# # 1. The book id and value is a tuple consisting of title, author and price.
# # 2. Keep function for addition and deletion of the books.
# # 3. Keep function for issuing books and receive returns with provisions for fine of rupee 1/- per day


from  datetime import datetime,timedelta 

class library_management:
    books = {101:("Time","Somen",200),102:("Space","SK",130),103:("Earth","Akash",230)} 
    issue_books = {}
    def addition(self,id,title,author,price):
        if id not in self.books:
            self.books[id] = (title,author,price) 
            print(f"Book of title {title} added successfully!")
        else:
            print("Book already available")

    def deletion(self):
        if id in self.books:
            del self.books[id]
            print(f"Book of title {title} deleted successfully!")
        else:
            print("No such book exist")

    def issue(self,id):
        if id in self.books:
            today=datetime.today()
            return_date = today+timedelta(7)
            self.issue_books[id] = (self.books[id],return_date)
            print(f"Return date of book id {id} is {return_date}")
            del self.books[id]
        else:
            print("No such book in library")

    def returning(self,id):
        if id in self.issue_books:
            self.books[id] = self.issue_books[id][0]
            print(f"Book of id {id} returned successfully!")
