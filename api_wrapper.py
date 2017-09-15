import requests
import logging


class Wrapper:
    def __init__(self, clan_tag):
        self.url = 'http://api.cr-api.com/clan/' + clan_tag
        self.data = None
        self.update_data()

    def update_data(self):
        try:
            self.data = requests.get(self.url).json()
        except requests.exceptions.RequestException as err:
            logging.error(err)
            self.data = {'error': True, 'message': err}
