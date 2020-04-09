#This file will have both books and chapters as objects.
#Books will be collections of chapters. This file should also be able
#to return a newly created book, and thus create books, to the main library_controller to allow for this book to be written out to the json file.

#todo remove this import
import json
class Book(object):
    def __init__(self):
        _book_string = "{"
        title = input("Book title:")
        book_type = input("Type- [specialty, drink, food] :")
        num_chapters = (int)(input("number of chapters:"))
        length = input("Book length:")
        description = input("Book description:")
        tempvar = 0
        _book_string = _book_string + ("\"title\":\"{title}\"," +
                  "\"type\":\"{book_type}\","+
                "\"length\":\"{length}\","+
                "\"description\":\"{description}\"}")#todo replace this } with ,
        #todo remove this useless test, uncomment the rest
        with open("bigtest.json", "w") as writefile:
            json.dump(json.loads(_book_string), writefile)

        #+
         #       "\"chapters\":["


       # while var < num_chapters:
       #     add_chapter()
    def add_chapter():
        chap_name = input("Enter chapter name: ")
        start_page = (int)(input("Enter start page for {}: ", chap_name))
        end_page = (int)(input("Enter ending page for {}: ", chap_name))
        _book_string = _book_string + "{"#todo finish this
