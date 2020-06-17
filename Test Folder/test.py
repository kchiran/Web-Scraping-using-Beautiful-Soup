from bs4 import BeautifulSoup
import urllib.request as request

folder = r'C:\Users\PC 50\Desktop\Test Folder' + '\\'
URL = 'https://www.google.com/about/products/'
response = request.urlopen(URL)
soup = BeautifulSoup(response, 'html.parser')

iconTable = soup.find('ul', {'class':'product-icon-list'})
icons = iconTable.find_all('li')

for icon in icons:
    request.urlretrieve(icon.img['data-lazy-src'], folder + icon.img['alt'] + '.png')