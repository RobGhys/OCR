'''
Tuto can be found at: https://www.youtube.com/watch?v=ve2pmm5JqmI&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=14
'''
import os

os.chdir('/Users/rob/Documents/photosmaisons') # Folder where the files are located

# print(os.getcwd()) # Make sure we are on the right directory


def show_files_names():
    '''Shows all files names'''
    for f in os.listdir():
        print(f)


def split_name_from_format():
    '''
    Separates the extention from the rest of the name
    Returns a tuple with both info for each item
    '''
    for f in os.listdir():
        print(os.path.splitext(f))


def get_name_without_extention():
    '''
    Shows lists containing 2 elements : what is before '_' and what is after
    '''
    for i, f in enumerate(os.listdir()):
        f_name, f_ext = os.path.splitext(f)
        f_title, f_number = f_name.split('_')
        f_title = f_title.strip()
        f_number = f_number.strip()
        new_name = 'Maison {}{}'.format(i, f_ext)

        os.rename(f, new_name)


get_name_without_extention()