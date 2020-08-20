# Writes to a text file and puts in it the content of another text file
def copy_text():
    with open('test.txt', 'r') as rf:
        with open('test_copy.txt', 'w') as wf:
            for line in rf:
                wf.write(line)

# Copies an image - using binary read and binary write
def copy_image():
    with open('sky.jpg', 'rb') as rf:
        with open('sky_copy.jpg', 'wb') as wf:

            # Number of data we read from our copy
            chunk_size = 4096
            # Reads the first chunk of data
            rf_chunk = rf.read(chunk_size)
            while len(rf_chunk) > 0:
                # Copies the chunk
                wf.write(rf_chunk)

                # Reads next chunk from file
                rf_chunk = rf.read(chunk_size)


copy_text()
copy_image()