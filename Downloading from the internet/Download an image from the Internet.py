import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)


url = input("Enter URL of the picture you wanna download: ")
download_web_image(url)
