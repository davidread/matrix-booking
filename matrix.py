import os.path
import configparser

import requests


# filepaths tried in order until a file is found
SETTINGS_FILEPATH = ('matrix.ini', '~/.matrix.ini')

class MatrixClient(object):
    _settings = None

    def __init__(self, base_url='https://app.matrixbooking.com'):
        self.base_url = base_url
        username, password = self.get_credentials()
        self.requests_session = requests.Session()
        response = self.requests_session.post(
            '{}/api/v1/user/login'.format(self.base_url),
            json={'username': username, 'password': password})
        if not response.ok:
            raise Exception('Error logging in: {} {}'
                            .format(response.status_code, response.text))

    def get_with_full_url(self, url):
        response = self.requests_session.get(url)
        response.raise_for_status()
        return response.json()

    def get(self, api_resource, param_string):
        url = '{}/api/v1/{}?{}'.format(self.base_url, api_resource, param_string)
        print('Getting {}'.format(url))
        return self.get_with_full_url(url)

    def get_settings(self):
        if not self._settings:
            config = configparser.ConfigParser()
            for settings_filepath in SETTINGS_FILEPATH:
                settings_filepath = os.path.expanduser(settings_filepath)
                if os.path.exists(settings_filepath):
                    break
            else:
                raise Exception(
                    'Cannot find settings file in the expected places: {}'
                    .format(SETTINGS_FILEPATH))
            config.read(settings_filepath)
            self._settings = config
        return self._settings

    def get_credentials(self):
        credentials = self.get_settings()['credentials']
        return (credentials['username'], credentials['password'])

    # Higher level calls

    def get_my_bookings(self):
        url = 'https://app.matrixbooking.com/api/v1/user/current/bookings?include=locations&include=visit&include=facilities&include=extras&include=bookingSettings&include=layouts'
        return self.get_with_full_url(url)
