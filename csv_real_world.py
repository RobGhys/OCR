import csv

html_output = ''
names = []


def populates_names():
    with open('patrons.csv', 'r') as data_f:
        csv_data = csv.reader(data_f)

        # The 2 first lines of the csv file = headers + bad data.
        # Don't want to show it.
        nbr_data_to_skip = 2
        for i in range(nbr_data_to_skip):
            next(csv_data)

        for line in csv_data:
            # Don't add names where people are listed as 'No Reward' (= those shouldn't be displayed)
            if line[0] == 'No Reward':
                break
            names.append(f"{line[0]} {line[1]}")


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