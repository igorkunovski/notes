"""Class Ui(User Interface) connects User command and App possibilities"""

import support
from book_class import Book
import config_db
import console
from note_class import Note


class Ui:

    @staticmethod
    def run(book: Book):
        while True:
            console.main_menu()
            choice = support.read_choice()

            match choice:
                case 1:
                    book.print_book()
                case 2:
                    book.add_note(Note(support.title(), support.text()))

                case 3:
                    book.note_titles()
                    choice = support.read_choice()
                    print(f'Old text: {book.get_note(choice).read_text()}')
                    text = support.text()
                    book.get_note(choice).edit_text(text)

                case 4:
                    book.note_titles()
                    choice = support.read_choice()
                    print(f'Note text: {book.get_note(choice).read_text()}')

                case 5:
                    book.note_titles()
                    choice = support.read_choice()
                    book.remove_note(choice)

                case 6:
                    if support.double_check():
                        book.clear_book()
                    else:
                        console.not_confirmed()

                case 7:
                    config_db.save(book)
                    console.buy()
                    break

                case _:
                    console.incorrect_cmd_num()

