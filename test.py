import requests
import sys
from lxml import html

from MobileSearchParameters import MobileSearchParameters
# from MainWindow import MainWindow
# from PyQt5.QtWidgets import QApplication

# url = "http://suchen.mobile.de/fahrzeuge/search.html?isSearchRequest=true&usage=NEW&usage=USED&usageType=PRE_REGISTRATION&makeModelVariant1.makeId=3500&makeModelVariant1.modelId=20&maxPrice=4000&minFirstRegistrationDate=&maxMileage=&ambitCountry=&zipcode="
mobile_bmw = {'525': 'http://suchen.mobile.de/fahrzeuge/search.html?isSearchRequest=true&usage=NEW&usage=USED&usageType=PRE_REGISTRATION&makeModelVariant1.makeId=3500&makeModelVariant1.modelId=20&maxPrice=4000&minFirstRegistrationDate=&maxMileage=&ambitCountry=&zipcode=',
              '530': 'http://suchen.mobile.de/fahrzeuge/search.html?isSearchRequest=true&scopeId=C&maxPrice=4000&makeModelVariant1.makeId=3500&makeModelVariant1.modelId=22&maxPowerAsArray=KW&minPowerAsArray=KW'}

header = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; de-de; HTC Magic Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}
model = '530'
res = requests.get(mobile_bmw[model], headers=header)

tree = html.fromstring(res.content.decode('UTF-8'))
# page = BeautifulSoup(res.content)e
# print page.find('div', )
titles = tree.xpath('//div[@class="headline-block u-margin-bottom-9"]/span/text()')
prices = tree.xpath('//div[@class="price-block u-margin-bottom-9"]/span/text()')
image = tree.xpath('//div[@class="image-block"]/img/@src')

parameters = MobileSearchParameters()
#
# print(titles)
# print(prices)
# print("Image: ", image)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     mainWindow.buttonQuit.clicked.connect(app.quit)
#
#     sys.exit(app.exec_())
#
