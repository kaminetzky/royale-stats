import csv
import logging
import os


def remove_column(path, index):
    if not os.path.exists(path):
        logging.error('File does not exist.')
        return False

    with open(path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    if index in [0, -len(data[0])]:
        logging.error('Can not remove first column.')
        return False
    elif index >= len(data[0]) or index < -len(data[0]):
        logging.error('Column does not exist.')
        return False

    new_data = [row[:index] + row[index + 1:] for row in data]

    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(new_data)


if __name__ == '__main__':
    pass
    # remove_column('donations.csv', 1)
    # remove_column('crowns.csv', 1)
