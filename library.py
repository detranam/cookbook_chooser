#This file will deal with all the JSON parsing, both in and out, to allow for
#book manipulation in this library.
#This file should also be the main command line application, allowing for pretty-printing of 
#the entire library. This should also allow us to randomly choose a page from ALL BOOKS, a subgenre of books.


import json
import argparse
import book_manager
import os
from tabulate import tabulate
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--addbook", action="count", default=0,
                    help="add a book to our library")
parser.add_argument("-l", "--listbooks", action="count", default=0,
                    help="lists all the books in our library")
parser.add_argument("-r", "--randomrecipe", action="count", default=0,
                    help="will pick a random page from a random book")
args = parser.parse_args()

def add_book():
    new_book = book_manager.Book()
    chapter_count = (int)(input("How many chapters? :"))
    new_book.add_chapter(chapter_count)
    # You have to do this to remove the last ']}' from the file so that
    # we can add a book to our library JSON file
    # NOTE: This is only good for UTF-8 encoded objects
    with open("library.json", "r") as read_file:
        tempdata = json.load(read_file)
        #json.dump(json.loads(temp_book_string), writefile, indent=2)
    # tempdata.update(json.loads(new_book._book_string))
    tempdata["library"].append(json.loads(new_book._book_string))
    with open("library.json", "w") as write_file:
        json.dump(tempdata, write_file)

if not args:
    exit(1)

if args.addbook:
    # If our file already exists, append to it
    if(os.path.exists('library.json')):
        add_book()
    else:
        with open("library.json", "w") as initial_write:
            initial_write.write("{\"library\": []}")
        add_book()
