import requests
from bs4 import BeautifulSoup

results = requests.get('https://www.whitehouse.gov/issues/economy-jobs/')
source = results.content
soup = BeautifulSoup(source, 'lxml')

urls = []
for h2_tag in soup.find_all('h2'):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

print(urls)