#
"""Book object manager and book creator

This file allows for the creation of books and chapters, objects 
that are useful in the creation and modification of the library.json 
file.
"""

__author__ = "detranam"
__copyright__ = ""
__version__ = "1.0.2"
__maintainer__ = "detranam"
__status__ = "Development"

if __name__ == "__main__":
    exit(1)


class Book(object):
    def __init__(self):
        title = input("Book title:")
        book_type = input("Type- [specialty, drink, food] :")
        length = input("Book length:")
        description = input("Book description:")

        # now we should make as unique an id as we can: take the first letter
        # of each word of the title and concatenate them into a 'unique id'
        split = title.split()
        id = ""
        for x in split:
            id += x[0]
        id += (str)(len(title))

        # create a.json friendly book string to allow this Book
        # to be added to the library.json file
        self._book_string = ("{" + f"\"title\":\"{title}\"," +
            f"\"type\":\"{book_type}\"," +
            f"\"length\":\"{length}\"," +
            f"\"description\":\"{description}\"," +
            f"\"uniqueid\":\"{id}\"," +
            f"\"chapters\":[")

    def add_chapter(self, num_chapters):
        for x in range(num_chapters):
            y = x+1
            chap_name = input(f"Enter chapter {y} name: ")
            start_page = (int)(input("Enter start page: "))
            end_page = (int)(input("Enter ending page : "))
            # create a .json friendly chapter string to add to
            # our chapter list for a given book
            self._book_string += ("{" +
                f"\"number\":\"{y}\"," +
                f"\"title\":\"{chap_name}\"," +
                f"\"start_page\":\"{start_page}\"," +
                f"\"end_page\":\"{end_page}\"" +
                "}")
            # there must be a comma between every chapter until
            # the final chapter, thus there must be an added
            # comma for all but the last chapter
            if y != num_chapters:
                self._book_string += ","
        self._book_string += "]}"
