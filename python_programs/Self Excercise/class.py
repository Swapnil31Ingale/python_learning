# Write a Library class with no_of_books and books as 
# two instance variables. Write a program to create a library from 
# this Library class and show how you can print all books, add a book 
# and get the number of books using different methods. Show that 
# your program doesnt persist the books after the program is stopped!

class library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)
        
    def lib_details(self):
        print(f"No of books in library: {self.no_of_books} and the books are as below: ")
        for book in self.books:
            print(book)
              

lib1 = library()
lib1.add_book("ABC")
lib1.add_book("PQR")
lib1.add_book("UTY")
lib1.lib_details()
lib2 = library()
lib2.add_book("XYZ")
lib2.add_book("GHI")
lib2.lib_details()
    
        
        
