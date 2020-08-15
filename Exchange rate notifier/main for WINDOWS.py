from urllib.request import urlopen
from datetime import datetime
from win10toast import ToastNotifier

toaster = ToastNotifier()


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
        toaster.show_toast("HIGH")

while True:
    download_data(url)
