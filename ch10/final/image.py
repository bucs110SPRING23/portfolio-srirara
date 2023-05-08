import requests

class ImageAPI:
    def __init__ (self):
        '''
        initializes an image API instance
        args: None
        '''
        self.url = 'https://picsum.photos/1500/500'
    def get_photo(self):
        '''
        gets a random photo using an API
        args: None
        returns: response.url (str)
        '''
        response = requests.get(self.url)
        return response.url
    def __str__(self):
        '''
        specifies the url of the API used
        args: None
        returns: str
        '''
        return f'URL: {self.url}, no key needed'
