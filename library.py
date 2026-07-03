#A simple library management system in Python

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        
    def borrow_book(self):
        pass
    
    def return_book(self):
        pass
    
    def display_info(self):
        pass
    

class Library:
    def __init__(self, books):
        self.books = []
        
    def add_book(self, book):
        pass
    
    def show_book(self):
        pass
    
    def boorrow_book(self, title):
        pass
    
    def return_book(self, title):
        pass
        