"""Module with Console output messages"""


def main_menu():
    print('----------------')
    print('----COMMANDS----')
    print('----------------')
    print('1. Print all notes')
    print('2. Add new note')
    print('3. Edit note')
    print('4. Print text of note by number')
    print('5. Remove note by number')
    print('6. Remove all notes from book')
    print('7. Save data and quit')
    print('-------------------------------')


def not_confirmed():
    print('-->Action was not confirmed<--')


def incorrect_cmd_num():
    print('-->Incorrect command number, please try again<--')


def incorrect_note_num():
    print('-->Incorrect NOTE number, please try again<--')


def buy():
    print('---BUY---')


def saved_success():
    print('-->Notes saved successfully to book<--')


def load_success():
    print('-->Notes downloaded successfully to book<--')


def no_notes():
    print('-->No notes in the Book<--')


def remove_success():
    print('-->Removed successfully<--')


def file_not_found():
    print('-->Database not found!<--')
    print('-->Application closed<--')

