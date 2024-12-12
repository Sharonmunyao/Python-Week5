# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

class Book:
    def __init__(self, color, genre, pages):
        self.color = color
        self.genre = genre
        self.pages = pages
    def read(self):
        return f"I am reading a {self.color} {self.genre} book"
    def bookmark(self):
        return f"I have placed a bookmark on the {self.pages} page book"

class miniBook(Book):
    def __init__(self, color, genre, pages, author, publisher, name):
        super().__init__(color, genre, pages)
        self.author = author
        self.publisher = publisher
        self.name = name
    def read(self):
        return(f"I am reading a {self.color} {self.genre} book by {self.author}")
    def bookmark(self):
        return f"I put the bookmark in the {self.color} book published by {self.publisher}"
    def highlight(self):
        return(f"I have highlighted the entire {self.name}")

book1 = Book("Red", "Fantasy", 1000)
book2 = miniBook("Blue", "Classic", 300, "Joe", "AmericanXpress", "Heidi")

print (book1.read())
print (book1.bookmark())
print (book2.read())
print (book2.bookmark())
print (book2.highlight())

