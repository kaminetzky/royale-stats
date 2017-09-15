from api_wrapper import Wrapper
import os
import datetime
import csv
import logging


class Logger:
    def __init__(self, clan_tag):
        self.wrapper = Wrapper(clan_tag)

    @staticmethod
    def log_data(path, new_data, log_total):

        if log_total:
            total = sum([player[1] for player in new_data])

        if os.path.exists(path):
            with open(path, 'r') as file:
                reader = csv.reader(file)
                if log_total:
                    dayweek_row, datetime_row, total_row, *data = list(reader)
                else:
                    dayweek_row, datetime_row, *data = list(reader)

            dayweek_row.append(datetime.datetime.now().strftime(
                "%A %W"))
            datetime_row.append(datetime.datetime.now().strftime(
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

            with open(path, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(dayweek_row)
                writer.writerow(datetime_row)
                if log_total:
                    writer.writerow(total_row)
                writer.writerows(data)

        else:
            with open(path, 'w') as file:
                new_data.sort()
                writer = csv.writer(file)
                writer.writerow(['Day / Week', datetime.datetime.now().strftime(
                    "%A %W")])
                writer.writerow(['Datetime', datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S")])
                if log_total:
                    writer.writerow(['Total', total])
                writer.writerows(new_data)

    def log_donations(self, path='donations.csv'):
        data = self.wrapper.get_json()
        if ('ok', False) in data.items():
            logging.error('Could not get data. Donations will not be saved.')
            return False
        new_donations = [[member['name'], member['donations']] for member in
                         data['members']]
        self.log_data(path, new_donations, True)
        logging.info('Successfully saved donation data.')

    def log_crowns(self, path='crowns.csv'):
        data = self.wrapper.get_json()
        if ('ok', False) in data.items():
            logging.error('Could not get data. Crowns will not be saved.')
            return False
        new_crowns = [(member['name'], member['clanChestCrowns']) for member in
                      data['members']]
        self.log_data(path, new_crowns, True)
        logging.info('Successfully saved crown data.')
