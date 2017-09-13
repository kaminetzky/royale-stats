import requests


class Wrapper:
    def __init__(self, clan_tag):
        self.url = 'http://api.cr-api.com/clan/' + clan_tag

    def get_json(self):
        try:
            return requests.get(self.url).json()
        except requests.RequestException:
            return {'OK': False}
