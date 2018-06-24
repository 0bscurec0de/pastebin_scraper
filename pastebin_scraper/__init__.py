import os
from json.decoder import JSONDecodeError
from urllib.parse import urljoin
from requests import session

from pastebin_scraper.constraints import SUPPORTED_LANGUAGES


class Pastebin(object):
    """
    Pastebin's Scraping API Handler

    """
    __api_root = 'https://scrape.pastebin.com/'

    def __init__(self):
        self.session = session()
        self.session.hooks = {
            'response': self.__api_check
        }

    @staticmethod
    def __api_check(response, *args, **kwargs):
        """
        Session Hook, validate if the response is correct or not

        :param response:
        :param args:
        :param kwargs:
        :return:
        """
        response.raise_for_status()

        if 'https://pastebin.com/doc_scraping_api' in response.text:
            raise RuntimeError(response.text.replace('\r\n', ' '))

    @staticmethod
    def get_supported_languages():
        return SUPPORTED_LANGUAGES

    @staticmethod
    def __save_file(file_path: str, buffer: str):
        """
        Save file to disk

        :param file_path: Path where the file will be saved
        :param buffer: Buffer containing the data to save
        :return:
        """
        with open(file_path, 'w') as f:
            f.write(buffer)

    def __query(self, url_pattern: str):
        """
        Connects Pastebin API

        :param url_pattern: URL pattern to connect
        :return:
        """
        response = self.session.request('GET', urljoin(self.__api_root, url_pattern))

        try:
            return response.json()
        except JSONDecodeError:
            return response.text

    def get_pastes_list(self, limit=0, language=''):
        """
        Get list of last reported pastes

        :param limit: Desired amount of pastes
        :param language: Desired programming language
        :return:
        """
        base_url = 'api_scraping.php'

        if not limit and not language:
            return self.__query(base_url)
        elif not limit and language and language in SUPPORTED_LANGUAGES.keys():
            return self.__query(base_url + '?lang={}'.format(language))
        elif limit and not language and 1 <= limit <= 250:
            return self.__query(base_url + '?limit={}'.format(limit))
        elif limit and language and language in SUPPORTED_LANGUAGES.keys() and 1 <= limit <= 250:
            return self.__query(base_url + '?limit={}&&lang={}'.format(limit, language))
        else:
            raise ValueError('Wrong options were provided')

    def get_paste_raw(self, paste_key: str):
        """
        Get paste's content (on memory)

        :param paste_key: Unique paste's key
        :return:
        """
        return self.__query('api_scrape_item.php?i={}'.format(paste_key))

    def get_paste_metadata(self, paste_key: str):
        """
        Get paste's metadata

        :param paste_key: Unique paste's key
        :return:
        """
        return self.__query('api_scrape_item_meta.php?i={}'.format(paste_key))[0]

    def download_paste(self, paste_key: str, file_path):
        """
        Get paste's content (on disk)

        :param paste_key: Unique paste's key
        :param file_path: File path where the paste will be stored
        :return:
        """
        self.__save_file(os.path.join(file_path, paste_key), self.get_paste_raw(paste_key))


pastebin_scrapper = Pastebin()
