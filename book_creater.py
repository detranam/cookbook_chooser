#This file will have both books and chapters as objects.
#Books will be collections of chapters. This file should also be able
#to return a newly created book, and thus create books, to the main library_controller to allow for this book to be written out to the json file.


class Book(object):
    def __init__(self, title, chapter_list):
        self.title = name
        self.chapters = chapter_list
    def add_chapter():
        chap_name = input("Enter chapter name: ")
        start_page = (int)input("Enter start page for {}: ", chap_name)
        end_page = (int)input("Enter ending page for {}: ", chap_name)
