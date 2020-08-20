# Tells how many characters have been read
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    print(f.tell())

# Prints size_to_read number of characters
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0) # Sets position back to the beginning of he file

    f_contents = f.read(size_to_read)
    print(f_contents)