"""Class Note holds properties of Note"""

import datetime


class Note:

    def __init__(self, title: str, text: str, date=None):

        if date is None:
            self.tite = title
            self.text = text
            self.date = str(datetime.datetime.now().strftime("%d %B %Y - %H:%M"))
        else:
            self.tite = title
            self.text = text
            self.date = date

    def read_text(self):
        return self.text

    def edit_text(self, new_text: str):
        self.text = new_text
        print('Text renewed')

    def print_note(self):
        print(f'Title: {self.tite}\n'
              f'Text:  {self.text} \n'
              f'Date:  {self.date} ')

    def note_to_str_line(self):
        return f'{self.tite};{self.text};{self.date}'

    @staticmethod
    def str_to_note(string: str):
        title = string.split(';')[0]
        text = string.split(';')[1]
        date = string.split(';')[2]

        return Note(title, text, date)
