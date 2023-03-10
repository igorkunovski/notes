"""Class Book is used for collection and working with notes"""

import console
from note_class import Note


class Book:
    def __init__(self):
        self.book_lst = []

    def note_qty(self):
        return len(self.book_lst)

    def add_note(self, note: Note):
        self.book_lst.insert(0, note)

    def print_book(self):
        if self.note_qty() > 0:
            for note in self.book_lst:
                print(self.book_lst.index(note) + 1)
                note.print_note()
        else:
            console.no_notes()

    def remove_note(self, note_number: int):
        if self.note_qty() > 0 and self.note_qty() >= note_number:
            self.book_lst.pop(note_number - 1)
            console.remove_success()
        else:
            console.incorrect_note_num()

    def clear_book(self):
        self.book_lst.clear()
        console.remove_success()

    def get_note(self, note_number: int):
        if self.note_qty() > 0 and self.note_qty() >= note_number:
            return self.book_lst[note_number - 1]
        else:
            console.incorrect_note_num()

    def note_titles(self):
        for note in self.book_lst:
            print(f'{(self.book_lst.index(note) + 1)}. {note.tite}')
