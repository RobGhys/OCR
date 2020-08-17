import os

path = '/Users/rob/'
#os.chdir(path)

# Generator that Yields a tuple of 3 values:
# Directory path + directories within that path + files within that path
# Top-Down by default
"""
for dirpath, dirnames, filenames in os.walk(path):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
"""

# Get path to a folder
home_env = os.environ.get('HOME')
print(home_env)

# Create a path with folder name, and file name
test_file = 'test.txt'
file_path = os.path.join(home_env, test_file)
print(file_path)

# Gives the name of a portion of a path
print(os.path.basename('/tmp/test.txt')) # Base name == file name
print(os.path.dirname('/tmp/test.txt')) # Directory name == /tmp
print(os.path.split('/tmp/test.txt')) # Both of them in a tuple

# Check if a path exists on your directory
print(os.path.exists('/tmp/test.txt'))

# Check if the path is a directory or file
print(os.path.isdir('/tmp/test.txt')) # Directory or not
print(os.path.isfile('/tmp/test.txt')) # File or not

# Splits the file root, and the extension
# Trick to parse file name !
print(os.path.splitext('/tmp/test.txt')) # Gives a tuple