from datetime import datetime
import sys
import os

WARNING_TEXT = ''

class ConColors:
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\u001b[32m'
    RED = '\033[91m'
    WHITE = '\u001b[37m'
    MAGENTA = '\u001b[35m'

def print_warning(msg):
    global WARNING_TEXT
    WARNING_TEXT += f'{ConColors.YELLOW}\nWARNING: {ConColors.WHITE}' + msg
    print(WARNING_TEXT)

def print_error(msg):
    print(f'{ConColors.RED}ERROR: {ConColors.WHITE}'+msg)

def print_success(start_time, num_of_files):
    os.system('cls')
    info = str(num_of_files) + ' files where added in ' + str(datetime.now() - start_time)
    print(f'{ConColors.GREEN}SUCCESS \n{ConColors.WHITE}' + info)
    if WARNING_TEXT != '':
        print(f'{ConColors.YELLOW}Warnings: ' + WARNING_TEXT)

def update_status_console(num_of_files, current_file, start_time):
    os.system('cls')
    print(f'{ConColors.BLUE}File ' + str(current_file) + ' of ' + str(num_of_files))
    print(f'{ConColors.WHITE}Time passed: ' + str(datetime.now() - start_time))
    if WARNING_TEXT != '':
        print(f'{ConColors.YELLOW}Warnings: ' + WARNING_TEXT)

def confirmation_insert_arts():
    print(f'{ConColors.MAGENTA}Are you sure you want to insert all articles to the database ?')
    print(f'{ConColors.WHITE}Make sure you have set the right directory')
    input_str = input('Type "yes": ')
    if input_str != 'yes':
        sys.exit()

def confirmation_get_new_vecs():
    print('Do you want to get all new word vecs from the database?')
    input_str = input('Type "yes" or "no": ')
    return input_str == 'yes'

def confirmation_insert_new_categories():
    print('Do you want to delete any existing categories and create new ones?')
    print('"Uncategorized" will not be deleted.')
    print('Note if articles have a reference to these categories it will result in an error.')
    input_str = input('Type "yes" or "no": ')
    return input_str == 'yes'

def print_process_percent(top_msg, current, max_num, start_time):
    os.system('cls')
    print(top_msg)
    print(f'{ConColors.BLUE}Processing {(current/max_num)*100}% done...')
    print(f'{ConColors.WHITE}Time passed: {datetime.now() - start_time}')

def print_menu():
    print(f'{ConColors.MAGENTA}Welcome{ConColors.WHITE}')
    print('Please select an option by typing its number:')
    print(f'{ConColors.BLUE}1.{ConColors.WHITE} Insert all articles to database')
    print(f'{ConColors.BLUE}2.{ConColors.WHITE} Generate word vecs')
    print(f'{ConColors.BLUE}3.{ConColors.WHITE} Do clustering and nearest articles')
    print(f'{ConColors.BLUE}4.{ConColors.WHITE} Insert clusters and nearest articles to database')
    return input()
