import requests
import json


class WikipediaApiClient:
    """
    Wikipedia api client.
    """
    def __init__(self):
        """
        Initialize the client.
        """
        self._endpoint = 'http://ja.wikipedia.org/w/api.php'

    def get(self, titles):
        """
        Get contents corresponding to the titles.
        :param titles: a list of titles
        :return: a list of contents
        """
        params = {
            'format': 'json',
            'action': 'query',
            'prop': 'revisions',
            'rvprop': 'content',
            'titles': '|'.join(titles)
        }
        res = requests.get(self._endpoint, params=params)

        contents = []
        if res.status_code == 200:
            res_body = json.loads(res.text)
            for page in res_body['query']['pages'].values():
                contents.append(page['revisions'][0]['*'])
        return contents

    def search_random(self, limit):
        """
        Search titles randomly.
        :param limit: a limit number of titles
        :return: a list of titles
        """
        if limit is None:
            limit = 10

        params = {
            'format': 'json',
            'action': 'query',
            'list': 'random',
            'rnnamespace': 0,
            'rnlimit': limit
        }
        res = requests.get(self._endpoint, params=params)

        titles = []
        if res.status_code == 200:
            res_body = json.loads(res.text)
            for page in res_body['query']['random']:
                titles.append(page['title'])
        return titles

    def search(self, word):
        """
        Search title of articles including the word.
        :param word: a search word
        :return: a list of titles
        """
        params = {
            'format': 'json',
            'action': 'query',
            'list': 'search',
            'srsearch': word
        }

        res = requests.get(self._endpoint, params=params)

        titles = []
        if res.status_code == 200:
            res_body = json.loads(res.text)
            for page in res_body['query']['search']:
                titles.append(page['title'])
        return titles
