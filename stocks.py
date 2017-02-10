from __future__ import print_function
from urllib2 import urlopen
import json, os
# import subprocess
# from twilio.rest import TwilioRestClient
import config
import datetime

stock_price = []
dg_price = []
weather = []

str_build = ""
# appid = config.api['weather']
# link = "http://api.openweathermap.org/data/2.5/weather?q=NewYork&APPID=" + appid
# data = urlopen(link).read().decode('ascii')
# result = json.loads(data)
# status = result['weather'][0]['description']
#
# if status.find('drizzle') or status.find('rain'):
#     str_build = "Yes, there will be " + status + " today"
# else:
#     str_build = "No, there won't be any rain today "
#
#
# print(str_build)

stock_list = ['CMCSA', 'TWTR', 'HDP']

    # for elem in stock_list:
    #     link = "https://www.quandl.com/api/v3/datasets/WIKI/" + elem + ".json?api_key=" + config.api['quandl']
    #     data = urlopen(link).read().decode('ascii')
    #     result = json.loads(data)
    #     stock_price.append(result['dataset']['data'][0][4])
for elem in stock_list:
    link = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol=" + elem
    data = urlopen(link).read().decode('ascii')
    result = json.loads(data)
    stock_price.append(result['LastPrice'])

speech_output = "Comcast stock is currently priced at " + str(stock_price[0]) + " Twitter stock is currently at " + str(stock_price[1]) + " and hortonworks stock is currently priced at " + str(stock_price[2])
print(speech_output)
