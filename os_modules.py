import os
from datetime import datetime

# Shows current working directory
print(os.getcwd())

# Changes current directory
os.chdir('/Users/rob/')
print(os.getcwd())

# Lists files and folders in current directory
print(os.listdir())

# Create directory
os.mkdir('Pictures-2')

# Creates all the intermediate directories too
os.makedirs('Pictures-3/sub-pic-3')
print(os.listdir())

# Delete folders (removedirs : recursive)
os.rmdir('Pictures-2')
os.removedirs('Pictures-3/sub-pic-3')

# Rename file
os.mkdir('Test')
os.rename('Test', 'Test-lol')
print(os.listdir())

# Get info on file - size
print(os.stat('Test-lol').st_size)

# Get info on file - time last modified
mod_time = os.stat('Test-lol').st_mtime # returns a time stamp
print(datetime.fromtimestamp(mod_time))