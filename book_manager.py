# This file will have both books and chapters as objects.
# Books will be collections of chapters. This file should also be able
# to return a newly created book, and thus create books, to the main
# library_controller to allow for this book to be written out to the json file.

if __name__ == "__main__":
    exit(1)


class Book(object):
    def __init__(self):
        title = input("Book title:")
        book_type = input("Type- [specialty, drink, food] :")
        length = input("Book length:")
        description = input("Book description:")
        self._book_string = ("{" + f"\"title\":\"{title}\"," +
            f"\"type\":\"{book_type}\"," +
            f"\"length\":\"{length}\"," +
            f"\"description\":\"{description}\"," +
            f"\"chapters\":[")

    def add_chapter(self, num_chapters):
        for x in range(num_chapters):
            y = x+1
            chap_name = input(f"Enter chapter {y} name: ")
            start_page = (int)(input("Enter start page: "))
            end_page = (int)(input("Enter ending page : "))
            self._book_string += ("{" +
                f"\"number\":\"{y}\"," +
                f"\"title\":\"{chap_name}\"," +
                f"\"start_page\":\"{start_page}\"," +
                f"\"end_page\":\"{end_page}\"" +
                "}")
            if y != num_chapters:
                self._book_string += ","
        self._book_string += "]}"
