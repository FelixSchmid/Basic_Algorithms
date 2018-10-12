class Books:

    def __init__(self, title, author, isbn, pages):
        self.title = title
        self.author = list(author)
        self.isbn = isbn
        self.pages = pages
        
    def __str__(self):
        output = "Title: " + self.title + "\n"
        for el in self.author:
            output += "Author: " + self.el + "\n"       
        output += "ISBN: " + self.isbn + "\n"
        output += "Pages: " + str(self.pages)
        return output

    def add_author(self, author):
        self.author.append(author)
       
    def __gt__(self, other):
        return self.pages > other.pages

    def __eq__(self, other):
        return self.pages == other.pages
