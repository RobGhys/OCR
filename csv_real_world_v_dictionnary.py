import csv

html_output = ''
names = []

""" Difference with other file """
def populates_names():
    with open('patrons.csv', 'r') as data_f:
        csv_data = csv.DictReader(data_f)

        next(csv_data)

        for line in csv_data:
            # Don't add names where people are listed as 'No Reward' (= those shouldn't be displayed)
            if line['FirstName'] == 'No Reward':
                break
            names.append(f"{line['FirstName']} {line['LastName']}")


def print_names(all_names):
    for name in all_names:
        print(name)


def count_nb_contributors(output, contrib_names):
    '''Populates an html output '''
    output += f'<p>There are currently {len(names)} public conributors. Thank you!</p>'
    output += '\n<ul>'

    for name in contrib_names:
        output += f'\n\t<li>{name}</li>'

    output += '\n</ul>'
    print(output)


populates_names()
print_names(names)
count_nb_contributors(html_output, names)