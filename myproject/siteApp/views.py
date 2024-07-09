from django.shortcuts import render
from typing import NamedTuple
from datetime import datetime
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def get_ell(path):
    file_path = os.path.join(BASE_DIR, 'siteApp', 'static', path)
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        ticker_descriptions = []
        ticker_names = []
        ticker_sectors = []
        for line in lines:
            splited = line.split(';')
            ticker_name = splited[0]
            sector = splited[1]
            description = ';'.join(splited[2:])
            ticker_names.append(ticker_name)
            ticker_sectors.append(sector)
            ticker_descriptions.append(description)
                                                        #  sector=sector,
                                                        #  description=description

    print(len(ticker_names), len(ticker_sectors), len(ticker_descriptions))


    values = zip(ticker_sectors, ticker_descriptions)

    info = {}
    for key, value in zip(ticker_names, values):
        info[key] = value

    return info


def index(request):
    elements = list(get_ell('data\\tickers.csv').keys())
    
    timestamp = datetime.now().timestamp()
    return render(request, 'index.html', {'elements': elements, 'timestamp': timestamp})