from utils import database

book_library,book_list=database.load_book_library("books.csv")
print(book_library)

def print_book_library(book_library):
    for book in book_library:
        print("Your book is")
        for key,value in book.items():
            print(f"{key}: {value}")


menu=""" Please specify what you want to do:
    a:to add a new book
    l:to list all books
    r:remove a book
    m:marked book as read  
    q:quit program
            
"""


while True:


    option=input(f"{menu} select your option: ")

    if option=="a":
        p

        new_book={k:input(f"Please enter {k}: ") for k in book_list[0]}
        book_library.append(new_book)
        database.save_book_library("books.csv", book_library)

    elif option=="l":
        print_book_library(book_library)

    elif option=="r":
        book_to_remove_name=input("Insert the name of the book you want to remove:")
        book_library=[book for book in book_library if book["name"]!=book_to_remove_name]
        print(book_library)
        database.save_book_library("books.csv", book_library)

    elif option=="m":

        read_book=input("Please enter the name of the book you have read: ")
        if any(book["name"]==read_book for book in book_library):
            for book in book_library:
                if book["name"]==read_book:
                    if book["read"] == "true":
                        print("book has been already read")
                    else:
                        book["read"] ="true"
                        database.save_book_library("books.csv", book_library)
        else:
            print("Book does not exist")

    elif option=="q":
        print("Thanks for using the book library")
        break
    else:
        print("Please enter only the keys previously specified")
        

