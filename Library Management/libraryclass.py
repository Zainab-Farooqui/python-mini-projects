class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def addbooks(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def info(self):
        print(f"Books are {self.books}")
        print(f"No of Books are {self.no_of_books}")
        
        if((self.no_of_books) != len(self.books)):
            print("Some Error!")
        else:
            print("All Good!")


obj = Library()
obj.addbooks("Harry Potter")
obj.addbooks("Harry Potter")
obj.addbooks("Harry Potter")
obj.addbooks("Harry Potter")
obj.addbooks("Harry Potter")
obj.info()

