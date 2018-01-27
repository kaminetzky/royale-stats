import requests
import logging


class Wrapper:
    def __init__(self, key, clan_tag):
        self.key = key
        self.url = 'http://api.cr-api.com/clan/' + clan_tag
        self.data = None
        self.update_data()

    def update_data(self):
        headers = {'auth': self.key}
        try:
            self.data = requests.get(self.url, headers=headers).json()
        except requests.exceptions.RequestException as err:
            logging.error(err)
            self.data = {'error': True, 'message': err}
