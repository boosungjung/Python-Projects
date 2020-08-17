from urllib.request import urlopen
from datetime import datetime
import os

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


url = 'https://markets.businessinsider.com/currencies/usd-krw'
high = int(input("Enter value you want to be notified at:"))


def download_data(csv_url):

    response = urlopen(csv_url)
    csv = str(response.read())
    line = csv.split("\\n")
    if line[1294][37:38] == ',':
        float_price = float(line[1294][31:37])
    else:
        live_price = line[1294][31:38]
        float_price = float(live_price)

    print(datetime.now(), "Price:", float_price)
    if float_price >= high:
        notify(title='USD/KRW 1200',
               subtitle='지금 환율 1200',
               message='지금 환율 1200')

while True:
    download_data(url)

