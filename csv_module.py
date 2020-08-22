import csv

def read_csv_file():
    with open('names.csv', 'r') as csv_f:
        csv_reader = csv.reader(csv_f) # Separation default value is ','

        for line in csv_reader:
            print(line)

def read_email():
    with open('names.csv', 'r') as csv_f:
        csv_reader = csv.reader(csv_f) # Separation default value is ','

        # Generator will jump over the first value,
        # which is the name of the column and we don't want
        next(csv_reader)

        for line in csv_reader:
            print(line[2]) # E-mail is the 3rd element, hence line 2


def write_data():
    # Opens the origin file for reading
    with open('names.csv', 'r') as csv_f:
        # Reads file
        csv_reader = csv.reader(csv_f) # Separation default value is ','

        # Opens new file for writing
        with open('updated_names.csv', 'w') as new_f:
            # Opens a writer, with a 'tab' as delimiter
            csv_writer = csv.writer(new_f, delimiter='\t')

            # For each line of the original file, write it in the new file
            for line in csv_reader:
                csv_writer.writerow(line)


def read_with_dict():
    '''Reads a CSV file using the Dict Reader. '''
    # Opens the origin file for reading
    with open('names.csv', 'r') as csv_f:
        # Use a Dict Reader instead of a CSV Reader
        csv_reader = csv.DictReader(csv_f)

        for line in csv_reader:
            print(line)


def write_with_dict():
    '''Writes in a CSV file using the Dict Reader. '''
    # Opens the origin file for reading
    with open('names.csv', 'r') as csv_f:
        # Use a Dict Reader instead of a CSV Reader
        csv_reader = csv.DictReader(csv_f)

        with open('new_name.csv', 'w') as new_f:
            fieldnames = ['first_name', 'last_name', 'email']
            csv_writer = csv.DictWriter(new_f, fieldnames=fieldnames, delimiter='\t')

            # Writes the headers as first line
            csv_writer.writeheader()

            for line in csv_reader:
                csv_writer.writerow(line)


def write_with_dict_besides_email():
    '''Writes in a CSV file using the Dict Reader. '''
    # Opens the origin file for reading
    with open('names.csv', 'r') as csv_f:
        # Use a Dict Reader instead of a CSV Reader
        csv_reader = csv.DictReader(csv_f)

        with open('new_name_no_email.csv', 'w') as new_f:
            fieldnames = ['first_name', 'last_name']
            csv_writer = csv.DictWriter(new_f, fieldnames=fieldnames, delimiter='\t')

            # Writes the headers as first line
            csv_writer.writeheader()

            # Writes all fieldnames, except from 'email'
            for line in csv_reader:
                del line['email']
                csv_writer.writerow(line)

#read_csv_file()
#read_email()
#write_data()
#read_with_dict()
#write_with_dict()
#write_with_dict_besides_email()