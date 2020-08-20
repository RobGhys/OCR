# File Objects

'''Recommended'''
# Context manager - will automatically close the file at the end of the app

# Reads data
print('------------------------')
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)


# Reads data in a list
print('------------------------')
with open('test.txt', 'r') as f:
    f_contents_w_lines = f.readlines()
    print(f_contents_w_lines)


# Good for memory: reads lines one at a time
print('------------------------')
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')


# Prints out the first x characters of the file
print('------------------------')
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
