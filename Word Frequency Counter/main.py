import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []

    connect = requests.get(url)
    source = connect.content
    soup = BeautifulSoup(source, "lxml")
    for post_text in soup.find_all('h2'):
        content = post_text.find('a')
        filtered = content.string.lower().split()
        for each_word in filtered:
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()+{}|:\"<>?[]\;',./_+"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)
start('https://www.whitehouse.gov/issues/economy-jobs/')
