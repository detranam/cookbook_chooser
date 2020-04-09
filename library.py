#This file will deal with all the JSON parsing, both in and out, to allow for
#book manipulation in this library.
#This file should also be the main command line application, allowing for pretty-printing of 
#the entire library. This should also allow us to randomly choose a page from ALL BOOKS, a subgenre of books.


import json
import argparse
import book_manager
from tabulate import tabulate
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--addbook", action="count", default=0,
                    help="add a book to our library")
parser.add_argument("-l", "--listbooks", action="count", default=0,
                    help="lists all the books in our library")
parser.add_argument("-r", "--randomrecipe", action="count", default=0,
                    help="will pick a random page from a random book")
args = parser.parse_args()

if not args:
    exit(1)

if args.addbook:
    new_book = book_manager.Book()
    chapter_count = (int)(input("How many chapters? :"))
    new_book.add_chapter(chapter_count)
    with open("test.json", "w") as writefile:
        json.dump(json.loads(new_book._book_string), writefile)