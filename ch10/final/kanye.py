import requests
class YePI:
    def __init__(self):
        '''
        initializes the Kanye quote API
        args: None
        '''
        self.url = 'https://api.kanye.rest/'

    def get_quote(self):
        '''
        gets a random quote using the API
        args: None
        returns: quote(str)
        '''
        response = requests.get(self.url)
        data = response.json()
        quote = data['quote']
        return quote
    
    def __str__(self):
        '''
        specifies the url of the API used
        args: None
        returns: str
        '''
        return f'URL: {self.url}, no key needed'