import csv
import logging
import os


def remove_column(path, index):
    if not os.path.exists(path):
        logging.error('File does not exist.')
        raise FileNotFoundError()

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


def remove_non_members(input_path, output_path):
    if not os.path.exists(input_path):
        logging.error('File does not exist.')
        raise FileNotFoundError()

    with open(input_path, 'r') as input_file,\
            open(output_path, 'w') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for line in reader:
            if line[-1] != '':
                writer.writerow(line)

