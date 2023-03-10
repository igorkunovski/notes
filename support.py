"""Module with support methods"""

import console


def read_choice():
    choice = input('-->Choose number and press Enter:  ')
    choice = choice.replace(' ', '')
    if choice.isdigit() and int(choice) > 0:
        return int(choice)
    else:
        console.incorrect_cmd_num()
        read_choice()


def title():
    new_title = input('-->Write NOTE title and press Enter:  ')
    return new_title


def text():
    new_text = input('-->Write NOTE text and press Enter:  ')
    return new_text


def double_check():
    print('-->Are You sure You want to delete all notes from the book?')
    yes = input('-->If YES press Y and Enter: ')

    if yes.replace(' ', '').upper() == 'Y':
        return True
    else:
        return False
