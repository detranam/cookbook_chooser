#This file will have both books and chapters as objects.
#Books will be collections of chapters. This file should also be able
#to return a newly created book, and thus create books, to the main library_controller to allow for this book to be written out to the json file.

#todo remove this import
import json
class Book(object):
    def __init__(self):
        self._book_string = "{"
        title = input("Book title:")
        book_type = input("Type- [specialty, drink, food] :")
        num_chapters = (int)(input("number of chapters:"))
        length = input("Book length:")
        description = input("Book description:")
        tempvar = 0
        _book_string = _book_string + (f"\"title\":\"{title}\"," +
            f"\n\"type\":\"{book_type}\","+
            f"\n\"length\":\"{length}\","+
            f"\n\"description\":\"{description}\","+
            f"\"chapters\":[")

    def add_chapter(num_chapters):
        for x in range(num_chapters-1):
            chap_name = input("Enter chapter name: ")
            start_page = (int)(input("Enter start page for {}: ", chap_name))
            end_page = (int)(input("Enter ending page for {}: ", chap_name))
            _book_string = _book_string + ("{" +
                f"\n\"title\":\"{chap_name}\","+
                f"\n\"start_page\":\"{starting_page}\","+
                f"\n\"end_page\":\"{end_page}\""+
                "}")
        _book_string = _book_string + "]\n}"
        return _book_string
