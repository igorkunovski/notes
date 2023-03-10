"""Module for operating with DB in .csv format"""

from book_class import Book
import console
from note_class import Note


pathCSV = 'db.csv'


def save(book: Book):
    with open(pathCSV, 'w', encoding='utf-8') as file:
        for note in book.book_lst:
            file.write(note.note_to_str_line() + ';\n')
    console.saved_success()


def load(book: Book):
    try:
        with open(pathCSV, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.replace('\n', '')
                temp_note = Note.str_to_note(line)
                book.add_note(temp_note)
    except FileNotFoundError:
        console.file_not_found()
        exit()
    console.load_success()
    return book

