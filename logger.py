from api_wrapper import Wrapper
import os
import datetime
import csv
import logging


class Logger:
    def __init__(self, key, clan_tag):
        self.wrapper = Wrapper(key, clan_tag)

    @staticmethod
    def log_data(path, new_data, log_total):

        if log_total:
            total = sum([player[1] for player in new_data])

        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                if log_total:
                    dayweek_row, datetime_row, total_row, *data = list(reader)
                else:
                    dayweek_row, datetime_row, *data = list(reader)

            dayweek_row.append(datetime.datetime.utcnow().strftime(
                "%A %W"))
            datetime_row.append(datetime.datetime.utcnow().strftime(
                "%Y-%m-%d %H:%M:%S"))

            if log_total:
                total_row.append(total)

            for new_player in new_data:
                if new_player[0] not in [player[0] for player in
                                         data]:
                    new_row = ([new_player[0]] + [''] * (len(datetime_row) - 2)
                               + [new_player[1]])
                    data.append(new_row)
                else:
                    for player in data:
                        if new_player[0] == player[0]:
                            player.append(new_player[1])

            for player in data:
                if player[0] not in [new_player[0] for new_player in
                                     new_data]:
                    player.append('')

            data.sort()

            with open(path, 'w', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(dayweek_row)
                writer.writerow(datetime_row)
                if log_total:
                    writer.writerow(total_row)
                writer.writerows(data)

        else:
            with open(path, 'w', encoding='utf-8') as file:
                new_data.sort()
                writer = csv.writer(file)
                writer.writerow(['Day / Week', datetime.datetime.utcnow(
                    ).strftime("%A %W")])
                writer.writerow(['Datetime', datetime.datetime.utcnow(
                    ).strftime("%Y-%m-%d %H:%M:%S")])
                if log_total:
                    writer.writerow(['Total', total])
                writer.writerows(new_data)

    def log_donations(self, path='donations.csv', log_total=True):
        data = self.wrapper.data
        if ('error', True) in data.items():
            logging.error('Could not get data. Donations will not be saved.')
            return False
        new_donations = [[member['name'], member['donations']] for member in
                         data['members']]
        self.log_data(path, new_donations, log_total)
        logging.info('Successfully saved donation data.')

    def log_crowns(self, path='crowns.csv', log_total=True):
        data = self.wrapper.data
        if ('error', True) in data.items():
            logging.error('Could not get data. Crowns will not be saved.')
            return False
        new_crowns = [(member['name'], member['clanChestCrowns']) for member in
                      data['members']]
        self.log_data(path, new_crowns, log_total)
        logging.info('Successfully saved crown data.')
