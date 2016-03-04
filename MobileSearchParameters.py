# This class to incapsulate the search parameters
# for mobile.de website

from requests import get
from lxml import html

class MobileSearchParameters:
    # Model
    model = '530'
    mark = 'BMW'

    def __init__(self):
        print(__name__, ' is initializated!')
        self.get_models()


    def get_models(self):
        res = get('http://www.mobile.de/')
        page = html.fromstring(res.content.decode('UTF-8'))
        print (res.content.decode('UTF-8'))
        i = 1
        for make in page.xpath('//select[id="qsmake"]/option/text()'):
            print(i, make)
            i += 1

