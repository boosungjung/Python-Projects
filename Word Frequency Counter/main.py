import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for post_text in soup.find_all('a', ('question-summary narrow tagged-interesting')):
        content = post_text.text
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)

start('https://stackoverflow.com/')
