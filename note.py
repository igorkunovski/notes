"""Program entry point"""

import config_db
from book_class import Book
from ui_class import Ui

if __name__ == '__main__':
    book = Book()
    config_db.load(book)
    ui = Ui()
    ui.run(book)

