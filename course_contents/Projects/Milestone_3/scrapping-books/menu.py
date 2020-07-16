import logging
from app import  books

logger=logging.getLogger("scraping.menu")

USER_CHOICE=""" Enter one of the following:

-"b" to look  at 5-start books
-"c" to look at the cheapest books
-"n" to just et the next availabe book on catalog
-"q" to exit
"""


def menu():
    user_input=input(USER_CHOICE)
    while user_input!="q":
        if user_input=="b":
            print_best_books()
        elif user_input=="c":
            print_cheapest_books()
        elif user_input=="n":
            get_next_book()
        else:
            print("Please select a valid option")
        user_input=input(USER_CHOICE)

    logger.info("Terminating program")




def print_best_books():
    logger.info("Finding best books by rating")
    best_books=sorted(books,key=lambda x:x.rating,reverse = True)[:]
    for book in best_books:
        print(book)
def print_cheapest_books():
    logger.info("Finding cheapest books by ")
    cheapest_books=sorted(books,key=lambda x:x.price)
    for book in cheapest_books:
        print(book)

def print_books_sorted_by_author():
    books_sorted_by_author=sorted(books,key=lambda x:x.name)
    for book in books_sorted_by_author:
        print(book)

books_generator=(x for x in books)

def get_next_book():
    logger.info("Geting next book from the list")
    print(next(books_generator))

menu()
# print(len(books))
# print("------Best------")
# print_best_books()
# print("------Cheapest------")
# print_cheapest_books()
# print("------By Namme------")
# print_books_sorted_by_author()