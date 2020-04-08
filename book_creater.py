#This file will have both books and chapters as objects.
#Books will be collections of chapters. This file should also be able
#to return a newly created book, and thus create books, to the main library_controller to allow for this book to be written out to the json file.


class Book(object):
    def __init__(self, title, chapter_list):
        self.title = name
        self.chapters = chapter_list


class Chapter(object):
    def __init__(self, chapter_name, start_page, end_page):
        self.name = chapter_name
        self.start_page = start_page
        self.end_page = end_page
