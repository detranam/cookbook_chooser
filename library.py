# This file will deal with all the JSON parsing, both in and out, to allow for
# book manipulation in this library.
# This file should also be the main command line application, allowing for
# pretty-printing of the entire library. This should also allow us to randomly
# choose a page from ALL BOOKS, a subgenre of books.


import json
import argparse
import book_manager
import os
import sys
from tabulate import tabulate
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--addbook", action="count", default=0,
                    help="add a book to our library")
parser.add_argument("-l", "--listbooks", action="count", default=0,
                    help="lists all the books in our library")
parser.add_argument("-r", "--randomrecipe", action="count", default=0,
                    help="will pick a random page from a random book")
args = parser.parse_args()

if not len(sys.argv) > 1:
    print("You must specify an argument!")
    print("Try \'library.py --help\' for more information")
    exit(1)


def add_book():
    new_book = book_manager.Book()
    chapter_count = (int)(input("How many chapters? :"))
    new_book.add_chapter(chapter_count)
    with open("library.json", "r") as read_file:
        tempdata = json.load(read_file)
    tempdata["library"].append(json.loads(new_book._book_string))
    with open("library.json", "w") as write_file:
        json.dump(tempdata, write_file)


if args.addbook:
    # If our file already exists, append a new book to it
    if(os.path.exists('library.json')):
        add_book()
    else:
        with open("library.json", "w") as initial_write:
            initial_write.write("{\"library\": []}")
        add_book()

if args.listbooks:
    if(os.path.exists('library.json')):
        with open("library.json", "r") as read_file:
            booklist = json.load(read_file)
            headers = ["Book Index", "Title"]
            book_printer = []
            x = 0
            while x < len(booklist["library"]):
                book_to_add = [x, booklist["library"][x]["title"]]
                book_printer.append(book_to_add)
                x += 1

            print(tabulate(book_printer, headers, tablefmt="fancy_grid"))
    else:
        print("No library.json file exists")
