import requests
from datetime import datetime as dt, timedelta
import numpy as np

def get_data(is_west: bool = True):
    if is_west:
        URL = "https://norlys.dk/api/flexel/getall?days=1&sector=DK1&isBusiness=false"
    else:
        URL = "https://norlys.dk/api/flexel/getall?days=1&sector=DK2&isBusiness=false"

    r = requests.get(url=URL)
    data = r.json()

    return data

def parse_data(arg_data):
    # convert time
    today_date = dt.strptime(arg_data["PriceDate"], '%Y-%m-%dT%H:%M:%SZ')

    prices = [i["value"] for i in arg_data["DisplayPrices"]]
    prices = np.array(prices)

    min_index = int(np.argmin(prices))
    min_time = dt.time(today_date + timedelta(hours=min_index))

    max_index = int(np.argmax(prices))
    max_time = dt.time(today_date + timedelta(hours=max_index))

    print(f"MOST EXPENSIVE: {prices[max_index]} at {max_time}")
    print(f"CHEAPEST: {prices[min_index]} at {min_time}")

def get_today_prices():
    parse_data(get_data()[0])


def get_tomorrow_prices():
    parse_data(get_data()[1])


if __name__ == "__main__":
    get_today_prices()
    get_tomorrow_prices()