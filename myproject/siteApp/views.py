from django.shortcuts import render, get_object_or_404
from typing import NamedTuple
from datetime import datetime
import os
from django.shortcuts import render, get_object_or_404
from typing import NamedTuple
from datetime import datetime
import os
import sys
import django

# Добавляем корневую директорию проекта в sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Инициализируем Django
django.setup()

from .models import Ticker 

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

    values = zip(ticker_sectors, ticker_descriptions)

    info = {}
    info_sec = {}
    info_des = {}
    for key, value in zip(ticker_names, values):
        info[key] = value
    
    for key, value in zip(ticker_names, ticker_sectors):
        info_sec[key] = value
    
    for key, value in zip(ticker_names, ticker_descriptions):
        info_des[key] = value

    return [info, info_sec, info_des]

def index(request):
    elements = list(get_ell('data/tickers.csv')[0].keys())
    info = get_ell('data/tickers.csv')[0]
    info_sec = get_ell('data/tickers.csv')[1]
    info_des = get_ell('data/tickers.csv')[2]
    timestamp = datetime.now().timestamp()
    return render(request, 'index.html', {'elements': elements, 'info': info, 'info_sec': info_sec, 'info_des': info_des, 'timestamp': timestamp})

def ticker_detail(request, name):
    ticker = get_object_or_404(Ticker, name=name)
    return render(request, 'ticker_detail.html', {'ticker': ticker})




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
    info_sec = {}
    info_des = {}
    for key, value in zip(ticker_names, values):
        info[key] = value
    
    for key, value in zip(ticker_names, ticker_sectors):
        info_sec[key] = value
    
    for key, value in zip(ticker_names, ticker_descriptions):
        info_des[key] = value

    return [info, info_sec, info_des]


def index(request):
    elements = list(get_ell('data\\tickers.csv')[0].keys())
    info = get_ell('data\\tickers.csv')[0]
    info_sec = get_ell('data\\tickers.csv')[1]
    info_des = get_ell('data\\tickers.csv')[2]
    timestamp = datetime.now().timestamp()
    return render(request, 'index.html', {'elements': elements, 'info': info, 'info_sec': info_sec, 'info_des': info_des, 'timestamp': timestamp})

def ticker_detail(request, name):
    ticker = get_object_or_404(Ticker, name=name)
    return render(request, 'ticker_detail.html', {'ticker': ticker})