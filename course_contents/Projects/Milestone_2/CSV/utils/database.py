""" In Memory Database  """
import json
import csv

book_libray=[]

def load_book_library(file):
    with open(file,"r") as file:
        books=file.readlines()
        books_list=[line.strip().split(",") for line in books]

    for book in books_list[1:]:
        dict_book = dict(zip(books_list[0],book))
        book_libray.append(dict_book)
    return book_libray,books_list

def save_book_library(file_name,book):
    csv_fieldnames=["name","author","read"]
    try:
        with open(file_name, 'w') as file:
            writer = csv.DictWriter(file,fieldnames =csv_fieldnames,lineterminator='\n' )
            writer.writeheader()
            for data in book:
                writer.writerow(data)

    except IOError:
        print("I/O error")

   # return book







