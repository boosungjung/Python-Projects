from urllib import request

down_url = 'https://datahub.io/core/exchange-rates/r/daily.csv'


def download_data(csv_url):

    response = request.urlopen(csv_url) #connects python to the internet
    csv = response.read()
    csv_str = str(csv) #converts everything into a string so no numerical errors
    lines = csv_str.split("\\n")
    dest_url = r'usd_exchange_rate.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_data(down_url)