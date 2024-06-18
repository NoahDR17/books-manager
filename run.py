class Book:
    def __init__(self, name, author, pages, price):
        self.name = name
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"'{self.name}' by {self.author}, {self.pages} pages, ${self.price:.2f}"
