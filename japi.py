from urllib import request
import json
from datetime import date, timedelta
def getStockData(stock_symbol):
    alpha_url = "https://www.alphavantage.co/query\?function=TIME_SERIES_DAILY&symbol=" + stock_symbol + "&apikey=P6F2LBGP6PGCPVV9"
    conn = request.urlopen(alpha_url)
    return conn.read().decode()

def main():
    symbol = input("Please enter company symbol? ")
    while symbol != "quit":
        try:
            json_data = getStockData(symbol)
            dict_data = json.loads(json_data)
            #print(dict_data)
            today = date.today() 
            yesterday = today - timedelta(days = 1) 
            print("The current price of %s is: $%s " % (symbol, dict_data["Time Series (Daily)"][str(yesterday)]["4. close"]))
            #print("The current price of %s is: %s" % (symbol,dict_data["Time Series (Daily)"][date.today()]["1. open"]))
        except:
            print("There was an error. Check your symbol and try agin.")
        symbol = input("Please enter company symbol? ")
main()
#print(getStockData("mar"))