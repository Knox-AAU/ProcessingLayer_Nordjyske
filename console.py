from datetime import datetime
import sys
import os
from colorama import Fore

def print_warning(msg):
    print(f'{Fore.YELLOW}WARNING: {Fore.WHITE}'+msg)

def print_error(msg):
    print(f'{Fore.RED}ERROR: {Fore.WHITE}'+msg)

def update_status_console(num_of_files, current_file, start_time):
    os.system('cls')
    print(f'{Fore.BLUE}File ' + str(current_file) + ' of ' + str(num_of_files))
    print(f'{Fore.WHITE}Time passed: '+ str(datetime.now() - start_time))

def console_confirmation():
    print(f'{Fore.MAGENTA}Are you sure you want to insert all articles in the directory?')
    print(f'{Fore.WHITE}Make sure the database does not have data in it')
    input_str = input('Type "yes": ')
    if input_str == 'yes':
        return
    else:
        sys.exit()
