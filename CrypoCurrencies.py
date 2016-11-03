from threading import Thread
import pandas as pd
import json
import urllib.request
from crontab import CronTab

price_data = []
# TODO: function to write out to csv
# TODO: function to send txt notification
# TODO: cron to run at least twice a day, for csv and text

def getCurrencyPrice(ticker, symbol):
    link = 'https://www.cryptocompare.com/api/data/price?fsym=' + ticker + '&tsyms=' + symbol
    data = urllib.request.urlopen(link).read().decode('ascii')
    result = json.loads(data)
    print(ticker)
    try:
        print(result['Data'][0]['Price'])
        price_data.append(result['Data'][0]['Price'])
    except Exception as e:
        print("Error: " + str(e))

def main():
    t1 = Thread(target=getCurrencyPrice, args=('BTC', 'USD'))
    t1.start()
    # t2 = Thread(target=getCurrencyPrice, args=('LTC', 'USD'))
    # t2.start()
    # t3 = Thread(target=getCurrencyPrice, args=('XRP', 'USD'))
    # t3.start()
    # t4 = Thread(target=getCurrencyPrice, args=('ETH', 'USD'))
    # t4.start()
    # t5 = Thread(target=getCurrencyPrice, args=('ETC', 'USD'))
    # t5.start()
    # t6 = Thread(target=getCurrencyPrice, args=('DOGE', 'USD'))
    # t6.start()
    # t7 = Thread(target=getCurrencyPrice, args=('BAY', 'USD'))
    # t7.start()
    # t8 = Thread(target=getCurrencyPrice, args=('WARP', 'USD'))
    # t8.start()
    # t9 = Thread(target=getCurrencyPrice, args=('XPOKE', 'USD'))
    # t9.start()
    # t0 = Thread(target=getCurrencyPrice, args=('DRACO', 'USD'))
    # t0.start()

    t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()
    # t7.join()
    # t8.join()
    # t9.join()
    # t0.join()

    print(price_data)


if __name__ == '__main__':
    main()
